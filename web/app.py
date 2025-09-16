from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os
from colorama import Fore, Style
from helpers.storage import load_todos, save_todos
from helpers.emailer import send_todo_email

app = Flask(__name__)
app.secret_key = 'your_secret_key'
## Storage and email helpers are now imported from helpers/

@app.route('/')
def index():
    todos = load_todos()
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task', '').strip()
    if task:
        todos = load_todos()
        todos.append({'task': task, 'done': False})
        save_todos(todos)
        flash('Task added!', 'success')
    else:
        flash('Task cannot be empty.', 'danger')
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>')
def complete(task_id):
    todos = load_todos()
    if 0 < task_id <= len(todos):
        todos[task_id-1]['done'] = True
        save_todos(todos)
        flash('Task completed!', 'success')
    else:
        flash('Invalid task number.', 'danger')
    return redirect(url_for('index'))

@app.route('/email', methods=['POST'])
def email():
    api_key = request.form.get('api_key')
    to_email = request.form.get('to_email', 'buddy.hutchinson@asiweb.com')
    from_email = request.form.get('from_email', 'buddy.hutchinson@asiweb.com')
    todos = load_todos()
    send_todo_email(api_key, to_email, from_email, todos)
    return redirect(url_for('index'))

# Delete task route
@app.route('/delete/<int:task_id>')
def delete(task_id):
    todos = load_todos()
    if 0 < task_id <= len(todos):
        removed = todos.pop(task_id-1)
        save_todos(todos)
        flash(f"Deleted task: {removed['task']}", 'warning')
    else:
        flash('Invalid task number.', 'danger')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
