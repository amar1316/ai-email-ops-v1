from openai import OpenAI

client = OpenAI()

MODEL_NAME = "gpt-4o-mini"


def draft_reply(sender, subject, category):
    prompt = f"""
You are a professional email assistant.

Write a short, polite, and professional email reply.

Email details:
From: {sender}
Subject: {subject}
Category: {category}

Rules:
- Be clear and respectful
- Do NOT invent facts
- Keep it under 5 lines
- Do NOT sign with a name
"""

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return "Thank you for your email. We will review it and get back to you shortly."
