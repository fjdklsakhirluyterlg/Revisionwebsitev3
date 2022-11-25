import pytest
from backends.models import User, Blog, Post, Chat, Urlshortner, Item, Object
from werkzeug.security import generate_password_hash
import random
from backends import create_app
from backends.url_shortener.add import generate_random_id

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

@pytest.mark.database_access
@pytest.fixture(scope='module')
def app_thingy():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///test.db"
    })

    yield app

@pytest.fixture()
def client(app_thingy):
    return app_thingy.test_client()

@pytest.mark.database_access
@pytest.fixture(scope="module")
def new_blog():
    blog = Blog(title="test", feature_image="stuff", content="content")
    return blog

@pytest.mark.database_access
@pytest.fixture(scope="module")
def new_post(new_user):
    user_id = new_user.id
    post = Post(title="title", content="this is a test", user_id=user_id)
    return post

@pytest.mark.database_access
@pytest.fixture(scope="module")
def new_chat(new_user):
    description = "description"
    name = "name"
    new = Chat(description=description, name=name)
    new_user.chats.append(new)
    return new

@pytest.mark.database_access
@pytest.fixture(scope="module")
def new_url(new_user):
    actual = "https://www.google.com"
    id = generate_random_id()
    new = Urlshortner(actual=actual, id=id, user_id=new_user.id)
    return new

@pytest.mark.database_access
@pytest.fixture(scope="module")
def new_item():
    new = Item(user_id=1, title="item")
