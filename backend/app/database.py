import os
import time
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL is None:
    raise RuntimeError("DATABASE_URL environment variable is required")

retry_attempts = 10
retry_delay = 3
for attempt in range(1, retry_attempts + 1):
    try:
        engine = create_engine(DATABASE_URL, future=True, pool_pre_ping=True)
        with engine.connect() as conn:
            pass
        break
    except OperationalError:
        if attempt == retry_attempts:
            raise
        time.sleep(retry_delay)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()