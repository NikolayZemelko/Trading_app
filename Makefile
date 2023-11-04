docker-start:
	docker-compose build
	docker-compose up

lint:
	flake8 .

migrate:
	alembic upgrade head