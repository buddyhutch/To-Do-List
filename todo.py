"""
Simple CLI To-Do List App: Add, list, and complete tasks, saved in a JSON file.
Features: Colored output, SendGrid email support.
"""
import json
import sys
import os
from colorama import init, Fore, Style
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

TODO_FILE = 'todo.json'

def load_todos():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, 'r') as f:
        return json.load(f)

def save_todos(todos):
    with open(TODO_FILE, 'w') as f:
        json.dump(todos, f, indent=2)

def add_task(task):
    todos = load_todos()
    todos.append({'task': task, 'done': False})
    save_todos(todos)
def list_tasks():
    """List all tasks with colored status."""
    init(autoreset=True)
    todos = load_todos()
    if not todos:
        print(Fore.YELLOW + "No tasks found.")
        return
    for i, todo in enumerate(todos, 1):
        if todo['done']:
            status = Fore.GREEN + '✔' + Style.RESET_ALL
            task_text = Fore.GREEN + todo['task'] + Style.RESET_ALL
        else:
            status = Fore.RED + '✗' + Style.RESET_ALL
            task_text = Fore.RED + todo['task'] + Style.RESET_ALL
        print(f"{i}. [{status}] {task_text}")
        status = '✔' if todo['done'] else '✗'
        print(f"{i}. [{status}] {todo['task']}")

def complete_task(index):
    todos = load_todos()
    if 0 < index <= len(todos):
        todos[index-1]['done'] = True
        save_todos(todos)
        print(f"Completed: {todos[index-1]['task']}")
    else:
        print("Invalid task number.")

def email_tasks(sendgrid_api_key, to_email, from_email):
    """Send the to-do list via SendGrid email."""
    todos = load_todos()
    if not todos:
        body = "No tasks found."
    else:
        body = "\n".join([
            f"{i+1}. [{'✔' if t['done'] else '✗'}] {t['task']}" for i, t in enumerate(todos)
        ])
    message = Mail(
        from_email=from_email,
        to_emails=to_email,
        subject='Your To-Do List',
        plain_text_content=body
    )
    try:
        sg = SendGridAPIClient(sendgrid_api_key)
        response = sg.send(message)
        print(Fore.CYAN + f"Email sent! Status code: {response.status_code}")
    except Exception as e:
        print(Fore.RED + f"Error sending email: {e}")
    """Send the to-do list via SendGrid email."""
    todos = load_todos()
    if not todos:
        body = "No tasks found."
    else:
        body = "\n".join([
            f"{i+1}. [{'✔' if t['done'] else '✗'}] {t['task']}" for i, t in enumerate(todos)
        ])
    message = Mail(
        from_email=from_email,
        to_emails=to_email,
        subject='Your To-Do List',
        plain_text_content=body
    )
    try:
        sg = SendGridAPIClient(sendgrid_api_key)
        response = sg.send(message)
        print(Fore.CYAN + f"Email sent! Status code: {response.status_code}")
    except Exception as e:
        print(Fore.RED + f"Error sending email: {e}")
        print("Invalid task number.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python todo.py [add|list|done] [task|number]")
        return
    cmd = sys.argv[1]
    if cmd == 'add' and len(sys.argv) > 2:
        add_task(' '.join(sys.argv[2:]))
    elif cmd == 'list':
        list_tasks()
    elif cmd == 'done' and len(sys.argv) > 2:
        try:
            idx = int(sys.argv[2])
            complete_task(idx)
        except ValueError:
            print("Please provide a valid task number.")
    elif cmd == 'email' and (len(sys.argv) == 5 or len(sys.argv) == 2):
        # If arguments provided, use them; else use default email
        if len(sys.argv) == 5:
            to_email = sys.argv[2]
            from_email = sys.argv[3]
            api_key = sys.argv[4]
        else:
            to_email = "buddy.hutchinson@asiweb.com"
            from_email = "buddy.hutchinson@asiweb.com"
            api_key = sys.argv[2]
        email_tasks(api_key, to_email, from_email)
    else:
        print("Unknown command or missing arguments.")

if __name__ == '__main__':
    main()
