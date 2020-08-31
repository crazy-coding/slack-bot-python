""" pytests for Flask """

import pytest
from app import app

@pytest.fixture(scope="module")
def client():
    return app.test_client()

def test_api(client):
    resp = client.get('/')
    assert resp.status_code == 200
