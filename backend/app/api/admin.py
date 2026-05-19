from fastapi import APIRouter
from app.db.session import SessionLocal
from app.db.models import Chat

router = APIRouter()

@router.get("/chats")
def get_chats():
    db = SessionLocal()
    return db.query(Chat).all()