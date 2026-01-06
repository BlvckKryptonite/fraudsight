import streamlit as st
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, roc_curve, auc
import seaborn as sns
import pickle
import pandas as pd
from pathlib import Path


@st.cache_resource
def load_model():
    BASE_DIR = Path(__file__).resolve().parents[2]
    MODEL_PATH = BASE_DIR / "src" / "utils" / "model_pipeline.pkl"

    with open(MODEL_PATH, "rb") as f:
        return pickle.load(f)


def app():
    st.title("Model Performance")
    model = load_model()
    df = pd.read_csv("data/cleaned_transactions.csv")
    # Mapped to match model expectations
    df = df.rename(columns={"Class": "Is_Fraud"})

    X = df.drop(columns=["Is_Fraud"])
    y = df["Is_Fraud"]

    # Confusion matrix
    st.write("#### Confusion Matrix")
    y_pred = model.predict(X)
    cm = confusion_matrix(y, y_pred)
    fig, ax = plt.subplots()
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", ax=ax)
    st.pyplot(fig)

    # ROC curve
    st.write("#### ROC Curve")
    y_proba = model.predict_proba(X)[:, 1]
    fpr, tpr, _ = roc_curve(y, y_proba)
    roc_auc = auc(fpr, tpr)
    fig, ax = plt.subplots()
    ax.plot(fpr, tpr, label=f"ROC Curve (AUC = {roc_auc:.2f})")
    ax.set_xlabel("False Positive Rate")
    ax.set_ylabel("True Positive Rate")
    ax.legend()
    st.pyplot(fig)
