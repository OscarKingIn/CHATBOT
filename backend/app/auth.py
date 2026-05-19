from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import User
from jose import jwt
import os

router = APIRouter()

SECRET = os.getenv("JWT_SECRET")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register")
def register(email: str, password: str, db: Session = Depends(get_db)):
    user = User(email=email, password=password)
    db.add(user)
    db.commit()
    return {"message": "User created"}


@router.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()

    if not user or user.password != password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = jwt.encode({"sub": user.email}, SECRET, algorithm="HS256")

    return {"access_token": token}