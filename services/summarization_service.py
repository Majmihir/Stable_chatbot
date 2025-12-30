from core.azure_client import client
from core.config import AZURE_OPENAI_DEPLOYMENT


def summarize_messages(old_messages: list, existing_summary: str) -> str:
    conversation = "\n".join(
        f"{m['role']}: {m['content']}" for m in old_messages
    )

    messages = [
        {
            "role": "system",
            "content": (
                "You are a memory summarizer. "
                "Create a concise factual summary. "
                "Preserve user goals, preferences, and important facts."
            )
        },
        {
            "role": "user",
            "content": f"""
Existing summary:
{existing_summary}

New conversation:
{conversation}

Update the summary:
"""
        }
    ]

    response = client.chat.completions.create(
        model=AZURE_OPENAI_DEPLOYMENT,
        messages=messages
    )

    return response.choices[0].message.content.strip()
