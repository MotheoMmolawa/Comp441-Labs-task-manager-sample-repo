from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TaskManagerPage:
    # Locators identify controls on the page.
    TITLE_INPUT = (By.ID, "task-title")
    ADD_BUTTON = (By.ID, "add-task")
    SEARCH_INPUT = (By.ID, "search-tasks")
    ERROR_MESSAGE = (By.ID, "error-message")
    TASK_COUNT = (By.ID, "task-count")
    TASK_ROWS = (By.CSS_SELECTOR, "#task-list .task-item")

    ROW_TITLE = (By.CSS_SELECTOR, ".task-title")
    ROW_STATUS = (By.CSS_SELECTOR, ".task-status")
    COMPLETE_BUTTON = (By.CSS_SELECTOR, ".complete-task")
    DELETE_BUTTON = (By.CSS_SELECTOR, ".delete-task")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.get(url)
        self.wait.until(
            EC.visibility_of_element_located(self.TITLE_INPUT)
        )

    def add_task(self, title):
        field = self.wait.until(
            EC.visibility_of_element_located(self.TITLE_INPUT)
        )
        field.clear()
        field.send_keys(title)

        self.wait.until(
            EC.element_to_be_clickable(self.ADD_BUTTON)
        ).click()

    def _find_task(self, title):
        """Find a visible task row by its exact title."""
        def locate(driver):
            for row in driver.find_elements(*self.TASK_ROWS):
                if row.is_displayed():
                    text = row.find_element(*self.ROW_TITLE).text
                    if text == title:
                        return row
            return False

        return self.wait.until(locate)

    def complete_task(self, title):
        row = self._find_task(title)
        row.find_element(*self.COMPLETE_BUTTON).click()

    def delete_task(self, title):
        row = self._find_task(title)
        row.find_element(*self.DELETE_BUTTON).click()
        self.wait.until(EC.staleness_of(row))

    def search(self, text):
        field = self.wait.until(
            EC.visibility_of_element_located(self.SEARCH_INPUT)
        )
        field.clear()
        field.send_keys(text)

    def visible_titles(self):
        """Return only titles currently visible on the page."""
        return [
            row.find_element(*self.ROW_TITLE).text
            for row in self.driver.find_elements(*self.TASK_ROWS)
            if row.is_displayed()
        ]

    def status_of(self, title):
        row = self._find_task(title)
        return row.find_element(*self.ROW_STATUS).text

    def error_text(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).text

    def total_count(self):
        text = self.driver.find_element(*self.TASK_COUNT).text
        return int(text.split(":")[-1].strip())