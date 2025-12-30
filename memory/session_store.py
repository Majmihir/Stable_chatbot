import json
import redis
from datetime import datetime

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

SESSION_TTL = 3600
MAX_MESSAGES = 6


def get_session(session_id: str):
    data = r.get(session_id)
    if not data:
        session = {
            "messages": [],
            "summary": "",
            "created_at": datetime.utcnow().isoformat()
        }
        r.setex(session_id, SESSION_TTL, json.dumps(session))
        return session
    return json.loads(data)


def save_session(session_id: str, session: dict):
    r.setex(session_id, SESSION_TTL, json.dumps(session))


def add_message(session_id: str, role: str, content: str):
    session = get_session(session_id)
    session["messages"].append({"role": role, "content": content})
    save_session(session_id, session)


def get_context(session_id: str):
    session = get_session(session_id)
    summary = session.get("summary", "")
    messages = session.get("messages", [])
    recent_messages = messages[-MAX_MESSAGES:]
    return summary, recent_messages


def update_summary(session_id: str, new_summary: str):
    session = get_session(session_id)
    session["summary"] = new_summary
    save_session(session_id, session)
