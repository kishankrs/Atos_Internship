import requests


def test_url():
    response = requests.get("http://bcxtest.herokuapp.com/")
    assert response.status_code == 200
