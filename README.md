# FraudSight Risk Analyzer <img align="center" src="assets/logo.png" alt="Fraudsight Logo" height="50">

![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=matplotlib&logoColor=white)
![Fly.io](https://img.shields.io/badge/Fly.io-8B5CF6?style=for-the-badge&logo=flydotio&logoColor=white)
![Heroku](https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
---

## 📌 Project Overview

**FraudSight Risk Analyzer** is a predictive analytics web application designed to identify potentially fraudulent financial transactions using machine learning and interactive data visualisation.

The application combines exploratory data analysis, supervised machine learning, and a Streamlit-based dashboard to support fraud detection, investigation, and performance evaluation. While the deployed version demonstrates core functionality using a representative sample dataset, the full model and dataset are intended to be run locally due to platform upload and memory constraints.

---

## 📖 Table of Contents

- [Dataset Content](#📊-dataset-content)
- [Business Requirements](#🎯-business-requirements)
- [Hypotheses and Validation](#🔬-hypotheses-and-validation)
- [Rationale for Data Visualisations and ML Tasks](#📈-rationale-for-data-visualisations-and-ml-tasks)
- [Machine Learning Business Case](#🤖-machine-learning-business-case)
- [Dashboard Design](#🧭-dashboard-design)
- [Development Notes & Technical Decisions](#🛠️-development-notes--technical-decisions)
- [Unfixed Bugs & Known Limitations](#🐞-unfixed-bugs--known-limitations)
- [Deployment](#🚀-deployment)
- [Main Data Analysis & ML Libraries](#📚-main-data-analysis--ml-libraries)
- [Credits](#📎-credits)
- [Acknowledgements](#🙏-acknowledgements)
- [Final Note for Assessors](#✅-final-note-for-assessors)

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

<br>

> **Note:** During preprocessing, the target variable was standardised to `Is_Fraud` for clarity and consistency across notebooks and application code.

---

<br>

## 🎯 Business Requirements

### Stakeholders

- Financial analysts
- Risk management teams
- Compliance and fraud investigation teams

<br>

### Core Requirements

---

| Requirement            | Description                                              |
|------------------------|----------------------------------------------------------|
| **Visual Analysis**    | Identify trends and patterns in fraudulent transactions  |
| **Predictive Modelling** | Classify transactions as fraudulent or legitimate        |
| **Decision Support**   | Highlight high-risk transactions for further review      |

<br>

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

<br>



## 📈 Rationale for Data Visualisations and ML Tasks

| Business Requirement      | Visualisation / ML Task        | Tools                 |
|---------------------------|-------------------------------|-----------------------|
| Fraud trend analysis      | Time-series plots              | Matplotlib, Seaborn   |
| Fraud classification      | Random Forest pipeline         | Scikit-learn          |
| Risk inspection            | Interactive tables             | Streamlit, Pandas     |


<br>

## 🤖 Machine Learning Business Case

### Aim:

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

<br>

## 🧭 Dashboard Design

### Pages:

| Page              | Description                                                     |
|-------------------|-----------------------------------------------------------------|
| **Project Summary** | Overview of objectives, dataset, and project scope             |
| **Fraud Visualizer** | Exploratory plots showing fraud trends and distributions       |
| **Fraud Detector**  | CSV upload for transaction-level fraud prediction              |
| **Model Performance** | Evaluation metrics, confusion matrix, and diagnostics       |


### Widgets:

- File uploader for CSV input
- Interactive tables and visual outputs

<br>

## 🛠️ Development Notes & Technical Decisions

### Why so many pull requests?

Early in development, large dataset handling caused repeated deployment and environment issues. To avoid destabilising the main branch, a separate `fixes` branch was used for debugging and recovery work, then merged incrementally.

> This mirrors real-world engineering practice and helped preserve project integrity.

<br>

### Model Tuning vs Diploma Scope

Significant time was initially spent tuning hyperparameters via `GridSearchCV`. While effective locally, this proved excessive for my deployment environment.

As a result:

- Parameter grids were reduced for production
- A stable, performant configuration was prioritised over exhaustive optimisation

> This distinction between local experimentation and production constraints is intentional and documented.

<br>

### Debug Print Statements in Notebooks

Although typically avoided in production code, print statements were retained in selected notebooks (e.g., model training) to support:

- Transparent debugging
- Easier future iteration and retraining
- Clear execution checkpoints during long-running processes

<br>

> Given the complexity of the dataset and training pipeline, as well as the challenges encountered due to differences between local and production environments, this decision prioritised stability, maintainability, and reproducibility of the application.

<br>

## 🐞 Unfixed Bugs & Known Limitations

| Issue                     | Description                                                                                                  |
|---------------------------|--------------------------------------------------------------------------------------------------------------|
| **Deployment Upload Limits** | Large CSV uploads may fail on the deployed app due to Fly.io memory constraints. The Fraud Detector works reliably when run locally with the full dataset. |
| **Class Imbalance Sensitivity** | Very small transaction amounts may show reduced predictive reliability due to class imbalance.        |
| **Model Performance Sampling** | The Model Performance page computes metrics on a 5,000-row sample rather than the full dataset to stay within memory limits on the deployed app. Results are representative but not exhaustive. |

<br>

## 🚀 Deployment

### Live Application

The app is live at **[https://fraudsight.fly.dev](https://fraudsight.fly.dev)**

Deployed on [Fly.io](https://fly.io). Due to platform memory constraints, the deployed version uses a representative sample dataset for demonstration. The full analytical workflow is available locally.

### Local Setup (Recommended for Full Functionality)

```bash
git clone https://github.com/BlvckKryptonite/fraudsight-risk-analyzer.git
cd fraudsight-risk-analyzer
pip install -r requirements.txt
streamlit run src/app.py
```

> ⚠️ **Important:** To run the full fraud detection workflow, download the complete dataset locally and place it in the `data` directory, replacing the representative sample.
> The file **must** be named exactly `sample_cleaned_transactions.csv`, as this filename is referenced consistently across the application and model pipeline.

<br>

### Migration to Fly.io

The app was originally deployed on Heroku and migrated to [Fly.io](https://fly.io) following Heroku's removal of its free tier. This was the most involved of the three migrations due to the app's data science stack and large dataset.

#### Why Fly.io?

Fly.io offers a generous free tier and Docker-based deployments that give full control over the runtime environment — important for a data science app with specific memory and dependency requirements.

#### Issues Encountered & How They Were Fixed

**1. Out of memory (OOM) crashes**

The app was repeatedly killed at startup with `Killed process (streamlit) — Out of memory`. Streamlit combined with pandas, scikit-learn, matplotlib, and seaborn consumes significant memory just from imports alone.

Fix: Scale the machine to 2048mb.
```bash
fly scale memory 2048
```

And update `fly.toml`:
```toml
[[vm]]
  memory = '2048mb'
  cpu_kind = 'shared'
  cpus = 1
```

**2. Model Performance page loading the full dataset on every visit**

`model_performance.py` was loading the entire 143MB CSV and running predictions on all rows without caching, causing repeated memory spikes.

Fix: Wrapped data loading and predictions in a `@st.cache_data` function and sampled 5,000 rows — more than sufficient for statistically meaningful confusion matrix and ROC curve outputs.

**3. 143MB CSV blocked by GitHub's file size limit**

The dataset had been committed to Git history, which blocked all pushes with `GH001: Large files detected`.

Fix: Purged the file from Git history entirely using `git filter-repo`:
```bash
git filter-repo --path data/sample_cleaned_transactions.csv --invert-paths --force
git remote add origin https://github.com/BlvckKryptonite/fraudsight.git
git push origin --force --all
```

The file is now excluded from Git via `.gitignore` but still baked into the Docker image at build time via the Dockerfile, so the deployed app can still access it.

**4. Slow deploys (600–800 second build context)**

The entire `data/` folder was being sent to the build server on every deploy, inflating the build context to over 800MB.

Fix: Added a `.dockerignore` to exclude unnecessary large files, keeping only `sample_cleaned_transactions.csv` since it is required at runtime.

**5. CSV not found at runtime**

After adding `.dockerignore`, `sample_cleaned_transactions.csv` was accidentally excluded, causing a `FileNotFoundError` at runtime.

Fix: Removed the file from `.dockerignore` and ensured `COPY data/ data/` appears before `COPY . .` in the Dockerfile so the data is available when the app starts.

#### Final Dockerfile

```dockerfile
FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY data/ data/
COPY . .

EXPOSE 8080

CMD ["streamlit", "run", "src/app.py", "--server.port=8080", "--server.address=0.0.0.0"]
```


<br>

## 🚀 Deployment

### Live Application

Deployed via Heroku (or equivalent platform). Due to platform constraints, the deployed version uses a representative sample dataset for demonstration.

### Local Setup (Recommended for Full Functionality)

    
    git clone https://github.com/BlvckKryptonite/fraudsight-risk-analyzer.git
    cd fraudsight-risk-analyzer
    pip install -r requirements.txt
    streamlit run src/app.py
    
<br>

> ⚠️ **Important:** To run the full fraud detection workflow, download the complete dataset locally and place it in the `data` directory, replacing the representative sample.
The file **must** be named exactly "`sample_cleaned_transactions.csv`", as this filename is referenced consistently across the application and model pipeline.

<br>

## 📚 Main Data Analysis & ML Libraries

| Library               | Usage                              |
|-----------------------|------------------------------------|
| Pandas                | Data manipulation and analysis     |
| Scikit-learn          | Machine learning & evaluation      |
| Matplotlib / Seaborn  | Data visualisation                 |
| Streamlit             | Interactive dashboard UI           |
| Joblib / Pickle       | Model persistence                  |


<br>

## 📎 Credits

- **Dataset**: [Kaggle Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- **Documentation**: [Scikit-learn](https://scikit-learn.org/) & [Streamlit](https://docs.streamlit.io/)

<br>

## 🙏 Acknowledgements

Special thanks to mentors, peers, and reviewers whose feedback helped shape this project.

This project represents both a technical and learning milestone within the programme.

<br>

## ✅ Final Note for Assessors

> The deployed application demonstrates core functionality using a representative dataset.
> The full analytical and predictive workflow is available locally and documented thoroughly to reflect real-world constraints, decision-making, and engineering trade-offs.
