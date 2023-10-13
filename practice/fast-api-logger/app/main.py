from typing import Mapping

import uvicorn
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import Response

app = FastAPI()


@app.middleware("http")
async def test_middleware(request: Request, call_next):
    print("This is a middleware called before the main router")
    response: Response = await call_next(request)
    print("This is a middleware called aftert the main router")
    print(await response.json())
    return response


@app.post("/")
def read_root(arg: Mapping[str, str]):
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=1234)
