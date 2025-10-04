from fastapi import FastAPI
from http import HTTPStatus
from fast_zero.schemas import Message, UserPublic, UserSchema, UserDB

app = FastAPI(title="API Braba")

database = []


@app.get("/", status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {"message": "Olá Mundo!"}


@app.post("/users/", response_model=UserPublic, status_code=HTTPStatus.CREATED)
def create_user(user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)

    database.append(user_with_id)

    return user_with_id
