from backends.models import User
import random
from werkzeug.security import generate_password_hash, check_password_hash

def mank_random_long_id(length):
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    result = ""
    charactersLength = len(characters) - 1
    for i in range(length):
        result += characters[random.randint(0, charactersLength)]
    return result

def test_user_model():
    name = "test"
    password = "password"
    security_key = mank_random_long_id(64)
    email = "test@test.com"
    user = User(name=name, email=email, password=generate_password_hash(password, method='sha256'), security_key=security_key)

    assert user.email == "test@test.com"
    assert user.password != "password"
    assert check_password_hash(user.password, "password")
    assert user.is_authenticated

def test_user_with_fixtures(new_user):
    assert new_user.email == "test@test.com"
    assert new_user.password != "password"
    assert check_password_hash(new_user.password, "password")

def test_blog(new_blog):
    assert new_blog.views == 0