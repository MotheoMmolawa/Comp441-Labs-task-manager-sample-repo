# Lab 4 Test Cases

All 11 test cases passed after the fixes on 2026-10-05.
Execution evidence is recorded in test-results-after-fixes.txt.

| Test ID | Requirement | Setup and action | Expected result | Status |
|---|---|---|---|---|
| TC-401 | REQ-001 | Start with an empty list. Call add_task with title "Write report", priority 2, and tags ["school"]. | The list contains one task. The returned task has the supplied title, priority and tags, and done is False. | Passed |
| TC-402 | REQ-002 | Create an unfinished task with ID 1. Call complete_task with ID 1. | The function returns True and that task's done value becomes True. | Passed |
| TC-403 | REQ-003 | Create an unfinished task with ID 1. Call complete_task with ID 99. | The function returns False and the task list remains unchanged. | Passed |
| TC-404 | REQ-004 | Create tasks with IDs 1, 2 and 3. Set their done values to False, True and False respectively. Call get_pending_tasks. | The result contains exactly tasks 1 and 3, in that order. | Passed |
| TC-405 | REQ-005 | Create three tasks with priorities 1, 2 and 3. Call average_priority. | The result is 2. | Passed |
| TC-406 | REQ-005 | Call average_priority with an empty list. | The result is 0 and no exception occurs. | Passed |
| TC-407 | REQ-006 | Create two tasks titled "Write report", with IDs 1 and 2. Search for "Write report". | The function returns the first matching task, ID 1. | Passed |
| TC-408 | REQ-006 | Create a task titled "Write report". Search for "Read notes". | The function returns None. | Passed |
| TC-409 | REQ-007 | Create tasks with IDs 1, 2 and 3. Remove ID 2. Then attempt to remove ID 99. | After removing ID 2, tasks 1 and 3 remain unchanged and in order. Removing ID 99 makes no further change. | Passed |
| TC-410 | REQ-008 | Point TASKS_FILE to a temporary file. Save a task list containing both completed and unfinished tasks, then load it. | The loaded list equals the saved list, including every task field and task order. | Passed |
| TC-411 | REQ-008 | Point TASKS_FILE to a nonexistent file inside a temporary directory. Call load_tasks. | The result is an empty list. | Passed |