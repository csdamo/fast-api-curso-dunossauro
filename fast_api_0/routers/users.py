from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import Select, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from fast_api_0.database import get_session
from fast_api_0.models import User
from fast_api_0.schemas import (
    FilterPage,
    Message,
    UserList,
    UserPublic,
    UserSchema,
)
from fast_api_0.security import get_current_user, get_password_hash

router = APIRouter(prefix='/users', tags=['users'])
T_Session = Annotated[Session, Depends(get_session)]
T_CurrentUser = Annotated[User, Depends(get_current_user)]
T_Filter = Annotated[FilterPage, Query()]


@router.post('/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema, session: T_Session):
    db_user = session.scalar(
        select(User).where(  # devolve User | None
            (User.username == user.username) | (User.email == user.email)
        )
    )

    # Se usuário já existe, retorna erro
    if db_user:
        raise HTTPException(
            detail='User already exists.', status_code=HTTPStatus.CONFLICT
        )

    # Se ainda não existe, cria usuário no banco de dados
    db_user = User(
        username=user.username,
        password=get_password_hash(user.password),
        email=user.email,
    )
    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user


@router.get('/', response_model=UserList)
def read_users(session: T_Session, filter_users: T_Filter):
    users = session.scalars(
        Select(User).limit(filter_users.limit).offset(filter_users.offset)
    )
    return {'users': users}


@router.put('/{user_id}', response_model=UserPublic)
def update_user(
    user_id: int,
    user: UserSchema,
    session: T_Session,
    current_user: T_CurrentUser,
):
    if current_user.id != user_id:
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN, detail='Not enough permissions'
        )

    try:
        current_user.username = user.username
        current_user.password = get_password_hash(user.password)
        current_user.email = user.email
        session.commit()
        session.refresh(current_user)

        return current_user

    except IntegrityError:
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT,
            detail='Username or Email already exists',
        )


@router.delete('/{user_id}', response_model=Message)
def delete_user(
    user_id: int,
    session: T_Session,
    current_user: T_CurrentUser,
):
    if current_user.id != user_id:
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN, detail='Not enough permissions'
        )

    session.delete(current_user)
    session.commit()
    return {'message': 'User deleted'}
