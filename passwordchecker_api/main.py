from fastapi import FastAPI
from pydantic import BaseModel
import string

app = FastAPI(title="Password Strength API")

class PasswordRequest(BaseModel):
    password: str

@app.post("/check")
def check_password(req: PasswordRequest):
    pwd = req.password
    length = len(pwd)

    has_upper = any(c.isupper() for c in pwd)
    has_lower = any(c.islower() for c in pwd)
    has_digit = any(c.isdigit() for c in pwd)
    has_symbol = any(c in string.punctuation for c in pwd)

    score = sum([length >= 8, has_upper, has_lower, has_digit, has_symbol])

    strength = "Weak"
    if score == 3:
        strength = "Moderate"
    if score >= 4:
        strength = "Strong"

    return {
        "strength": strength,
        "score": score,
        "length": length,
        "has_upper": has_upper,
        "has_lower": has_lower,
        "has_digit": has_digit,
        "has_symbol": has_symbol
    }
