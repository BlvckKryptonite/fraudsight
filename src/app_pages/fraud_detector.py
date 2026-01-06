import streamlit as st
import pickle
import pandas as pd
from pathlib import Path


st.set_page_config(
    page_title="FraudSight — Fraud Detector",
    layout="centered",
)


@st.cache_resource
def load_model():
    BASE_DIR = Path(__file__).resolve().parents[2]
    MODEL_PATH = BASE_DIR / "src" / "utils" / "model_pipeline.pkl"

    with open(MODEL_PATH, "rb") as f:
        return pickle.load(f)


def app():
    st.title("🕵🏾 Fraud Detector")
    st.write("Upload a transaction CSV to detect potential fraud.")

    model = load_model()
    st.success("Model loaded successfully.")

    uploaded_file = st.file_uploader(
        "Upload transactions (CSV)",
        type=["csv"]
    )

    if uploaded_file:
        df = pd.read_csv(uploaded_file)

        # Standardize/normalize input
        if "Class" in df.columns:
            df = df.drop(columns=["Class"])

        # Ensuring correct feature order
        df = df[model.feature_names_in_]

        # Prediction
        predictions = model.predict(df)
        probabilities = model.predict_proba(df)[:, 1]

        results = df.copy()
        results["Fraud_Prediction"] = predictions
        results["Fraud_Probability"] = probabilities

        # Some UI output polish
        st.subheader("Prediction Results")

        # Limit maximum rows to display
        MAX_DISPLAY_ROWS = 100

        st.dataframe(
            results[["Amount", "Fraud_Prediction", "Fraud_Probability"]]
            .head(MAX_DISPLAY_ROWS)
            .assign(
                Fraud_Prediction=lambda x: x["Fraud_Prediction"].map(
                    {0: "Legitimate", 1: "Fraud"}
                )
            )
            .style.format({"Fraud_Probability": "{:.2%}"})
        )

        st.write(f"Displaying top {MAX_DISPLAY_ROWS} transactions")

        fraud_count = results["Fraud_Prediction"].sum()
        st.info(
            f"🚨 Detected {fraud_count} potentially fraudulent transactions."
        )
