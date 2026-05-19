import os
from jose import jwt

SECRET = os.getenv("JWT_SECRET")

if not SECRET:
    raise ValueError("JWT_SECRET is not set")

def create_token(user_id: str):
    return jwt.encode({"sub": user_id}, SECRET, algorithm="HS256")

def verify_token(token: str):
    return jwt.decode(token, SECRET, algorithms=["HS256"])