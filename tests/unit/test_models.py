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
    secrutiy_key = mank_random_long_id(64)
    