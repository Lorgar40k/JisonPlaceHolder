import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

@pytest.fixture
def new_post():
    payload = {
        "title": "fixture post",
        "body": "fixture body",
        "userId": 123
    }
    response = requests.post(BASE_URL, json=payload)
    post = response.json()
    yield post
    requests.delete(f"{BASE_URL}/{post['id']}")
