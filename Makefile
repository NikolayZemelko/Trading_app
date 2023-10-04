start:
	 uvicorn main:app --reload --host 0.0.0.0

docker-start:
	docker-compose up

lint:
	flake8 .
