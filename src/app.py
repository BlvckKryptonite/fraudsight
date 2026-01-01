import streamlit as st
import importlib

# Import modules whose filenames start with a digit using importlib and assign to valid identifiers
_1_project_summary = importlib.import_module("app_pages.1_project_summary")
_2_fraud_visualizer = importlib.import_module("app_pages.2_fraud_visualizer")
_3_fraud_detector = importlib.import_module("app_pages.3_fraud_detector")
_4_model_performance = importlib.import_module("app_pages.4_model_performance")
pages = {
    "Project Summary": _1_project_summary,
    "Fraud Visualizer": _2_fraud_visualizer,
    "Fraud Detector": _3_fraud_detector,
    "Model Performance": _4_model_performance
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(pages.keys()))
page = pages[selection]
page.app()
