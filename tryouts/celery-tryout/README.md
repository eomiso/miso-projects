# Celery Tryout

## How to run

```
$ docker compose up -d
$ celery -A simple_celery worker --loglevel=INFO

$ python

>>> from simple_celery import add
>>> res = add.delay(4, 4)
>>> a = res.get()
>>> a.status
```

## Rerences

- [Sample Flower Docker compose file](https://github.com/mher/flower/blob/master/docker-compose.yml)
- sample-fastapi from tiangolo
