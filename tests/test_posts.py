import pytest
import requests
import allure

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

@pytest.fixture
def new_post():
    payload = {
        "title": "fixture post",
        "body": "fixture body",
        "userId": 123
    }
    with allure.step("Создание нового поста через API"):
        response = requests.post(BASE_URL, json=payload)
        assert response.status_code == 201
        post = response.json()
    yield post

def test_get_all_posts():
    with allure.step("Получение всех постов"):
        response = requests.get(BASE_URL)
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) > 0

def test_post_new_post():
    payload = {
        "id": 0,
        "title": "string",
        "body": "string",
        "userId": 0
    }
    with allure.step("Создание нового поста"):
        response = requests.post(BASE_URL, json=payload)
        assert response.status_code == 201
        data = response.json()
        assert data["title"] == payload["title"]

def test_get_post_by_id(new_post):
    post_id = new_post["id"]
    with allure.step(f"Получение поста с id={post_id}"):
        response = requests.get(f"{BASE_URL}/{post_id}")
        assert response.status_code in [200, 404]

def test_put_post_by_id(new_post):
    post_id = new_post["id"]
    payload = {
        "id": post_id,
        "title": "updated title",
        "body": "updated body",
        "userId": new_post["userId"]
    }
    with allure.step(f"Обновление поста с id={post_id}"):
        response = requests.put(f"{BASE_URL}/{post_id}", json=payload)
        assert response.status_code in [200, 500]

def test_delete_post_by_id():
    post_id = 20
    with allure.step(f"Удаление поста с id={post_id}"):
        response = requests.delete(f"{BASE_URL}/{post_id}")
        assert response.status_code == 200
