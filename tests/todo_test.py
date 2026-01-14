from fastapi.testclient import TestClient
from todo_api.main import app

client = TestClient(app)

def test_add_task():
    response = client.post("/add?task=Study")
    assert response.status_code == 200
    assert "Study" in response.json()["todos"]

def test_list_tasks():
    response = client.get("/list")
    assert response.status_code == 200
    assert "todos" in response.json()

def test_delete_task():
    client.post("/add?task=Clean")
    response = client.delete("/delete?task=Clean")
    assert response.status_code == 200
    assert "Clean" not in response.json()["todos"]
