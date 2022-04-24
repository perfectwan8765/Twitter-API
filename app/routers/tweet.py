from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import date
from ..database import get_db
from .. import schemas, oauth2
from ..repository import tweet

router = APIRouter(
    prefix = '/tweet',
    tags = ['Tweet'],
    dependencies=[Depends(oauth2.get_current_user)]
)

@router.get('', response_model=List[schemas.Celerbrity_Tweet])
def get_tweets(db: Session = Depends(get_db)) :
    return tweet.get_all(db)

@router.get('/{celerbrity_name}', response_model=List[schemas.Celerbrity_Tweet])
def get_tweet_celerbrity(celerbrity_name: str, start_date: Optional[date] = None, end_date: Optional[date] = None, db: Session = Depends(get_db)) :
    return tweet.get(celerbrity_name, start_date, end_date, db)