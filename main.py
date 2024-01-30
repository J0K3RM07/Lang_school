from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any
app = FastAPI()

class Name(BaseModel):
    name: Any


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/hello/")
async def say_hello(name: Name):
    return {"message": f"Hello {name.name}!"}

