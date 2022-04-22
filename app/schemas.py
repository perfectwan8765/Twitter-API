from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

class Celerbrity(BaseModel) :
    celerbrity : str
    followers_count : int
    url : str
    check_date : datetime

    class Config:
        orm_mode = True

class Celerbrity_Tweet(BaseModel) :
    celerbrity: str
    tweet_url: str
    favorite_count: int  
    retweet_count: int
    created_at: datetime

    class Config:
        orm_mode = True