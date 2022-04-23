from fastapi import FastAPI
from app.routers import celerbrity, tweet, user, authentication
from app import models, database

app = FastAPI()

models.Base.metadata.create_all(database.engine)

app.include_router(celerbrity.router)
app.include_router(tweet.router)
app.include_router(user.router)
app.include_router(authentication.router)