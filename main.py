from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Address(BaseModel):
    city: str
    state: str
    country: str

class User(BaseModel):
    name: str
    age: int
    address: Address

@app.post("/new user")
def new_user(user: User):
    return{
        "message": "User created successfully",
        "data": user
         }
