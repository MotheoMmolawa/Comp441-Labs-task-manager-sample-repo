from copy import deepcopy

from app import tasks as task_manager


# Build fresh test data without relying on add_task().
def make_task(task_id, title, priority=1, done=False):
    return {
        "id": task_id,
        "title": title,
        "priority": priority,
        "tags": [],
        "done": done,
    }


# TC-401 / REQ-001: Add a task with the supplied values.
def test_TC401_add_task():
    tasks = []

    result = task_manager.add_task(
        tasks,
        "Write report",
        priority=2,
        tags=["school"],
    )

    assert len(tasks) == 1
    assert result is tasks[0]
    assert result["title"] == "Write report"
    assert result["priority"] == 2
    assert result["tags"] == ["school"]
    assert result["done"] is False


# TC-402 / REQ-002: Complete an existing task.
def test_TC402_complete_existing_task():
    tasks = [make_task(1, "Write report")]

    result = task_manager.complete_task(tasks, 1)

    assert result is True
    assert tasks[0]["done"] is True


# TC-403 / REQ-003: A missing ID must not change the list.
def test_TC403_complete_missing_task():
    tasks = [make_task(1, "Write report")]
    original = deepcopy(tasks)

    result = task_manager.complete_task(tasks, 99)

    assert result is False
    assert tasks == original


# TC-404 / REQ-004: Include every pending task in input order.
def test_TC404_get_all_pending_tasks():
    tasks = [
        make_task(1, "Task A", done=False),
        make_task(2, "Task B", done=True),
        make_task(3, "Task C", done=False),
    ]
    expected = deepcopy([tasks[0], tasks[2]])

    result = task_manager.get_pending_tasks(tasks)

    assert result == expected


# TC-405 / REQ-005: Calculate the average of three priorities.
def test_TC405_average_priority():
    tasks = [
        make_task(1, "Task A", priority=1),
        make_task(2, "Task B", priority=2),
        make_task(3, "Task C", priority=3),
    ]

    result = task_manager.average_priority(tasks)

    assert result == 2


# TC-406 / REQ-005: An empty list should have an average of zero.
def test_TC406_average_priority_empty_list():
    result = task_manager.average_priority([])

    assert result == 0


# TC-407 / REQ-006: Return the first exact title match.
def test_TC407_find_first_matching_title():
    tasks = [
        make_task(1, "Write report"),
        make_task(2, "Write report"),
    ]

    result = task_manager.find_task_by_title(tasks, "Write report")

    assert result is tasks[0]
    assert result["id"] == 1


# TC-408 / REQ-006: Return None when no title matches.
def test_TC408_find_missing_title():
    tasks = [make_task(1, "Write report")]

    result = task_manager.find_task_by_title(tasks, "Read notes")

    assert result is None


# TC-409 / REQ-007: Remove one task and preserve the others.
def test_TC409_remove_task():
    tasks = [
        make_task(1, "Task A"),
        make_task(2, "Task B"),
        make_task(3, "Task C"),
    ]
    expected = deepcopy([tasks[0], tasks[2]])

    task_manager.remove_task(tasks, 2)

    assert tasks == expected

    # Removing an ID that does not exist should change nothing.
    task_manager.remove_task(tasks, 99)

    assert tasks == expected


# TC-410 / REQ-008: Save and load tasks using a temporary file.
def test_TC410_save_and_load_tasks(tmp_path, monkeypatch):
    temporary_file = tmp_path / "tasks.json"
    monkeypatch.setattr(task_manager, "TASKS_FILE", str(temporary_file))

    tasks = [
        make_task(1, "Write report", priority=2, done=False),
        make_task(2, "Read notes", priority=3, done=True),
    ]
    tasks[0]["tags"] = ["school"]
    expected = deepcopy(tasks)

    task_manager.save_tasks(tasks)
    result = task_manager.load_tasks()

    assert temporary_file.exists()
    assert result == expected


# TC-411 / REQ-008: A missing file should produce an empty list.
def test_TC411_load_missing_file(tmp_path, monkeypatch):
    missing_file = tmp_path / "missing-tasks.json"
    monkeypatch.setattr(task_manager, "TASKS_FILE", str(missing_file))

    assert not missing_file.exists()

    result = task_manager.load_tasks()

    assert result == []