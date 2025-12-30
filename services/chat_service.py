from core.azure_client import client
from core.config import AZURE_OPENAI_DEPLOYMENT
from memory.session_store import (
    get_session,
    add_message,
    get_context,
    update_summary,
    MAX_MESSAGES
)
from services.tool_service import execute_tool
from services.summarization_service import summarize_messages

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "Perform mathematical calculations",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {"type": "string"}
                },
                "required": ["expression"]
            }
        }
    }
]


def process_chat(session_id: str, user_message: str) -> str:
    session = get_session(session_id)

    # 1️⃣ Save user message
    add_message(session_id, "user", user_message)

    summary, recent_messages = get_context(session_id)

    # 2️⃣ Summarize if needed
    if len(session["messages"]) > MAX_MESSAGES:
        old_messages = session["messages"][:-MAX_MESSAGES]

        new_summary = summarize_messages(
            old_messages=old_messages,
            existing_summary=summary
        )

        update_summary(session_id, new_summary)
        session["messages"] = recent_messages

    # 3️⃣ Build LLM context
    messages = [{"role": "system", "content": "You are a helpful assistant."}]

    if summary:
        messages.append({
            "role": "system",
            "content": f"Conversation summary: {summary}"
        })

    messages.extend(recent_messages)

    # 4️⃣ LLM call
    response = client.chat.completions.create(
        model=AZURE_OPENAI_DEPLOYMENT,
        messages=messages,
        tools=TOOLS,
        tool_choice="auto"
    )

    msg = response.choices[0].message

    # 5️⃣ Tool handling
    if msg.tool_calls:
        tool_call = msg.tool_calls[0]
        args = eval(tool_call.function.arguments)

        result = execute_tool(tool_call.function.name, args)

        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": str(result)
        })

        final = client.chat.completions.create(
            model=AZURE_OPENAI_DEPLOYMENT,
            messages=messages
        )

        assistant_message = final.choices[0].message.content
    else:
        assistant_message = msg.content

    # 6️⃣ Save assistant message
    add_message(session_id, "assistant", assistant_message)

    return assistant_message
