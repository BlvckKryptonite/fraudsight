import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


@st.cache_data
def load_data():
    df = pd.read_csv("data/cleaned_transactions.csv")

    # Normalize target column
    if "Class" in df.columns:
        df = df.rename(columns={"Class": "Is_Fraud"})

    # Mapping the Hour column from Time (seconds since first transaction)
    df["Hour"] = (df["Time"] // 3600) % 24

    return df


def app():
    st.title("📊 Fraud Visualizer")
    df = load_data()

    #  Fraud rate by hour
    st.subheader("Fraud Rate by Hour")
    fig, ax = plt.subplots()
    sns.barplot(x="Hour", y="Is_Fraud", data=df, ax=ax)
    ax.set_ylabel("Fraud Rate")
    st.pyplot(fig)

    # Transaction amount distribution
    st.subheader("Transaction Amount Distribution")
    fig, ax = plt.subplots()
    sns.boxplot(x="Is_Fraud", y="Amount", data=df, ax=ax)
    ax.set_xticklabels(["Legitimate", "Fraud"])
    st.pyplot(fig)
