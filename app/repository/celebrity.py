from fastapi import status, HTTPException
from .. import models


def get_all(db) :
    celebrites = db.query(models.Celerbrity).all()
    return celebrites

def get(celerbrity_name, db) :
    celerbrity = db.query(models.Celerbrity).where(models.Celerbrity.celerbrity == celerbrity_name).first()

    if not celerbrity :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'{celerbrity_name} not exists')

    return celerbrity