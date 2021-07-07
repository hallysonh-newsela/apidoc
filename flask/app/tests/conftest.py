import pytest
from flask.testing import FlaskClient

from .. import app


@pytest.fixture
def test_client() -> FlaskClient:
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client
