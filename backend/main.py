from fastapi import FastAPI
from app.api.chat import router as chat_router
from app.database import engine, Base
from app.auth import router as auth_router

app = FastAPI(title="CHATBOT AI")

app.include_router(auth_router, prefix="/auth")
app.include_router(chat_router, prefix="/api")

Base.metadata.create_all(bind=engine)
