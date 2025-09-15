from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_api_0.routers import auth, users

from .schemas import Message

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)


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
