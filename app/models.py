from .database import Base
from sqlalchemy import Column, Integer, String, DateTime

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