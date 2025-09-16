import subprocess
import sys
import os

PYTHON = r"C:\Users\Buddy.Hutchinson\AppData\Local\Programs\Python\Python313\python.exe"
TODO_SCRIPT = "todo.py"

def run_cmd(args):
    result = subprocess.run([PYTHON, TODO_SCRIPT] + args, capture_output=True, text=True)
    return result.stdout.strip(), result.stderr.strip(), result.returncode

def test_add_empty_task():
    out, err, code = run_cmd(["add", ""])
    print("Test Add Empty Task:", out)
    assert code == 0
    # Optionally check for empty task handling in output

def test_done_nonexistent_task():
    out, err, code = run_cmd(["done", "999"])
    print("Test Done Nonexistent Task:", out)
    assert "Invalid task number" in out
    assert code == 0

def test_send_email_invalid_key():
    out, err, code = run_cmd(["email", "recipient@example.com", "sender@example.com", "INVALID_KEY"])
    print("Test Send Email Invalid Key:", out)
    assert "Error sending email" in out
    assert code == 0

if __name__ == "__main__":
    test_add_empty_task()
    test_done_nonexistent_task()
    test_send_email_invalid_key()
    print("Edge-case tests completed.")

import subprocess
import sys
import os

PYTHON = r"C:\Users\Buddy.Hutchinson\AppData\Local\Programs\Python\Python313\python.exe"
TODO_SCRIPT = "todo.py"

def run_cmd(args):
    result = subprocess.run([PYTHON, TODO_SCRIPT] + args, capture_output=True, text=True)
    return result.stdout.strip(), result.stderr.strip(), result.returncode

def test_add_empty_task():
    out, err, code = run_cmd(["add", ""])
    print("Test Add Empty Task:", out)
    assert code == 0
    # Optionally check for empty task handling in output

def test_done_nonexistent_task():
    out, err, code = run_cmd(["done", "999"])
    print("Test Done Nonexistent Task:", out)
    assert "Invalid task number" in out
    assert code == 0

def test_send_email_invalid_key():
    out, err, code = run_cmd(["email", "recipient@example.com", "sender@example.com", "INVALID_KEY"])
    print("Test Send Email Invalid Key:", out)
    assert "Error sending email" in out
    assert code == 0

if __name__ == "__main__":
    test_add_empty_task()
    test_done_nonexistent_task()
    test_send_email_invalid_key()
    print("Edge-case tests completed.")
