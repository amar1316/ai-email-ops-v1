# email_sender.py

import base64
from email.mime.text import MIMEText


def send_email(service, to_email, subject, body_text):
    message = MIMEText(body_text)
    message["to"] = to_email
    message["subject"] = subject

    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()

    sent_message = service.users().messages().send(
        userId="me",
        body={"raw": raw}
    ).execute()

    return sent_message
