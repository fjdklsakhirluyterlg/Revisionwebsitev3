import pytest
from backends.models import User
from werkzeug.security import generate_password_hash
import random

def mank_random_long_id(length):
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    result = ""
    charactersLength = len(characters) - 1
    for i in range(length):
        result += characters[random.randint(0, charactersLength)]
    return result

def new_user():
    name = "test"
    password = "password"
    security_key = mank_random_long_id(64)
    email = "test@test.com"
    user = User(name=name, email=email, password=generate_password_hash(password, method='sha256'), security_key=security_key)