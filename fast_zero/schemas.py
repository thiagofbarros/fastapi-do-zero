from pydantic import BaseModel, EmailStr

class Message(BaseModel):
    message: str

class UserPublic(BaseModel):
    username: str
    email: EmailStr
    is_active: bool

class UserSchema(UserPublic):
    password: str

class UserDB(UserSchema):
    id: int