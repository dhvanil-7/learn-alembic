ARG IMAGE_VERSION=4-python3.10

FROM mcr.microsoft.com/azure-functions/python:${IMAGE_VERSION}

RUN apt-get update && \
    ACCEPT_EULA=Y apt-get install -y msodbcsql18 unixodbc-dev

RUN pip install poetry

WORKDIR /src

COPY ./poetry.lock ./pyproject.toml ./

RUN poetry config virtualenvs.create false && \
    poetry config virtualenvs.in-project true && \
    poetry install

WORKDIR /src/learn_alembic

CMD ["alembic", "upgrade", "head"]