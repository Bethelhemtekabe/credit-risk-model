# src/api/pydantic_models.py
from pydantic import BaseModel, Field

class RiskPredictionRequest(BaseModel):
    # TODO: Replace these with your exact model features from Task 5
    Amount: float = Field(..., description="Transaction amount value", example=5000.0)
    Value: float = Field(..., description="Absolute value of transaction", example=5000.0)
    Recency: float = Field(..., description="Days since last transaction", example=12.0)
    Frequency: float = Field(..., description="Total count of transactions", example=36.0)
    Monetary: float = Field(..., description="Total spent amount", example=180000.0)

    class Config:
        json_schema_extra = {
            "example": {
                "Amount": 2500.0,
                "Value": 2500.0,
                "Recency": 5.0,
                "Frequency": 42.0,
                "Monetary": 120000.0
            }
        }

class RiskPredictionResponse(BaseModel):
    risk_probability: float = Field(..., description="Probability of being high risk (0.0 to 1.0)")
    is_high_risk: int = Field(..., description="Binary classification label (0 or 1)")