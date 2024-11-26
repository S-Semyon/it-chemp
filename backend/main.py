from typing import Union
from models import User
from db import init_db
from fastapi import FastAPI

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    print("INITIALISING DATABASE")
    await init_db()

@app.post("/create/user")
async def create_user():
    await User.create(
        name = "John",
        last_name = "Doe",
        email = "johndoe@gmail.com",
        password = "password"
    )

@app.post("/token/user")
async def token_user():
    return {"token": "token"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}