"""
app.py
FastAPI service that loads the trained Netflix model
and exposes a /predict endpoint.
"""

import joblib
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel

# load model and encoder once at startup
model = joblib.load("model.pkl")
le = joblib.load("label_encoder.pkl")

app = FastAPI(title="Netflix Type Predictor")


class NetflixInput(BaseModel):
    """Input schema — release year of the title."""
    release_year: int


class PredictionResponse(BaseModel):
    """Output schema — predicted type."""
    release_year: int
    prediction: str


@app.get("/")
def root():
    """Health check."""
    return {"status": "ok", "message": "Netflix Predictor is running"}


@app.post("/predict", response_model=PredictionResponse)
def predict(data: NetflixInput):
    """
    Predict whether a title is a Movie or TV Show.

    Args:
        data: JSON with release_year field.

    Returns:
        Predicted type as string.
    """
    features = np.array([[data.release_year]])
    pred = model.predict(features)[0]
    label = le.inverse_transform([pred])[0]

    return PredictionResponse(
        release_year=data.release_year,
        prediction=label
    ) 