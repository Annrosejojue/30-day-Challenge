from fastapi.testclient import TestClient
from weather_api.main import app
from unittest.mock import patch

client = TestClient(app)

@patch("weather_api.main.requests.get")
def test_weather(mock_get):
    mock_get.return_value.json.return_value = {
        "current_condition": [{
            "temp_C": "20",
            "humidity": "50",
            "weatherDesc": [{"value": "Sunny"}]
        }]
    }

    response = client.get("/weather?city=London")
    assert response.status_code == 200
    data = response.json()

    assert data["city"] == "London"
    assert data["temperature_C"] == "20"
    assert data["weather"] == "Sunny"
