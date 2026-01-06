import pickle
import pandas as pd
import os

# Absolute-safe path resolution
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "utils", "model_pipeline.pkl")

# Load model once at startup
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

print("✅ Model loaded successfully")


def predict_fraud(transaction_data: dict):
    """
    transaction_data: dict with keys matching model features
    returns: prediction (0 = legit, 1 = fraud)
    """

    df = pd.DataFrame([transaction_data])
    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]

    return {
        "prediction": int(prediction),
        "fraud_probability": float(probability)
    }
