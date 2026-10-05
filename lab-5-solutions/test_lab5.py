import json
import os
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from task_manager_page import TaskManagerPage


# Read test inputs and expected results from the JSON file.
DATA_FILE = Path(__file__).with_name("test-data.json")
CASES = json.loads(DATA_FILE.read_text(encoding="utf-8"))


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()

    # Later, this setting will let us connect to Docker/Healenium.
    remote_url = os.getenv("SELENIUM_REMOTE_URL")

    if remote_url:
        browser = webdriver.Remote(
            command_executor=remote_url,
            options=options,
        )
    else:
        browser = webdriver.Chrome(options=options)

    try:
        browser.set_window_size(1200, 900)
        yield browser
    finally:
        # Close the browser even when a test fails.
        browser.quit()


@pytest.mark.parametrize(
    "case",
    CASES,
    ids=[case["id"] for case in CASES],
)
def test_task_manager(driver, case):
    page = TaskManagerPage(driver)

    # Each test opens a fresh page with no tasks.
    app_url = os.getenv("APP_URL", "http://localhost:8000")
    page.open(app_url)

    # Create any tasks needed before the action.
    for title in case["setup_tasks"]:
        page.add_task(title)

    action = case["action"]

    if action in ("add", "reject_blank"):
        page.add_task(case["title"])

    elif action == "complete":
        page.complete_task(case["target"])

    elif action == "delete":
        page.delete_task(case["target"])

    elif action == "search":
        page.search(case["search_text"])

    else:
        pytest.fail(f"Unknown test action: {action}")

    # Wait for the expected visible result.
    WebDriverWait(driver, 10).until(
        lambda _: page.visible_titles() == case["expected_titles"]
    )

    # Assertions check the actual behaviour against the JSON data.
    assert page.visible_titles() == case["expected_titles"]
    assert page.total_count() == case["expected_count"]

    if "expected_error" in case:
        assert page.error_text() == case["expected_error"]
    else:
        assert page.error_text() == ""

    if "expected_status" in case:
        target = case.get("target", case.get("title"))
        assert page.status_of(target) == case["expected_status"]