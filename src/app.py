import streamlit as st

from app_pages import (
    project_summary,
    fraud_visualizer,
    fraud_detector,
    model_performance
)

st.set_page_config(page_title="FraudSight", layout="wide")

pages = {
    "📘 Project Summary": project_summary,
    "📊 Fraud Visualizer": fraud_visualizer,
    "🕵🏾 Fraud Detector": fraud_detector,
    "📈 Model Performance": model_performance,
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(pages.keys()))

page = pages[selection]
page.app()
