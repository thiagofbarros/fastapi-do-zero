from fastapi import FastAPI
from http import HTTPStatus
from fast_zero.schemas import Message, UserPublic, UserSchema

app = FastAPI(title='API Braba')  


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)  
def read_root():  
    return {'message': 'Olá Mundo!'}

@app.post('/users/', response_model=UserPublic, status_code=HTTPStatus.CREATED)
def create_user(user: UserSchema):
    return user