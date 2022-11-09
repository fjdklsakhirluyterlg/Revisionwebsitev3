from urllib import response
from backends import create_app

def test_home_page_get():
    flask_app = create_app()
    with flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert b"Hi there" in response.data

def test_home_page_post():
    flask_app = create_app()
    with flask_app.test_client() as test_client:
        response = test_client.post('/')
        # assert response.status_code != 200
        assert b"Hi there" not in response.data 
        assert b"wrong method" in response.data

def test_home_page_get_with_fixture(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hi there" in response.data

def test_home_page_post_with_fixture(client):
    response = client.post('/')
    # assert response.status_code == 405
    assert b"Hi there" not in response.data
    assert b"wrong method" in response.data

def test_todo_application(client):
    response = client.post("/todo/add", data={
        "title": "test"
    })
    assert response.status_code == 302

def test_blog_post(client):
    response = client.post("/blogs/add", json={
        "title":"test",
        "content":"content test",
        "feature_image":"stuff",
        "tags":["test", "stuff"]
    })
    assert response.json
    assert response.status_code == 200

def test_community_post(client):
    response = client.post("/api/community/add", json={
        "title":"a title",
        "content":"a contnet",
        "userid":1,
        "tags":["test", "stuff"]
    })
    assert response.json
    assert response.status_code == 200

def test_url_shotener_create_id(client):
    response = client.post("/api/urls/shortner/add", json={
        "actual":"https://www.google.com"
    })
    assert response.status_code == 200
