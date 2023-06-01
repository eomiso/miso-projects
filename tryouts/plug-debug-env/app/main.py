import inspect

from fastapi import FastAPI
from logger import logger

app = FastAPI()


@app.get("/")
def read_root():
    logger.debug(
        "[DEBUG] This is debug message from"
        f"{inspect.currentframe().f_code.co_filename}:{inspect.currentframe().f_lineno}"
    )

    return {"msg": "Server is running sync"}


@app.get("/async-root")
async def async_read_root():
    logger.debug(
        "[DEBUG] This is debug message from"
        f"{inspect.currentframe().f_code.co_filename}:{inspect.currentframe().f_lineno}"
    )

    return {"msg": "Server is running async"}
