FROM python:3.10.4

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /blog_project

COPY Pipfile Pipfile.lock /blog_project/
RUN pip install pipenv && pipenv install --system

COPY . /blog_project/

