# AI-Generated RTM Comparison

Complete after asking an AI assistant to draft a traceability matrix from the same `requirements.md`.

| Requirement ID | Student matrix coverage | AI matrix coverage | Difference / issue | Correct action and reason |
|---|---|---|---|---|

## Short discussion

Write your own comparison. Check that each requirement has a test, test IDs are unique, assumptions are visible, and no unsupported behaviour was invented.

The fresh AI matrix covered all eight requirements and suggested 17 test cases. The matrix I worked through had 11 test cases. Two useful additions were checking an average that includes a decimal, such as 1.5, and checking a list where every task is already completed. These test situations were missing from our original set. However, the fresh AI matrix did not include checking what happens when someone tries to remove a task using an ID that does not exist. Our TC-409 covered that situation.

The fresh AI matrix labelled the file-saving and loading tests as integration tests. This made sense because these tests check how the application works with actual files on disk. The original matrix labelled them as unit tests, so that classification needed correcting. Having 17 suggested tests does not automatically make the AI matrix better. Those tests were marked “Not Run”, while I ran our 11 tests and confirmed that they all passed after the two defects were fixed.

For an audit, I would trust the reviewed matrix more because it links to tests that were actually run, saved results, and records of the defects and their fixes. The fresh AI matrix is still useful because it suggests more situations to test. Both matrices use draft requirements, so their assumptions still need confirmation. AI helped prepare the original requirements, matrix and test code, which I then worked through and ran. This comparison is therefore between an AI-assisted matrix reviewed by me and a fresh AI-generated draft.
