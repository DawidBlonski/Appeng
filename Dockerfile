FROM python:3.8.0

ENV PYTHONUNBUFFERED 1
WORKDIR /app

COPY appeng/requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .