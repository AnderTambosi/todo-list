FROM python:3.5

ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

ADD Pipfile /code/

RUN apt-get update -yq && apt-get upgrade -yq

RUN apt-get install python-pip -yq

RUN pip install pipenv

RUN pipenv install

RUN pipenv install --dev

ADD . /code/
