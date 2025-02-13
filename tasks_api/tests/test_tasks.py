import pytest
from jose import jwt
from fastapi.testclient import TestClient
from app.main import app
from app import schemas
from app.config import settings
from app.oauth2 import create_access_token

client = TestClient(app)

@pytest.fixture
def test_user():
    return {"id": 1, "name": "hello123", "password": "password123"}

@pytest.fixture
def token(test_user):
    return create_access_token({"user_id": test_user['id']})