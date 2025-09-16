import json
import os

todo_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'todo.json'))

def load_todos():
    if not os.path.exists(todo_file):
        return []
    try:
        with open(todo_file, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        from flask import current_app
        current_app.logger.error(f"Error loading todos: {e}")
        return []

def save_todos(todos):
    try:
        with open(todo_file, 'w') as f:
            json.dump(todos, f, indent=2)
    except IOError as e:
        from flask import current_app
        current_app.logger.error(f"Error saving todos: {e}")
