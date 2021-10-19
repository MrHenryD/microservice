from fastapi import FastAPI

import api.v1.api as v1

app = FastAPI()

app.include_router(v1.api_router, prefix="/api/v1")

####
from typing import Optional

from pydantic import BaseModel

from fastapi import FastAPI, HTTPException, Form, Query

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


class User(BaseModel):
    name: str = Query(
        ..., title="Name", description="Name of User", min_length=3, max_length=20
    )
    age: int = Query(
        ...,
        title="Age",
        description="Age of User",
    )


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.post("/items/")
async def create_item(item: Item):
    return item


@app.post("/users/")
async def create_user(user: User):
    return user


@app.post("/login/")
async def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username}


@app.get("/errors")
async def error_message():
    raise HTTPException(status_code=404, detail="This is an error")
