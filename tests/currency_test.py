from fastapi.testclient import TestClient
from currency_api.main import app
from unittest.mock import patch

client = TestClient(app)

@patch("currency_api.main.requests.get")
def test_convert_currency(mock_get):
    mock_get.return_value.json.return_value = {
        "rates": {"INR": 80}
    }

    response = client.get("/convert?amount=10&from_currency=USD&to_currency=INR")
    assert response.status_code == 200
    data = response.json()

    assert data["converted_amount"] == 800
