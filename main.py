from fastapi import FastAPI
from .app.routers import celerbrity, tweet

app = FastAPI()

app.include_router(celerbrity.router)
app.include_router(tweet.router)