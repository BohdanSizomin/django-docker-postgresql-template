FROM python:3.12-slim

# Set environment variables
ENV PYTHONFAULTHANDLER 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on

# Installing dependencies
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        bash \
        build-essential \
        curl \
        gettext \
        git \
        libpq-dev \
        wget \
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Installing Poetry
RUN pip install poetry

# Install app dependencies
COPY poetry.lock pyproject.toml poetry.toml /app/
RUN poetry install --no-dev --no-interaction --no-ansi

# Copy the rest of the application code
COPY . .

EXPOSE 8000
