"""
Email Reader Module
Handles Gmail authentication, email reading,
AI classification, human approval, sending, and logging
"""

import os
import json
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from config import SCOPES
from ai_classifier import classify_email
from ai_reply import draft_reply
from email_sender import send_email
from sheets_logger import log_to_sheet


TOKEN_FILE = "token.json"
CREDENTIALS_FILE = "credentials.json"


# -------------------------------------------------
# GMAIL AUTHENTICATION
# -------------------------------------------------
import os
import pickle
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from config import SCOPES


def get_gmail_service():
    creds = None

    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)

        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    service = build("gmail", "v1", credentials=creds)
    return service



# -------------------------------------------------
# MAIN EMAIL PROCESSING LOGIC (V1 – HUMAN APPROVAL)
# -------------------------------------------------
def read_latest_emails(max_results=5):
    service = get_gmail_service()

    results = service.users().messages().list(
        userId="me",
        maxResults=max_results
    ).execute()

    messages = results.get("messages", [])

    if not messages:
        print("📭 No unread emails found.")
        return

    for msg in messages:
        try:
            msg_data = service.users().messages().get(
                userId="me",
                id=msg["id"],
                format="metadata"
            ).execute()

            headers = msg_data["payload"]["headers"]
            subject = "No Subject"
            sender = "Unknown"

            for h in headers:
                if h["name"] == "Subject":
                    subject = h["value"]
                elif h["name"] == "From":
                    sender = h["value"]

            # AI classification
            category = classify_email(sender, subject)

            # AI reply drafting
            reply = draft_reply(sender, subject, category)

            print("\n" + "-" * 70)
            print("From     :", sender)
            print("Subject  :", subject)
            print("Category :", category)
            print("\n🤖 AI Draft Reply:\n")
            print(reply)

            choice = input("\nSend this reply? (y/n): ").strip().lower()

            if choice == "y":
                send_email(
                    service=service,
                    to_email=sender,
                    subject=f"Re: {subject}",
                    body_text=reply
                )
                status = "Sent"
                print("📤 Email sent")
            else:
                status = "Skipped"
                print("❌ Email skipped")

            log_to_sheet(
                sender=sender,
                subject=subject,
                category=category,
                reply=reply,
                status=status
            )

        except Exception as e:
            print("❌ Failed to process one email")
            print("Reason:", e)
