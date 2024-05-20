FROM python:3.11-slim

WORKDIR /app

# Copy the project files
COPY . .

#COPY pyproject.toml poetry.lock /app/

RUN pip install poetry
RUN poetry install 

COPY . /app

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "app.main:app" ,"--host", "0.0.0.0", "--port", "8000","--workers","4" ]
