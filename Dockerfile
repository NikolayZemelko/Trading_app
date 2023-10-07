FROM python:3.9

ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN pip freeze > requirements.txt

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["make", "start"]
