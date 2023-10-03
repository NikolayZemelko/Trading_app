start:
	 uvicorn main:app --reload

lint:
	flake8 .
