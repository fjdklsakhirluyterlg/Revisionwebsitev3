import pytest
from backends.models import User
from werkzeug.security import generate_password_hash
import random
from backends import create_app

def mank_random_long_id(length):
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    result = ""
    charactersLength = len(characters) - 1
    for i in range(length):
        result += characters[random.randint(0, charactersLength)]
    return result

@pytest.fixture(scope='module')
def new_user():
    name = "test"
    password = "password"
    security_key = mank_random_long_id(64)
    email = "test@test.com"
    user = User(name=name, email=email, password=generate_password_hash(password, method='sha256'), security_key=security_key)
    return user

@pytest.fixture(scope="module")
def test_client():
    flask_app = create_app()
    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            yield testing_client