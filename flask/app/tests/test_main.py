from flask.testing import FlaskClient

from .. import app


def test_read_main(test_client: FlaskClient) -> None:
    response = test_client.get("/")
    assert response is not None

    data = response.data
    assert data is not None

    assert response.status_code == 200
    assert data == str.encode(f"Hello from Flask App! (ENV: {app.config['ENV']})")


def test_users_list(test_client: FlaskClient) -> None:
    response = test_client.get("/users")
    assert response is not None

    json = response.json
    assert json is not None

    assert response.status_code == 200
    assert len(json) == 3
