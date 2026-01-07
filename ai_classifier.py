from openai import OpenAI

client = OpenAI()

MODEL_NAME = "gpt-4o-mini"


def classify_email(sender, subject):
    prompt = f"""
You are an email classification assistant.

Classify the following email into ONE category only:
- Job
- Sales
- Support
- Spam
- Other

Email details:
From: {sender}
Subject: {subject}

Return only the category name.
"""

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        category = response.choices[0].message.content.strip()
        return category.capitalize()

    except Exception as e:
        print("⚠️ Classification failed, defaulting to 'Other'")
        return "Other"
