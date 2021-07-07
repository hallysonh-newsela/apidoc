import pytest
from blacksheep.testing import TestClient
from ..config import Settings


@pytest.mark.asyncio
async def test_read_main(test_client: TestClient) -> None:
    response = await test_client.get("/")
    assert response is not None

    text = await response.text()
    assert text is not None

    assert response.status == 200
    assert text == f"Hello from BlackSheep App! (ENV: {Settings().environment})"


@pytest.mark.asyncio
async def test_users_list(test_client: TestClient) -> None:
    response = await test_client.get("/users")
    assert response is not None

    json = await response.json()
    assert json is not None

    assert response.status == 200
    assert len(json) == 3
