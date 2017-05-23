# Todo-List

[![Build Status](https://travis-ci.org/hudsonbrendon/todo-list.svg?branch=master)](https://travis-ci.org/hudsonbrendon/todo-list)
![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)


# Install

```sh
$ https://github.com/hudsonbrendon/todo-list.git
$ cd todo-list
$ docker-compose run web pipenv python manage.py makemigrations
$ docker-compose run web pipenv python manage.py migrate
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

# Tests
```sh
$ ./runtests
```

# Dependencies

- [Python 3.5](https://www.python.org/downloads/release/python-350/)
- [Pipenv](https://github.com/kennethreitz/pipenv)
- [NodeJS](https://nodejs.org/en/)
- [Bower](https://bower.io/)
