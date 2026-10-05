# Mini Test Plan: REQ-004 Pending Tasks

## Scope

Verify that `get_pending_tasks` returns all tasks with `done == False`, preserves their input order, and does not include completed tasks. Include cases where the first task is pending, completed, or the only task. This is unit-level testing of the function in isolation.

## Entry criteria

- The Task Manager source and Python test environment are available.
- Test data can be constructed as task dictionaries with `id` and `done` fields.
- Expected results are agreed against the draft requirement.

## Exit criteria

- All planned REQ-004 test cases have been run and their outcomes recorded.
- Any mismatch is logged as a defect with reproducible input and actual result.
- The status in the traceability matrix reflects the execution evidence.
