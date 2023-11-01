start:
	uvicorn src.main:app --reload --host 0.0.0.0 --port 6789

redis-run:
	redis-server

celery-worker:
	celery -A src.operations.tasks:celery worker

celery-flower:
	celery -A src.operations.tasks:celery flower

docker-start:
	docker-compose build --no-cache
	docker-compose up

lint:
	flake8 .

# Alembic commands
migrations:
	alembic revision --autogenerate -m $(ARGS)

migrate:
	alembic upgrade $(ARGS)