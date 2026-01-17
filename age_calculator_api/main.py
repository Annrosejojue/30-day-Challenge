from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date

app = FastAPI(title="Age Calculator API")

class AgeRequest(BaseModel):
    date_of_birth: date

@app.post("/age")
def calculate_age(req: AgeRequest):
    today = date.today()
    dob = req.date_of_birth

    years = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    days = (today - dob).days
    months = years * 12 + (today.month - dob.month)

    return {
        "years": years,
        "months": months,
        "days": days
    }
