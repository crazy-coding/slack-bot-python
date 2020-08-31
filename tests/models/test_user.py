# import pytest, os
# from flask_migrate import Migrate

# from app import app
# from app.models import db, User

# @pytest.fixture(scope="module")
# def client():
#     return app.test_client()

# def test_user(client):
#     resp = client.get('/api/users')
#     assert resp.status_code == 200
