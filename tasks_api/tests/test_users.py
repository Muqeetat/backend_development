import pytest
from jose import jwt
from fastapi.testclient import TestClient
from app.main import app
from app import schemas
from app.config import settings

# =========================================================================
# Setting up the TestClient to simulate HTTP requests to the FastAPI app.
# =========================================================================
client = TestClient(app)

# ===================================================================================
# The 'test_user' fixture will provide a mock user object with predefined attributes 
# (id, name, password) that can be used in multiple test cases.
# ===================================================================================
@pytest.fixture
def test_user():
    return {"id": 1, "name": "hello123", "password": "password123"}

# ====================================================================================
# Test case for the root endpoint ("/").
# Expectation: return a JSON object with the 'message' field containing 'Hello World'.
# ====================================================================================
def test_root():
    res = client.get("/")
    assert res.json().get('message') == 'Hello World'
    assert res.status_code == 200


# # =====================================================================================
# # Test case for creating a new user.
# # Expectation: create a new user with the provided name and password
# # =====================================================================================
# def test_create_user():
#     res = client.post(
#         "/users/", json={"name": "hello123", "password": "password123"})
    
#     new_user = schemas.UserResponse(**res.json())
#     assert new_user.name == "hello123"
#     assert res.status_code == 201  # Check if the status code is 201 (Created)


# =============================================================================================
# Test case for authenticating user login.
# Expectation: successfully authenticate the user
# ==============================================================================================
def test_login_user(test_user):
    res = client.post(
        "/login", data={"username": test_user['name'], "password": test_user['password']})
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token,
                         settings.secret_key, algorithms=[settings.algorithm])
    
    print("Decoded JWT Payload:", payload)
    assert int(payload.get("user_id")) == test_user['id']
    assert login_res.token_type == "bearer"
    assert res.status_code == 200

# ===============================================================================================
# Test various invalid login cases with different username and password combinations.
# Expectation: check to ensure that the correct HTTP status code is returned based on the inputs.
# ===============================================================================================
@pytest.mark.parametrize("name, password, status_code", [
    ('wrong', 'password123', 403),
    ('hello123', 'wrongpassword', 403),
    ('wrong', 'wrongpassword', 403),
    (None, 'password123', 422),
    ('hello123', None, 422)
])
def test_incorrect_login(test_user, name, password, status_code):
    res = client.post(
        "/login", data={"username": name, "password": password})

    assert res.status_code == status_code