from pydantic import BaseModel, ConfigDict, EmailStr


class Message(BaseModel):
    message: str


class BaseUserSchema(BaseModel):
    username: str
    email: EmailStr


class UserSchema(BaseUserSchema):
    password: str


class UserPublic(BaseUserSchema):
    id: int
    model_config = ConfigDict(from_attributes=True)


class UserList(BaseModel):
    users: list[UserPublic]
