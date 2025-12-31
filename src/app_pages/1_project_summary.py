import streamlit as st


def app():
    st.title("FraudSight Risk Analyzer")
    st.markdown("""
    ### Project Overview
    This app detects fraudulent transactions using predictive analytics.
    - **Goal**: Reduce financial losses by flagging high-risk transactions.
    - **Dataset**: [Kaggle Credit Card Fraud]
                (https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
    """)
