# Trading_app
Started on render:
https://fastapi-app-mxel.onrender.com/

#### This project is a Python-based trading application. It uses poetry for dependency management and includes a Makefile for easy project execution.
-
Using:
- FastAPI
- SQLAlchemy
- Alembic
- Redis
- Celery
- Gunicorn

## Installation

Or use step-by-step way:
1. Clone the repository:
```
git clone https://github.com/NikolayZemelko/Trading_app.git
```
2. Install dependencies:
```
poetry shell && poetry install
```
3. Create `.env` file in root directory, use `.env-example` as a basis 
   
5. Make Alembic migrations
```
make migrate
```
6. Use command to start all services
```
make docker-start
```

#### Open your APP http://0.0.0.0:9999 
#### Open Flower http://0.0.0.0:8888