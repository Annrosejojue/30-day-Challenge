from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/bmi")
def calculate_bmi(
    weight: float = Query(..., description="Weight in pounds"),
    height_in: float = Query(..., description="Height in inches")
):
    bmi = (weight * 703) / (height_in ** 2)
    return {
        "weight": weight,
        "height_in": height_in,
        "bmi": round(bmi, 2)
    }
