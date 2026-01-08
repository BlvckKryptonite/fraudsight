import streamlit as st
from pathlib import Path


def app():
    # Logo & Title
    logo_path = Path("assets/logo.png")

    cols = st.columns([1, 4])
    with cols[0]:
        if logo_path.exists():
            st.image(str(logo_path), width=90)
    with cols[1]:
        st.title("FraudSight Risk Analyzer")

    st.markdown("---")

    # Overview
    st.markdown(
        """
        ### Project Overview

        **FraudSight Risk Analyzer** is a predictive analytics prototype
        designed to identify potentially fraudulent
        financial transactions using a trained machine learning model.

        The application demonstrates an end-to-end data science workflow
        , including:
        data preparation, model training, evaluation, and interactive
         visualization.
        """
    )

    # Key Features
    st.markdown(
        """
        ### Key Features
        - **Fraud Detector**: Upload a CSV of transactions and receive
          fraud predictions
        - **Fraud Visualizer**: Explore patterns and distributions in
         transaction data
        - **Model Performance**: Review evaluation metrics and model behavior
        """
    )

    # Dataset
    st.markdown(
        """
        ### Dataset
        - **Original dataset:**
          [Kaggle – Credit Card Fraud Dataset][kaggle_link]

        - A **condensed sample** of the original dataset is included
          for deployment and demonstration
          purposes due to hosting and upload limitations.

        [kaggle_link]: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud
        """
    )

    # README Link
    repo_url = (
        "https://github.com/BlvckKryptonite/"
        "fraudsight/blob/main/README.md"
    )

    st.markdown(
        f"""
        ### Documentation

        👉 **Full project details and setup instructions**
        and deployment notes are available
        [in the README here.]({repo_url})

        The README explains:
        - How to run the app locally with the full dataset
        - Dataset size limitations in the deployed version
        - Model design decisions and evaluation results
        """
    )
