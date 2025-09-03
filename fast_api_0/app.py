from http import HTTPStatus

from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from sqlalchemy import Select, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from fast_api_0.database import get_session
from fast_api_0.models import User

from .schemas import Message, UserList, UserPublic, UserSchema

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá mundo!'}


@app.get('/exercicio2', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def exercicio_02():
    return """
        <html>
            <head>
                <title>Nosso olá mundo!</title>
            </head>
            <body>
                <h1> Olá Mundo </h1>
            </body>
        </html>"""


# ______________versão 2, com banco de dados


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema, session: Session = Depends(get_session)):
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
        username=user.username, password=user.password, email=user.email
    )
    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user


@app.get('/users/', response_model=UserList)
def read_users(
    limit: int = 10, offset: int = 0, session: Session = Depends(get_session)
):
    users = session.scalars(Select(User).limit(limit).offset(offset))
    return {'users': users}


@app.put('/users/{user_id}', response_model=UserPublic)
def update_user(
    user_id: int, user: UserSchema, session: Session = Depends(get_session)
):
    db_user = session.scalar(select(User).where(User.id == user_id))
    if not db_user:
        raise HTTPException(
            detail='User not found', status_code=HTTPStatus.NOT_FOUND
        )
    try:
        db_user.username = user.username
        db_user.password = user.password
        db_user.email = user.email
        session.commit()
        session.refresh(db_user)

        return db_user

    except IntegrityError:
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT,
            detail='Username or Email already exists'
        )


@app.delete('/users/{user_id}', response_model=Message)
def delete_user(user_id: int, session: Session = Depends(get_session)):
    db_user = session.scalar(select(User).where(User.id == user_id))
    if not db_user:
        raise HTTPException(
            detail='User not found', status_code=HTTPStatus.NOT_FOUND
        )

    session.delete(db_user)
    session.commit()
    return {'message': 'User deleted'}
