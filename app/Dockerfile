FROM python:3.12-slim

ENV PYTHONBUFFERED 1

WORKDIR /app

RUN apt-get -y update
RUN pip install --upgrade pip && pip install poetry

USER root

COPY pyproject.toml /app/

RUN poetry config virtualenvs.create false --local
RUN poetry install --no-interaction

COPY . .
