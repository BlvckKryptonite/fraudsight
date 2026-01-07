# FraudSight Risk Analyzer <img align="center" src="assets/logo.png" alt="Fraudsight Logo" height="50">

![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=matplotlib&logoColor=white)
![Heroku](https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
---

## 📌 Project Overview

**FraudSight Risk Analyzer** is a predictive analytics web application designed to identify potentially fraudulent financial transactions using machine learning and interactive data visualisation.

The application combines exploratory data analysis, supervised machine learning, and a Streamlit-based dashboard to support fraud detection, investigation, and performance evaluation. While the deployed version demonstrates core functionality using a representative sample dataset, the full model and dataset are intended to be run locally due to platform upload and memory constraints.

---

## 📖 Table of Contents

- [Dataset Content](#dataset-content)
- [Business Requirements](#business-requirements)
- [Hypotheses and Validation](#hypotheses-and-validation)
- [Rationale for Data Visualisations and ML Tasks](#rationale-for-data-visualisations-and-ml-tasks)
- [Machine Learning Business Case](#machine-learning-business-case)
- [Dashboard Design](#dashboard-design)
- [Development Notes & Technical Decisions](#development-notes--technical-decisions)
- [Unfixed Bugs & Known Limitations](#unfixed-bugs--known-limitations)
- [Deployment](#deployment)
- [Main Data Analysis & ML Libraries](#main-data-analysis--ml-libraries)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

---

## 📊 Dataset Content

### Source

The dataset used in this project is the [Kaggle Credit Card Fraud Detection Dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud).

This dataset contains anonymised credit card transactions and is highly imbalanced, making it well-suited for fraud detection tasks.

### Variables

| Variable        | Description                                                     | Example Values        |
|-----------------|-----------------------------------------------------------------|-----------------------|
| `Time`          | Seconds elapsed between this transaction and the first one      | `12345`               |
| `Amount`        | Transaction amount                                              | `2.99`, `149.99`      |
| `V1–V28`        | Anonymised PCA-transformed features  (from original dataset)                            | Continuous values     |
| `Class` / `Is_Fraud` | Fraud label (0 = Legitimate, 1 = Fraud)                    | `0`, `1`              |


> **Note:** During preprocessing, the target variable was standardised to `Is_Fraud` for clarity and consistency across notebooks and application code.

---

## 🎯 Business Requirements

### Stakeholders

- Financial analysts
- Risk management teams
- Compliance and fraud investigation teams

### Core Requirements

---

| Requirement            | Description                                              |
|------------------------|----------------------------------------------------------|
| **Visual Analysis**    | Identify trends and patterns in fraudulent transactions  |
| **Predictive Modelling** | Classify transactions as fraudulent or legitimate        |
| **Decision Support**   | Highlight high-risk transactions for further review      |


## 🔬 Hypotheses and Validation

### Hypotheses

1. Fraudulent transactions are more likely to occur outside standard business hours
2. High-value transactions are disproportionately associated with fraud

### Validation Methods

- Time-based aggregation and fraud rate comparison
- Distribution analysis of transaction amounts by fraud label

### Conclusions

| Hypothesis     | Result                                                                 |
|----------------|------------------------------------------------------------------------|
| **Hypothesis 1** | ✅ Confirmed — fraud rates increase outside typical business hours     |
| **Hypothesis 2** | ✅ Confirmed — higher transaction values show elevated fraud risk      |


---

## 📈 Rationale for Data Visualisations and ML Tasks

| Business Requirement      | Visualisation / ML Task        | Tools                 |
|---------------------------|-------------------------------|-----------------------|
| Fraud trend analysis      | Time-series plots              | Matplotlib, Seaborn   |
| Fraud classification      | Random Forest pipeline         | Scikit-learn          |
| Risk inspection            | Interactive tables             | Streamlit, Pandas     |


---

## 🤖 Machine Learning Business Case

### Aim

Reduce financial losses by flagging potentially fraudulent transactions early.

### Model Choice

A **Random Forest classifier** was selected due to:

- Robustness to noisy and imbalanced data
- Strong baseline performance without excessive feature engineering
- Interpretability compared to more opaque models

### Success Metrics

- Recall prioritised to minimise false negatives
- Balanced performance evaluated using cross-validation

### Output

- Binary fraud prediction
- Fraud probability score

---

## 🧭 Dashboard Design

### Pages

| Page              | Description                                                     |
|-------------------|-----------------------------------------------------------------|
| **Project Summary** | Overview of objectives, dataset, and project scope             |
| **Fraud Visualizer** | Exploratory plots showing fraud trends and distributions       |
| **Fraud Detector**  | CSV upload for transaction-level fraud prediction              |
| **Model Performance** | Evaluation metrics, confusion matrix, and diagnostics       |


### Widgets

- File uploader for CSV input
- Interactive tables and visual outputs

---

## 🛠️ Development Notes & Technical Decisions

### Why so many pull requests?

Early in development, large dataset handling caused repeated deployment and environment issues. To avoid destabilising the main branch, a separate `fixes` branch was used for debugging and recovery work, then merged incrementally.

> This mirrors real-world engineering practice and helped preserve project integrity.

### Model Tuning vs Diploma Scope

Significant time was initially spent tuning hyperparameters via `GridSearchCV`. While effective locally, this proved excessive for a diploma-level deployment environment.

As a result:

- Parameter grids were reduced for production
- A stable, performant configuration was prioritised over exhaustive optimisation

> This distinction between local experimentation and production constraints is intentional and documented.

### Debug Print Statements in Notebooks

Although typically avoided in production code, print statements were retained in selected notebooks (e.g., model training) to support:

- Transparent debugging
- Easier future iteration and retraining
- Clear execution checkpoints during long-running processes

> Given the complexity of the dataset and training pipeline, this decision prioritised maintainability.

---

## 🐞 Unfixed Bugs & Known Limitations

| Issue                     | Description                                                                                                  |
|---------------------------|--------------------------------------------------------------------------------------------------------------|
| **Deployment Upload Limits** | Large CSV uploads (including small samples) may fail on the deployed app due to platform constraints. The Fraud Detector works reliably when run locally with the full dataset. |
| **Class Imbalance Sensitivity** | Very small transaction amounts may show reduced predictive reliability due to class imbalance.        |


---

## 🚀 Deployment

### Live Application

Deployed via Heroku (or equivalent platform). Due to platform constraints, the deployed version uses a representative sample dataset for demonstration.

### Local Setup (Recommended for Full Functionality)

    
    git clone https://github.com/BlvckKryptonite/fraudsight-risk-analyzer.git
    cd fraudsight-risk-analyzer
    pip install -r requirements.txt
    streamlit run src/app.py
    

> ⚠️ **Important**: To run the full fraud detection workflow, download the full dataset locally and ensure it is named according to the README instructions.

---

## 📚 Main Data Analysis & ML Libraries

| Library               | Usage                              |
|-----------------------|------------------------------------|
| Pandas                | Data manipulation and analysis     |
| Scikit-learn          | Machine learning & evaluation      |
| Matplotlib / Seaborn  | Data visualisation                 |
| Streamlit             | Interactive dashboard UI           |
| Joblib / Pickle       | Model persistence                  |


---

## 📎 Credits

- **Dataset**: [Kaggle Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- **Documentation**: [Scikit-learn](https://scikit-learn.org/) & [Streamlit](https://docs.streamlit.io/)


## 🙏 Acknowledgements

Special thanks to mentors, peers, and reviewers whose feedback helped shape this project.

This project represents both a technical and learning milestone within the programme.

---

## ✅ Final Note for Assessors

> The deployed application demonstrates core functionality using a representative dataset.
> The full analytical and predictive workflow is available locally and documented thoroughly to reflect real-world constraints, decision-making, and engineering trade-offs.
