

"""
Entry point for AI Email Operations Assistant (Version 1)
Human-in-the-loop email processing
"""

from email_reader import read_latest_emails


def main():
    print("📬 AI Email Operations Assistant – Version 1")
    print("🔍 Reading latest emails...\n")

    try:
        read_latest_emails(max_results=3)
    except Exception as e:
        print("❌ Error occurred while processing emails")
        print(f"Details: {e}")


if __name__ == "__main__":
    main()
