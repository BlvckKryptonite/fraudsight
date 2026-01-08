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

    # Safeguard to prevent potential future corruption 😮‍💨
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Model not found at {MODEL_PATH}")

    if MODEL_PATH.stat().st_size < 10_000:
        raise ValueError("Model file looks corrupted (too small)")

    with open(MODEL_PATH, "rb") as f:
        return pickle.load(f)


def app():
    st.title("Model Performance")
    st.info("""
    This page evaluates how well the fraud detection model performs on
             historical transaction data.

    - **Confusion Matrix:** Shows how many transactions were correctly and
             incorrectly classified,
      highlighting false positives and false negatives.
    - **ROC Curve & AUC:** Illustrates the model’s ability to distinguish
      between fraudulent and legitimate transactions across different
             thresholds.

    In fraud detection, **recall is prioritised** to minimise missed
             fraudulent transactions,
    even if this results in some false positives. These metrics support model
             validation
    and risk-based decision-making.
    """)

    model = load_model()

    # Resolve data path relative to the project root
    # to avoid working-directory issues
    BASE_DIR = Path(__file__).resolve().parents[2]
    DATA_PATH = BASE_DIR / "data" / "sample_cleaned_transactions.csv"
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Data not found at {DATA_PATH}")

    df = pd.read_csv(DATA_PATH)
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
    # Some estimators don't implement predict_proba; fall back to
    # decision_function and scale to [0,1]
    if hasattr(model, "predict_proba"):
        y_proba = model.predict_proba(X)[:, 1]
    elif hasattr(model, "decision_function"):
        scores = model.decision_function(X)
        from sklearn.preprocessing import minmax_scale
        y_proba = minmax_scale(scores)
    else:
        st.error(
            "Model does not support predict_proba or "
            "decision_function; cannot compute ROC."
        )
        return

    fpr, tpr, _ = roc_curve(y, y_proba)
    roc_auc = auc(fpr, tpr)
    fig, ax = plt.subplots()
    ax.plot(fpr, tpr, label=f"ROC Curve (AUC = {roc_auc:.2f})")
    ax.set_xlabel("False Positive Rate")
    ax.set_ylabel("True Positive Rate")
    ax.legend()
    st.pyplot(fig)
