from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
users = []

class User(BaseModel):
    name: str
    age: int

@app.post("/users")
def create_user(user: User):
    users.append(user)
    return {"message": "User created successfully", "user data": user}

@app.get("/users")
def get_users():
    return {"users": users}

@app.put("/users/{user_id}")
def update_user(user_id: int, user: User, notify:bool = False):
    if user_id < len(users):
        users[user_id] = user
        return {"message": "User updated successfully", "notify": notify, "user data": user}
    return {"error": "User not found"}