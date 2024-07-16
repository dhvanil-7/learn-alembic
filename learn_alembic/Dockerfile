ARG IMAGE_VERSION=4-python3.10

FROM mcr.microsoft.com/azure-functions/python:${IMAGE_VERSION}

ENV AzureWebJobsScriptRoot=/src/learn_alembic \
    AzureFunctionsJobHost__Logging__Console__IsEnabled=true

RUN apt-get update && \
    ACCEPT_EULA=Y apt-get install -y msodbcsql18 unixodbc-dev azure-functions-core-tools-4

RUN pip install poetry

WORKDIR /src

COPY ./poetry.lock ./pyproject.toml ./

RUN poetry config virtualenvs.create false && \
    poetry config virtualenvs.in-project true && \
    poetry install
