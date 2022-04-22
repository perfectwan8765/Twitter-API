from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from .. import schemas
from ..repository import celebrity

router = APIRouter(
    prefix = '/celerbrity',
    tags = ['Celerbirty']
)

@router.get('', response_model=List[schemas.Celerbrity])
def get_celebrites(db: Session = Depends(get_db)) :
    return celebrity.get_all(db)

@router.get('/{celerbrity_name}', response_model=schemas.Celerbrity)
def get_celerbrity(celerbrity_name: str, db: Session = Depends(get_db)) :
    return celebrity.get(celerbrity_name, db)