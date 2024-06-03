import pytest
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_create_item(client):
    response = client.post("/items", json={"name": "Item 1"})
    assert response.status_code == 201
    assert response.json == {"name": "Item 1"}


def test_get_items(client):
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json == [{"name": "Item 1"}]


def test_get_item(client):
    response = client.get("/items/0")
    assert response.status_code == 200
    assert response.json == {"name": "Item 1"}


def test_get_non_existent_item(client):
    response = client.get("/items/999")
    assert response.status_code == 404
    assert response.json == {"error": "Item not found"}


def test_update_item(client):
    response = client.put("/items/0", json={"name": "Updated Item 1"})
    assert response.status_code == 200
    assert response.json == {"name": "Updated Item 1"}


def test_update_non_existent_item(client):
    response = client.put("/items/999", json={"name": "Non-Existent Item"})
    assert response.status_code == 404
    assert response.json == {"error": "Item not found"}


def test_delete_item(client):
    response = client.delete("/items/0")
    assert response.status_code == 204
    response = client.get("/items/0")
    assert response.status_code == 404


def test_delete_non_existent_item(client):
    response = client.delete("/items/999")
    assert response.status_code == 404
    assert response.json == {"error": "Item not found"}
