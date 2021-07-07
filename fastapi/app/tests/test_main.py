from fastapi.testclient import TestClient

from ..config import get_settings
from ..main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    env = get_settings().environment
    print(env)
    assert response.status_code == 200
    assert response.text == f"Hello from FastAPI App! (ENV: {env})"


def test_users_list():
    response = client.get("/users")
    assert response.status_code == 200
    assert len(response.json()) == 3
