FROM python:3.5

ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

ADD Pipfile /code/

RUN apt-get update -yq && apt-get upgrade -yq

RUN apt-get install python-pip -yq

RUN apt-get install -y -qq git curl wget

# install npm
RUN apt-get install -y -qq npm
RUN ln -s /usr/bin/nodejs /usr/bin/node

# install bower
RUN npm install --global bower


RUN pip install pipenv

RUN pipenv install

RUN pipenv install --dev

ADD . /code/
