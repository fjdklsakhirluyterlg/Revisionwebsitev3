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

# def test_home_page_get_with_fixture(test_client):
#     response = test_client.get('/')
#     assert response.status_code == 200
#     assert b"Hi there" in response.data

# def test_home_page_post_with_fixture(test_client):
#     response = test_client.post('/')
#     # assert response.status_code != 200
#     assert b"Hi there" not in response.data
#     assert b"wrong method" in response.data
