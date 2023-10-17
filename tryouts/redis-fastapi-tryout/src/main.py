import logging
import pickle

import redis
import requests
from fastapi import FastAPI

logger = logging.getLogger("uvicorn.access")

rd = redis.Redis(host="localhost", port=6379, db=0)
app = FastAPI()


def set_cache(key, value):
    if isinstance(value, dict):
        rd.set(key, pickle.dumps(value))


def get_cache(key):
    import pdb

    pdb.set_trace()
    cache = rd.hgetall(key)
    if cache:
        return pickle.loads(cache)

    return None


@app.get("/")
def read_root():
    return "Hello World"


@app.get("/users/{user_id}")
def read_fish(user_id: str):
    r = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    # import pdb; pdb.set_trace()
    cache = get_cache(user_id)
    if cache:
        return cache
    else:
        set_cache(user_id, r.json())

    return r.json()
