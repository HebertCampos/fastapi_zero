from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Hello World"}


def test_create_user(client):
    response = client.post(
        "/users/",
        json={
            "username": "alice",
            "email": "alice@example.com",
            "password": "secret",
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "username": "alice",
        "email": "alice@example.com",
        "id": 1,
    }


def test_read_users(client):
    response = client.get("/users/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "users": [
            {
                "username": "alice",
                "email": "alice@example.com",
                "id": 1,
            }
        ]
    }


def test_read_user_by_id(client):
    response = client.get("/users/1")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "username": "alice",
        "email": "alice@example.com",
        "id": 1,
    }


def test_update_user(client):
    response = client.put(
        "/users/1",
        json={
            "username": "bob",
            "email": "bob@example.com",
            "password": "mynewpassword",
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "username": "bob",
        "email": "bob@example.com",
        "id": 1,
    }


def test_delete_user(client):
    response = client.delete("/users/1")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "User deleted"}


def test_not_found_user(client):
    response_get_id = client.get("/users/999")
    response_delete_id = client.delete("/users/999")
    response_put_id = client.put(
        "/users/999",
        json={
            "username": "bob",
            "email": "bob@example.com",
            "password": "mynewpassword",
        },
    )

    assert response_get_id.status_code == HTTPStatus.NOT_FOUND
    assert response_get_id.json() == {"detail": "User not found"}

    assert response_delete_id.status_code == HTTPStatus.NOT_FOUND
    assert response_delete_id.json() == {"detail": "User not found"}

    assert response_put_id.status_code == HTTPStatus.NOT_FOUND
    assert response_put_id.json() == {"detail": "User not found"}
