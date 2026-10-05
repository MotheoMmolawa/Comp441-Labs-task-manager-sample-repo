# Lab 4: Requirements Traceability & Test Management

## Source of requirements

The supplied repository contains no separate requirements document. The draft requirements in `requirements.md` are student-derived from the Task Manager functions and their docstrings. They include explicit assumptions for behaviour the code does not fully specify. Confirm these assumptions with the TA.

## Deliverables

- `requirements.md`: eight draft functional requirements.
- `traceability-matrix.csv`: requirement-to-test mapping. Update test status after execution.
- `mini-test-plan.md`: scope and entry/exit criteria for REQ-004.
- `defect-log.csv`: log two actual defects and record each real lifecycle transition, including owner, date, severity, priority, and evidence.
- `ai-comparison.md`: compare the AI-generated matrix with the reviewed student matrix. Complete after generating the AI version.

Do not claim defects are fixed or closed until the fix has been run and verified.

## Results

- Before fixes: 9 Lab 4 tests passed and 2 failed.
- After fixes: all 11 Lab 4 tests passed.
- Regression check: all 6 original tests passed.
- DEF-001 and DEF-002 completed the lifecycle from New to Closed.
- The fresh AI matrix proposed 17 test cases; these were not executed.
- The comparison and audit reflection are in ai-comparison.md.

## AI assistance

AI helped draft the requirements, traceability matrix, test cases,
test code, fixes and comparison text. I ran the tests and recorded
the results. The requirements are student-derived rather than
an official specification supplied by the TA.
