from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()

class UserNotFoundException(Exception):
    def __init__(self, name:str):
        self.name  = name

@app.exception_handler(UserNotFoundException)
def user_not_found_exception_handler(request: Request, exc: UserNotFoundException):
    return JSONResponse(
        status_code=404,
        content={"message": f"User '{exc.name}' not found."},
    )

@app.get("/user/{name}")
def get_user(name: str):
    if name != "Casper":
        raise UserNotFoundException(name)
    return {"name": name, "message": "User found!"}