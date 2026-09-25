from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI(
    title="DevOps LLMOps Lab",
    version="0.1.0"
)


class RecommendationRequest(BaseModel):
    body_type: str | None = None
    family: bool = False


@app.get("/health")
def health():
    return {
        "status": "ok",
        "version": "0.1.0",
        "environment": os.getenv("APP_ENV", "local")
    }


@app.post("/recommend")
def recommend(request: RecommendationRequest):
    body_type = (request.body_type or "").lower()

    if body_type == "sedan" and request.family:
        recommendation = "Superb"

    elif body_type == "sedan":
        recommendation = "Octavia"

    elif body_type == "suv":
        recommendation = "Kodiaq"

    else:
        recommendation = "Clarification required"

    return {
        "recommendation": recommendation
    }

@app.get("/info")
def info():
    return {
        "name": "DevOps LLMOps Lab",
        "version": "0.1.0"
    }