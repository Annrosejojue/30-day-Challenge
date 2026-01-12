from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/weather")
def get_weather(city: str):
    url = f"https://wttr.in/{city}?format=j1"
    data = requests.get(url).json()
    current = data["current_condition"][0]
    return {
        "city": city,
        "temperature_C": current["temp_C"],
        "humidity": current["humidity"],
        "weather": current["weatherDesc"][0]["value"]
    }
