FROM python:latest

RUN pip install poetry

WORKDIR /app

COPY . .

RUN poetry install
