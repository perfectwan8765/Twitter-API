from .database import Base
from sqlalchemy import Column, Integer, String, DateTime
from uuid import uuid4

class Celerbrity(Base) :
    __tablename__ = 'celerbrity'
    
    id = Column(Integer, primary_key=True)
    celerbrity = Column(String)
    followers_count = Column(Integer)
    url = Column(String)
    check_date = Column(DateTime)

class Celerbrity_Tweet(Base) :
    __tablename__ = 'celerbrity_tweet'
    
    twit_id = Column(Integer, primary_key=True)
    celerbrity = Column(String)
    tweet_url = Column(String)
    retweet_count = Column(Integer)
    favorite_count = Column(Integer)
    created_at = Column(DateTime)

class User(Base) :
    __tablename__ = 'user'

    user_id = Column(String, primary_key=True, default=uuid4().hex)
    name = Column(String)
    email = Column(String)
    password = Column(String)