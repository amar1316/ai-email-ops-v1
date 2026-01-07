# AI Email Operations Assistant (Version 1)

🚀 Human-in-the-loop AI system for reading, classifying, and replying to emails.

## 🔹 Features
- Reads unread Gmail emails
- Classifies email intent (Sales / Support / Spam / Other)
- Generates AI draft replies
- Human approval required before sending
- Safe & controllable automation

## 🔹 Tech Stack
- Python
- OpenAI API
- Gmail API
- OAuth 2.0

## 🔹 Workflow
1. Fetch unread emails
2. Classify intent using AI
3. Generate reply draft
4. Ask human approval (y/n)
5. Send email only if approved

## 🔹 Setup Instructions

### 1️⃣ Clone Repository
```bash
git clone https://github.com/yourusername/ai-email-ops-v1.git
cd ai-email-ops-v1

This project requires a Google Sheets service account JSON file
(sheets_credentials.json) which should NOT be committed.