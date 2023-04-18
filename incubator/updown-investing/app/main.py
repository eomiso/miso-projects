import fastapi

app = fastapi.FastAPI()


@app.get("/")
def read_root():
    return {"msg": "Hello World"}


@app.get("/async-root")
async def async_read_root():
    return {"msg": "Hello World"}
