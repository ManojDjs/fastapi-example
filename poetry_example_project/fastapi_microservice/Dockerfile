FROM python:3.11-slim

WORKDIR /code

# Copy the project files for depenedency and env management

COPY pyproject.toml poetry.lock config.ini /code/
# Install poetry and project depenedencies with poetry
RUN pip install poetry

RUN poetry install 

# Copy app folder into the working directory with app folder similar to our project structure
COPY /app /code/app

# expose port to access the api
EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "app.main:app" ,"--host", "0.0.0.0", "--port", "8000","--workers","4" ]
