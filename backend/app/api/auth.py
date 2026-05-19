from fastapi import APIRouter
from app.core.security import create_token

router = APIRouter()

@router.post("/login")
def login(username: str):
    token = create_token(username)
    return {"access_token": token}

from fastapi import Depends
from app.core.security import verify_token

def get_user(token: str):
    return verify_token(token)["sub"]