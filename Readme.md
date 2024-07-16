This project is for understanding database migrations using alembic.

## Technologies used:
- Azure functions: For scheduling migration script
- Python libraries: alembic, sqlAlchemy
- Database: MSSQL server
- Package management: poetry
----------------------------------------------------------

## What is alembic?
Alembic is a lightweight database migration tool for usage with the SQLAlchemy Database Toolkit for Python. For more information: [Alembic Docs](https://alembic.sqlalchemy.org/en/latest/)

----------------------------------------------------------
## What is poetry?
Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you. Poetry offers a lockfile to ensure repeatable installs, and can build your project for distribution. For more info: [Poetry Docs](https://python-poetry.org/docs/)

----------------------------------------------------------

## What is Azure functions?
Azure functions is a seerverless resource that provides environment for running the code using different triggers.

### Steps to Setup azure function
1. Run below command either at root of the project or at location where you want to create function app.   
` func init --docker`
2. Select programming language
3. Create function using templates available   
` func new --name function_name --template "Timer trigger"`   


### Steps to Setup Dockerfile for Alembic
1. To connect with database, OS requires msodbcsql18 and unixodbc-dev drivers
2. After installing drivers, copy package management content and required files.
3. Install dependencies
4. Add environment variables for azure function app settings