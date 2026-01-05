import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


@st.cache_data
def load_data():
    # Fixed path relative to project root folder
    return pd.read_csv("data/cleaned_transactions.csv")


def app():
    st.title("Fraud Visualizer")
    df = load_data()

    # Extract hour from Time column
    df['Hour'] = pd.to_datetime(df['Time']).dt.hour

    # Fraud rate by hour
    st.write("#### Fraud Rate by Hour")
    fig, ax = plt.subplots()
    sns.barplot(x="Hour", y="Is_Fraud", data=df, ax=ax)
    st.pyplot(fig)

    # Transaction amount distribution
    st.write("#### Transaction Amount Distribution")
    fig, ax = plt.subplots()
    sns.boxplot(x="Is_Fraud", y="Amount", data=df, ax=ax)
    st.pyplot(fig)