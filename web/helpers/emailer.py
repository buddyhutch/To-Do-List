from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from flask import current_app, flash

def send_todo_email(api_key, to_email, from_email, todos):
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
        sg = SendGridAPIClient(api_key)
        response = sg.send(message)
        flash(f'Email sent! Status code: {response.status_code}', 'info')
    except Exception as e:
        current_app.logger.error(f'Error sending email: {e}')
        flash('There was a problem sending your email. Please check your API key and try again.', 'danger')
