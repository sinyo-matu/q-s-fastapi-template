"""Test handlers"""

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_add():
    """Test add"""
    response = client.post("/add", json={"a": 1, "b": 2})
    assert response.status_code == 200
    assert response.json() == {"result": 3}
