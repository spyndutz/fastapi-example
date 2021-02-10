# FROM python:3.8-alpine AS base
FROM python:3.9-slim AS base

# Basic Python Setup
ENV PIP_DISABLE_PIP_VERSION_CHECK=on \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DEFAULT_TIMEOUT=100

# Install python package manager
RUN pip3 install poetry

ENV PYTHONPATH=/app
WORKDIR $PYTHONPATH

COPY . .

RUN poetry config virtualenvs.create false && \
  poetry update --no-interaction && \
  poetry install --no-interaction

# Add and run project code
FROM base as main

CMD poetry run python server.py