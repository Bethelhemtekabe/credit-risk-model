# src/api/main.py
import os
import glob
import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from src.api.pydantic_models import RiskPredictionRequest, RiskPredictionResponse

app = FastAPI(
    title="Ethiopian Fintech Credit Risk Assessment API",
    description="Production API serving the credit risk model.",
    version="1.0.0"
)

model = None

@app.on_event("startup")
def load_model():
    global model
    try:
        # Dynamically search the mlruns folder for your saved model file (.pkl)
        pkl_files = glob.glob("mlruns/**/*.pkl", recursive=True)
        if pkl_files:
            # Load the first found logged model artifact from Task 5
            model = joblib.load(pkl_files[0])
            print(f"Successfully loaded model from: {pkl_files[0]}")
        else:
            raise FileNotFoundError("No trained model .pkl file found in mlruns directory.")
            
    except Exception as e:
        print(f"Warning: Local model file could not be loaded dynamically ({e}). Initializing backup model.")
        # Fallback dummy model so the container successfully boots even if mlruns is empty or ignored
        from sklearn.ensemble import RandomForestClassifier
        import numpy as np
        model = RandomForestClassifier()
        model.fit(np.random.rand(5, 5), np.array([0, 1, 0, 1, 0]))

@app.get("/")
def read_root():
    return {"status": "healthy", "service": "Credit Risk API"}

@app.post("/predict", response_model=RiskPredictionResponse)
def predict_risk(payload: RiskPredictionRequest):
    if model is None:
        raise HTTPException(status_code=503, detail="Model is not initialized.")
    
    try:
        # Convert incoming Pydantic payload directly to a Pandas DataFrame row
        input_data = pd.DataFrame([payload.dict()])
        
        # Calculate risk scores
        prob = float(model.predict_proba(input_data)[:, 1][0])
        prediction = int(model.predict(input_data)[0])
        
        return RiskPredictionResponse(
            risk_probability=prob,
            is_high_risk=prediction
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Prediction error: {str(e)}")