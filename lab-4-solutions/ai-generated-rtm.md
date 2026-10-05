| Requirement ID | Requirement Description | Test Case ID(s) | Test Description | Test Level | Status |
|---|---|---|---|---|---|
| REQ-001 | `add_task` shall append a task with the given title, a priority, tags, and `done` set to false. | TC-001 | Add a task to a list containing existing tasks. Verify that one task is appended, its title matches the supplied title, and existing tasks remain unchanged. | Unit | Not Run |
| REQ-001 | Same as above. | TC-002 | Add a task with an explicitly supplied priority and tags. Verify that the new task contains those values and that `done` is false. | Unit | Not Run |
| REQ-002 | `complete_task` shall mark an existing task done and return true. | TC-003 | Provide the ID of an existing pending task. Verify that its `done` value becomes true and the function returns true. | Unit | Not Run |
| REQ-003 | `complete_task` shall return false for a nonexistent ID and leave the task list unchanged. | TC-004 | Provide an ID absent from a populated task list. Verify that the function returns false and the entire list remains unchanged. | Unit | Not Run |
| REQ-004 | `get_pending_tasks` shall return every task whose `done` value is false, including a task at the first list position. | TC-005 | Use a list containing both pending and completed tasks, with a pending task at the first position. Verify that all pending tasks, including the first task, are returned and completed tasks are excluded. | Unit | Not Run |
| REQ-004 | Same as above. | TC-006 | Provide a list containing only completed tasks. Verify that the result is an empty list. | Unit | Not Run |
| REQ-004 | Same as above. | TC-007 | Provide an empty list. Verify that the result is an empty list. | Unit | Not Run |
| REQ-005 | `average_priority` shall return the arithmetic mean of task priorities, or 0 for an empty list. | TC-008 | Provide tasks with priorities whose arithmetic mean is non-integer. Verify that the result equals the sum of their priorities divided by the number of tasks. Use values within the confirmed priority domain. | Unit | Not Run |
| REQ-005 | Same as above. | TC-009 | Provide one task. Verify that the returned average equals that task’s priority. | Unit | Not Run |
| REQ-005 | Same as above. | TC-010 | Provide an empty list. Verify that the result is 0. | Unit | Not Run |
| REQ-006 | `find_task_by_title` shall return the first task with an exact title match, or `None` if none matches. | TC-011 | Provide a list containing one exact title match among nonmatching tasks. Verify that the matching task is returned. | Unit | Not Run |
| REQ-006 | Same as above. | TC-012 | Provide two tasks with identical titles but distinguishable IDs. Search for that title and verify that the first matching task in the list is returned. | Unit | Not Run |
| REQ-006 | Same as above. | TC-013 | Search for a title when the list contains only a longer title containing that search text. Verify that the function returns `None`, because a partial match is not an exact match. | Unit | Not Run |
| REQ-007 | `remove_task` shall remove the task with the requested ID and leave other tasks unchanged. | TC-014 | Request removal of an existing task from a list containing several tasks. Verify that the target task is removed and every other task retains its original data. | Unit | Not Run |
| REQ-008 | `save_tasks` shall write tasks so `load_tasks` can read them back. | TC-015 | Save a populated task list to a temporary file, then load it. Verify that the loaded list equals the supplied list, including all task field values. | Integration | Not Run |
| REQ-008 | Same as above. | TC-016 | Save an empty task list to a temporary file, then load it. Verify that the result is an empty list. | Integration | Not Run |
| REQ-008 | `load_tasks` shall return an empty list when the data file does not exist. | TC-017 | Use a nonexistent file path within a temporary directory. Call `load_tasks` and verify that it returns an empty list. | Integration | Not Run |

Assumptions to confirm
- For TC-002, priority and tags can be supplied explicitly; their input format must be confirmed from the function interface.
- Input ordering for get_pending_tasks is a draft assumption. The tests above check membership without requiring a particular order.
- Case-sensitive title matching is a draft assumption. The title tests use identical capitalization and do not establish case-sensitivity as an approved requirement.
- Leaving the list unchanged when remove_task receives an absent ID is a draft assumption. It is not included as a required test outcome.
- File tests use isolated temporary files/directories. This is a test setup choice, not an application requirement.
Ambiguities and limitations
- REQ-001 does not define default priority/tags, valid priority values, or whether empty titles and invalid priorities must be rejected.
- Behaviour for duplicate task IDs is unspecified.
- Malformed-file handling is unspecified.
- The requirements remain student-derived and require TA review. The note about an existing implementation failure is not execution evidence for this matrix; all statuses remain Not Run.