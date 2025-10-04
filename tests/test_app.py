from http import HTTPStatus
from fastapi.testclient import TestClient
from fast_zero.app import app


def test_root():
    client = TestClient(app)

    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Olá Mundo!"}


def test_create_user():
    client = TestClient(app)

    response = client.post(
        "/users/",
        json={
            "username": "testuser",
            "email": "test@email.com",
            "password": "strongpassword",
            "is_active": True,
            "id": 1,
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "username": "testuser",
        "email": "test@email.com",
        "is_active": True,
        "id": 1,
    }
