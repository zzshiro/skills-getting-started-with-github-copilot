# Copilot instructions

## Project overview

This repository contains a FastAPI application for viewing and signing up for Mergington High School activities.

- `src/app.py` defines the API and in-memory activity data.
- `src/static/` contains the HTML, CSS, and JavaScript frontend.
- `.github/steps/` and `.github/workflows/` support the repository's GitHub Copilot learning exercises; avoid changing them unless the task is about those exercises.
- `requirements.txt` lists the Python dependencies.

## Development and validation

- Use Python 3.12 or newer. Install dependencies with `pip install -r requirements.txt`.
- Run the app from the repository root with `python -m uvicorn src.app:app --reload --host 0.0.0.0 --port 8000`.
- There is no configured automated test suite, linter, or build step. For API changes, run the app and check `GET /activities` and the affected signup scenarios, including relevant error cases. For frontend changes, load `/` and verify the affected interaction in a browser.
- Activity data is held in memory and resets whenever the server restarts.

## Change guidance

- Keep changes focused on the requested task and follow the existing patterns in the relevant source files.
- Avoid adding dependencies unless they are necessary.
- Update documentation when behavior or developer instructions change.
