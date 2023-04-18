import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient

from app.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


@pytest.mark.anyio
async def test_async_read_root():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/async-root")

        assert response.status_code == 200
        assert response.json() == {"msg": "Hello World"}
