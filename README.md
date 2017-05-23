# Todo-List

[![Build Status](https://travis-ci.org/hudsonbrendon/todo-list.svg?branch=master)](https://travis-ci.org/hudsonbrendon/todo-list)
![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)


![todo](todo.gif)


# To install and configure docker access:

- [Docker: Tudo o que você precisa saber para começar a usar](https://medium.com/@hudsonbrendon/docker-tudo-o-que-voc%C3%AA-precisa-saber-para-come%C3%A7ar-a-usar-b82b2d4284f0)

- [Conteinerizando suas aplicações django com docker e docker-compose](https://medium.com/grupy-rn/conteinerizando-suas-aplica%C3%A7%C3%B5es-django-com-docker-e-docker-compose-3e86a8df6984)


# Install

```sh
$ git clone https://github.com/hudsonbrendon/todo-list.git
$ cd todo-list
$ docker-compose run web pipenv run python manage.py makemigrations
$ docker-compose run web pipenv run python manage.py migrate
```
And

```sh
$ docker-compose run web bower install
```

# Running

For running:

```sh
$ docker-compose up
```
or
```sh
$ docker-compose up -d
```
For running in background.

# Access

To access the platform:

[localhost:8000](http://localhost:8000)

# Tests

For running tests:

```sh
$ ./runtests
```

# Dependencies

- [Docker](https://docker.com)
- [docker-compose](https://docs.docker.com/compose/)
- [Python 3.5](https://www.python.org/downloads/release/python-350/)
- [Pipenv](https://github.com/kennethreitz/pipenv)
- [NodeJS](https://nodejs.org/en/)
- [Bower](https://bower.io/)
