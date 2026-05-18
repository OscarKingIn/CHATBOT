from fastapi import APIRouter
from pydantic import BaseModel
from app.services.llm import generate_response
from app.services.memory import save_message, get_history
from app.rag.retriever import get_context

router = APIRouter()

class ChatRequest(BaseModel):
    user_id: str
    message: str

@router.post("/chat")
def chat(req: ChatRequest):
    history = get_history(req.user_id)
    context = get_context(req.message)

    response = generate_response(req.message, history, context)

    save_message(req.user_id, req.message, response)

    return {"response": response}