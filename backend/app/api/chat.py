from fastapi import APIRouter
from pydantic import BaseModel
from app.models import Chat
from app.database import SessionLocal

router = APIRouter()

class ChatRequest(BaseModel):
    user_id: int | None = None
    message: str

@router.post("/chat")
def chat(req: ChatRequest):
    db = SessionLocal()

    response = "AI response here"  # your LLM logic

    chat_item = Chat(user_id=req.user_id or 0, message=req.message, response=response)
    db.add(chat_item)
    db.commit()

    return {"response": response}
