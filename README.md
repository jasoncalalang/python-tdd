# TDD Exercise

This repository contains the source code for my Python project, which follows best practices in testing with `pytest` and automatic test re-runs using `pytest-watch`.

## Prerequisites
 - Python (e.g., 3.8+)
 - Virtual environment (optional but recommended)

## Setting Up the Development Environment
1. Clone the repository
```bash
git clone <repository_url>
cd <repository_directory>
```
2. Set up a virtual environment (recommended)
```bash
python -m venv venv
```
  Activate the virtual environment:
  - Windows:
  ```bash
  .\venv\Scripts\activate
  ```
  - macOS and Linux:
  ```bash
  source /venv/bin/activate
  ```

3. Install the project dependencies:
```bash
pip install -r requirements.txt
```

## Running Tests
1. Using `pytest` directly:
```bash
pytest
```
2. Using pytest-watch for automatic test re-runs:
If you want to automatically re-run the tests whenever a source file changes:
```bash
ptw
```
Or, if you want the screen to clear before each test run:
```bash
ptw --runner "clear && pytest"
```
(Replace `clear` with `cls` on Windows.)
