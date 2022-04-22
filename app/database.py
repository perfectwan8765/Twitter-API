from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import db_confing

SQLALCHAMY_DATABASE_URL = db_confing.get_url()

engine = create_engine(SQLALCHAMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

def get_db() :
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()