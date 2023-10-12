start:
	uvicorn src.main:app --reload --host 0.0.0.0

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