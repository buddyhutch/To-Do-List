# CLI & Web To-Do List App

A simple Python to-do list application with both CLI and Flask web interfaces. Tasks are saved in a JSON file. Features include colored status, SendGrid email integration, and edge-case test automation.

## Features
- Add, list, and complete tasks (CLI & Web)
- Colored status for tasks
- SendGrid email integration
- Robust error handling
- Automated edge-case tests

## CLI Usage
```
python todo.py add "task description"
python todo.py list
python todo.py done <task_number>
python todo.py email <SENDGRID_API_KEY>
```

## Web App Usage
1. Install dependencies:
   ```
   pip install flask colorama sendgrid
   ```
2. Run the web app:
   ```
   python web/app.py
   ```
3. Open [http://localhost:5000](http://localhost:5000) in your browser.

## Email Feature
- Default sender/recipient: buddy.hutchinson@asiweb.com
- Requires a valid SendGrid API key

## Testing
Run edge-case tests:
```
python test_edge_cases.py
```

## File Structure
- `todo.py` — CLI app
- `web/app.py` — Flask web app
- `web/helpers/` — Storage & email helpers
- `web/templates/index.html` — Web UI
- `todo.json` — Task storage
- `test_edge_cases.py` — Automated tests

---
GitHub Copilot
