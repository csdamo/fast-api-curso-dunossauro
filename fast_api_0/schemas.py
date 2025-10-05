from pydantic import BaseModel, ConfigDict, EmailStr, Field

from fast_api_0.models import TodoState


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


class FilterTodo(FilterPage):
    title: str | None = Field(default=None, min_length=3, max_length=20)
    description: str | None = Field(default=None, min_length=3, max_length=20)
    state: TodoState | None = None


class TodoSchema(BaseModel):
    title: str
    description: str
    state: TodoState = Field(default=TodoState.todo)


class TodoPublic(TodoSchema):
    id: int


class TodoList(BaseModel):
    todos: list[TodoPublic]


class TodoUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    state: TodoState | None = None
