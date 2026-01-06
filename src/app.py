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


# ---- TEST BLOCK (temporary) ----
if __name__ == "__main__":
    sample_transaction = {
        "Time": 100000,
        "V1": -1.359807,
        "V2": -0.072781,
        "V3": 2.536346,
        "V4": 1.378155,
        "V5": -0.338321,
        "V6": 0.462388,
        "V7": 0.239599,
        "V8": 0.098698,
        "V9": 0.363787,
        "V10": 0.090794,
        "V11": -0.551600,
        "V12": -0.617801,
        "V13": -0.991390,
        "V14": -0.311169,
        "V15": 1.468177,
        "V16": -0.470401,
        "V17": 0.207971,
        "V18": 0.025791,
        "V19": 0.403993,
        "V20": 0.251412,
        "V21": -0.018307,
        "V22": 0.277838,
        "V23": -0.110474,
        "V24": 0.066928,
        "V25": 0.128539,
        "V26": -0.189115,
        "V27": 0.133558,
        "V28": -0.021053,
        "Amount": 149.62
    }

    result = predict_fraud(sample_transaction)
    print(result)
