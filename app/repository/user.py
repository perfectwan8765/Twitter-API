import email
from http.client import HTTPException
from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, models
from ..hashing import Hash


def create(request: schemas.User, db: Session) :
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def getall(db: Session) :
    return db.query(models.User).all()

def get(user_id: str, db: Session) :
    user = db.query(models.User).filter(models.User.user_id == user_id).first()

    if not user :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with the id {user_id} is not avaliable")
    
    return user