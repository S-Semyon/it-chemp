from typing import Union
from models import User
from db import init_db
from fastapi import FastAPI
from pydantic import BaseModel
from security import text_to_hash, generatetoken
import asyncio

class RegisterUser(BaseModel):
    username: str
    email: str
    password: str

class LoginUser (BaseModel):
    username: str
    password: str

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    print("INITIALISING DATABASE")
    await init_db()

@app.post("/register")
async def register(user: RegisterUser):
    
    if await User.get_or_none(username= user.username) is None and await User.get_or_none(email= user.email) is None:
        
        await User.create(username=user.name, email=user.mail, password=text_to_hash(user.password))

        return {"status": 200, "token": asyncio.run(generatetoken(user.name))}
    else:
        return {"status": 425}
    
@app.post("/login")
async def login(user: LoginUser):
    usr = await User.get_or_none(username= user.username)
    if  usr is not None:
        if text_to_hash(user.password) == usr.password:

            return {"status": 200, "token": asyncio.run(generatetoken(user.name))}
        else:
            return {"status": 401}
    else:
        return {"status": 401}