# Lab 5: Test Automation Framework & Self-Healing Locators

## Selected application

A small Task Manager web interface is planned for this lab so the UI tests use the same task-management domain as the Python sample. Keep the web demonstration inside this folder; do not replace the supplied Python sample.

## Planned structure

- `web-app/`: small browser-based Task Manager.
- `tests/`: Selenium tests using a Page Object and data loaded from JSON.
- `test-data.json`: values for five UI scenarios.
- `reports/`: baseline, locator-drift, and healing evidence.
- `healenium/`: Docker configuration and setup notes, added when the current official self-hosted instructions are checked.

Complete the baseline suite first. Then change one locator, run with healing disabled, and run with the Healenium Selenium proxy enabled. Record actual results and inspect the healing decision. Do not describe a test as self-healed unless the report or logs confirm it.
