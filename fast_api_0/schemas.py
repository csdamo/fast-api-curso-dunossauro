from pydantic import BaseModel, ConfigDict, EmailStr, Field


class Message(BaseModel):
    message: str


class Token(BaseModel):
    access_token: str
    token_type: str


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


class FilterPage(BaseModel):
    offset: int = Field(0, ge=0)
    limit: int = Field(100, ge=1)
