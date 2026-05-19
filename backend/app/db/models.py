from sqlalchemy import Column, String, Text
from app.db.session import Base

class Chat(Base):
    __tablename__ = "chats"

    id = Column(String, primary_key=True)
    user_id = Column(String)
    message = Column(Text)
    response = Column(Text)