FROM python:3.13-slim
ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app
COPY . .

RUN pip install poetry

ENV POETRY_HTTP_TIMEOUT=600
ENV POETRY_REQUESTS_TIMEOUT=600

RUN poetry config installer.max-workers 2
RUN poetry install --no-interaction --no-ansi --without dev

EXPOSE 8000
CMD poetry run uvicorn --host 0.0.0.0 fast_api_0.app:app