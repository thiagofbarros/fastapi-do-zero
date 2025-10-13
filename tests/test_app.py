from http import HTTPStatus


def test_root(client):
    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Olá Mundo!"}


def test_create_user(client):
    response = client.post(
        "/users/",
        json={
            "username": "testuser",
            "email": "test@example.com",
            "password": "strongpassword",
            "is_active": True,
            "id": 1,
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "username": "testuser",
        "email": "test@example.com",
        "is_active": True,
        "id": 1,
    }


def test_read_users(client):
    response = client.get("/users/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "users": [
            {
                "username": "testuser",
                "email": "test@example.com",
                "id": 1,
                "is_active": True,
            }
        ]
    }
