from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import schemas, database, models, token
from ..hashing import Hash

router = APIRouter(
    tags=["Authentication"]
)

@router.post("/login", response_model=schemas.Token)
def login(request: OAuth2PasswordRequestForm=Depends(), db: Session=Depends(database.get_db)) :
    user = db.query(models.User).filter(models.User.email == request.username).first()

    if not user :
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials", headers={"WWW-Authenticate": "Bearer"})

    if not Hash.verify(request.password, user.password) :
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect Password", headers={"WWW-Authenticate": "Bearer"})

    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}