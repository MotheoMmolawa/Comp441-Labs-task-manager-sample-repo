# Lab 6: AI-Generated Test Cases & Coverage Delta

## Selected functions

These functions in the supplied sample have no tests in the original suite:

- `app.tasks.find_task_by_title`
- `app.tasks.remove_task`
- `app.storage.format_task_report`

Confirm these choices by reviewing the current tests before beginning. Keep AI-generated tests and independently written tests in separate files. The Lab 6 manual requires the manual tests to be written without AI assistance.

## Planned structure

- `tests/ai_generated/`: reviewed tests drafted by the assistant.
- `tests/manual/`: tests independently designed and written by the student.
- `tests/combined/`: merged suite, avoiding duplicate collection where needed.
- `coverage/`: AI-only, manual-only, and combined reports.
- `comparison.md`: coverage percentages, assertion counts, assertion-strength examples, and the student's verdict.

Run and record each suite separately. Coverage measures executed code; review assertions to judge whether tests check correct behaviour.
