from fastapi import APIRouter
from models.chat_schema import ChatRequest, ChatResponse
from services.chat_service import process_chat

router = APIRouter(prefix="/chat", tags=["Chat"])

@router.post("", response_model=ChatResponse)
def chat(req: ChatRequest):
    response = process_chat(req.session_id, req.message)
    return ChatResponse(
        session_id=req.session_id,
        response=response
    )
