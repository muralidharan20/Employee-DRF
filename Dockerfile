FROM python:3.10.7-slim-bullseye

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /app

WORKDIR /app

COPY requirement.txt /app

RUN pip install -r requirement.txt

COPY . /app

EXPOSE 8000

CMD Python manage.py runserver