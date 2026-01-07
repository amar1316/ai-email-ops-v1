from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from datetime import datetime
from config import SPREADSHEET_ID


SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]




def log_to_sheet(sender, subject, category, reply, status):
    creds = Credentials.from_service_account_file(
        "sheets_credentials.json",
        scopes=SCOPES
    )

    service = build("sheets", "v4", credentials=creds)

    values = [[
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        sender,
        subject,
        category,
        reply,
        status
    ]]

    body = {"values": values}

    # ✅ FINAL FIX: NO SHEET NAME
    service.spreadsheets().values().append(
        spreadsheetId=SPREADSHEET_ID,
        range="A:F",               # 👈 THIS IS THE KEY
        valueInputOption="RAW",
        body=body
    ).execute()
