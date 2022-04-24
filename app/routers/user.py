from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, database, oauth2
from ..repository import user

router = APIRouter(
    prefix = '/user',
    tags = ['Users'],
    dependencies=[Depends(oauth2.get_current_user)]
)

@router.post('', response_model=schemas.ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.User, db: Session = Depends(database.get_db)) :
    return user.create(request, db)

@router.get('', response_model=List[schemas.ShowUser])
def get_users(db: Session = Depends(database.get_db)) :
    return user.getall(db)

@router.get('/{user_id}', response_model=schemas.ShowUser)
def get_user(user_id: str, db: Session = Depends(database.get_db)) :
    return user.get(user_id, db)