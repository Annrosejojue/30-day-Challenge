from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/convert")
def convert_currency(amount: float, from_currency: str, to_currency: str):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency.upper()}"
    data = requests.get(url).json()
    rate = data["rates"][to_currency.upper()]
    converted = amount * rate
    return {
        "amount": amount,
        "from": from_currency,
        "to": to_currency,
        "converted_amount": round(converted, 2)
    }
