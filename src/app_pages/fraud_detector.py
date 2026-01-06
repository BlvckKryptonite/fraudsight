import streamlit as st
import pickle
import pandas as pd


st.set_page_config(
    page_title="FraudSight — Fraud Detector",
    layout="centered",
)


@st.cache_resource
def load_model():
    with open("src/utils/model_pipeline.pkl", "rb") as f:
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

        st.dataframe(
            results[["Amount", "Fraud_Prediction", "Fraud_Probability"]]
            .assign(
                Fraud_Prediction=lambda x: x["Fraud_Prediction"].map(
                    {0: "Legitimate", 1: "Fraud"}
                )
            )
            .style.format({"Fraud_Probability": "{:.2%}"})
        )

        fraud_count = results["Fraud_Prediction"].sum()
        st.info(
            f"🚨 Detected {fraud_count} potentially fraudulent transactions.")
