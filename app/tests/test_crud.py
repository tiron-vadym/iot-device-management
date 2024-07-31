import pytest
from aiohttp.test_utils import TestClient, TestServer
from peewee import PostgresqlDatabase

from app.models import BaseModel
from main import app


@pytest.fixture
def client() -> TestClient:
    server = TestServer(app)
    return TestClient(server)


test_db = PostgresqlDatabase(
    database="test_db",
    user="test_user",
    password="test_password",
    host="localhost",
    port=5432
)


@pytest.fixture(scope="module")
async def setup_db():
    test_db.connect()
    test_db.create_tables([BaseModel], safe=True)

    yield

    test_db.drop_tables([BaseModel], safe=True)
    test_db.close()


async def test_create_device(client: TestClient, setup_db):
    data = {
        "name": "Device1",
        "type": "Type1",
        "login": "login1",
        "password": "password1",
        "location_id": 1,
        "api_user_id": 1
    }
    response = await client.post("/devices/", json=data)
    assert response.status == 201
    response_data = await response.json()
    assert response_data["name"] == data["name"]
    assert response_data["type"] == data["type"]
    assert response_data["login"] == data["login"]


async def test_get_devices(client: TestClient, setup_db):
    response = await client.get("/devices/")
    assert response.status == 200
    response_data = await response.json()
    assert isinstance(response_data, list)


async def test_get_device(client: TestClient, setup_db):
    data = {
        "name": "Device2",
        "type": "Type2",
        "login": "login2",
        "password": "password2",
        "location_id": 1,
        "api_user_id": 1
    }
    response = await client.post("/devices/", json=data)
    assert response.status == 201
    created_device = await response.json()

    device_id = created_device["id"]
    response = await client.get(f"/devices/{device_id}/")
    assert response.status == 200
    response_data = await response.json()
    assert response_data["id"] == device_id
    assert response_data["name"] == data["name"]


async def test_update_device(client: TestClient, setup_db):
    data = {
        "name": "Device3",
        "type": "Type3",
        "login": "login3",
        "password": "password3",
        "location_id": 1,
        "api_user_id": 1
    }
    response = await client.post("/devices/", json=data)
    assert response.status == 201
    created_device = await response.json()

    device_id = created_device["id"]
    updated_data = {
        "name": "UpdatedDevice3",
        "type": "UpdatedType3"
    }
    response = await client.put(f"/devices/{device_id}/", json=updated_data)
    assert response.status == 200
    response_data = await response.json()
    assert response_data["name"] == updated_data["name"]
    assert response_data["type"] == updated_data["type"]


async def test_delete_device(client: TestClient, setup_db):
    data = {
        "name": "Device4",
        "type": "Type4",
        "login": "login4",
        "password": "password4",
        "location_id": 1,
        "api_user_id": 1
    }
    response = await client.post("/devices/", json=data)
    assert response.status == 201
    created_device = await response.json()

    device_id = created_device["id"]
    response = await client.delete(f"/devices/{device_id}/")
    assert response.status == 200

    response = await client.get(f"/devices/{device_id}/")
    assert response.status == 404
