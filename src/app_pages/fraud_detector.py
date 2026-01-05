import streamlit as st
import pickle
import pandas as pd


@st.cache_resource
def load_model():
    with open("src/utils/model_pipeline.pkl", "rb") as f:
        return pickle.load(f)


def app():
    st.title("Fraud Detector")
    model = load_model()

    uploaded_file = st.file_uploader("Upload transactions (CSV)")
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        predictions = model.predict(df)
        df["Prediction"] = predictions
        st.write(df[["Transaction_ID", "Amount", "Prediction"]])
