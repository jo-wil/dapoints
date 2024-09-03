import logging

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from .database import (
    run_migrations
)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

logger = logging.getLogger("uvicorn.error")

run_migrations()

class Login(BaseModel):
    email: str
    password: str


@app.post("/login")
def login(login: Login):
    if login.email == "joey.wilson.a@gmail.com":
        return { "name": "Joey", "email": "joey.wilson.a@gmail.com", "jwt": "token" }
    else:
        raise HTTPException(status_code=400, detail="")
