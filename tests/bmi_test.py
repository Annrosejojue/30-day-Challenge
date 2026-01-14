from fastapi.testclient import TestClient
from bmi_api.main import app

client = TestClient(app)

def test_bmi():
    response = client.get("/bmi?weight=120&height_in=61")
    assert response.status_code == 200
    data = response.json()
    assert abs(data["bmi"] - 22.67) < 0.01


