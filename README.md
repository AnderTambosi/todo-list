# Todo-List

[![Build Status](https://travis-ci.org/hudsonbrendon/todo-list.svg?branch=master)](https://travis-ci.org/hudsonbrendon/todo-list)
![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)


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

For running:

```sh
$ docker-compose up
```

And access:

[localhost:8000](http://localhost:8000)

Using autofixture for populate tasks:

```sh
$ docker-compose run web pipenv run python manage.py loadtestdata tasks.Task:30
```

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
