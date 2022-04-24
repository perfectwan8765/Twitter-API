from typing import Optional
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

class User(BaseModel) :
    name : str
    email : str
    password : str

class ShowUser(BaseModel) :
    user_id : str
    name : str
    email : str

    class Config:
        orm_mode = True

class Login(BaseModel) :
    username : str
    password : str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None