import pytest

# Base fixture
@pytest.fixture
def user_data():
    return {"username": "testuser", "email": "test@example.com"}

# Fixture that depends on user_data
@pytest.fixture
def user_profile(user_data):
    user_data["premium"] = True
    return user_data

# Test using the dependent fixture
def test_user_profile(user_profile):
    assert user_profile["username"] == "testuser"
    assert user_profile["premium"] is True



