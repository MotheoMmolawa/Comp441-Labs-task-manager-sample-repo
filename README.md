# COMP 441 Labs: Task Manager

Shared working repository for COMP 441 labs 4–6, using the supplied Python Task Manager sample.

## Project setup (Windows PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pytest -v
```

Run the sample application with:

```powershell
.\.venv\Scripts\python.exe -m app.cli
```

## Lab folders

- `lab-4-solutions/` contains draft student-derived requirements and templates for traceability, test planning, defect tracking, and the AI comparison.
- `lab-5-solutions/` is reserved for the small Task Manager web app and its UI automation work.
- `lab-6-solutions/` documents the selected source functions and provides places for AI-generated, independently written, and combined tests and coverage results.

The Lab 4 requirements are derived from the sample code and its docstrings because no separate requirements document was supplied. Review the assumptions with the TA before treating them as approved requirements. Record actual test and coverage results after running them; do not fill in expected results as if measured.
