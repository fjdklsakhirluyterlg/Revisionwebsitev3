from backends import create_app

def test_home_page_get():
    flask_app = create_app()
    with flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert b"hi there" in response.data

def test_home_page_post():
    flask_app = create_app()
    with flask_app.test_client() as test_client:
        response = test_client.post('/')
        assert response.status_code == 405
        assert b"hi there" not in response.data