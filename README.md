# 🍷 Wine Quality Prediction - End-to-End MLOps Project

An end-to-end Machine Learning Operations (MLOps) project for predicting wine quality using physicochemical properties of wine. This project demonstrates the complete ML lifecycle including data ingestion, preprocessing, model training, evaluation, experiment tracking, deployment, and production-ready application development.

---

## 🚀 Project Overview

This project focuses on building a scalable and production-ready machine learning pipeline for wine quality prediction. It covers:

* Data ingestion and validation
* Data transformation and preprocessing
* Model training and evaluation
* Experiment tracking using MLflow
* Modular pipeline architecture
* Flask-based web application
* CI/CD ready structure
* Docker support for deployment
* Reproducible ML workflows

The project follows MLOps best practices for maintainability, scalability, and deployment readiness. ([arXiv][1])

---

# 📌 Problem Statement

Wine quality prediction is a supervised machine learning problem where the model predicts wine quality based on various chemical properties such as:

* Fixed acidity
* Volatile acidity
* Citric acid
* Residual sugar
* Chlorides
* Alcohol content
* pH
* Sulphates

The goal is to automate wine quality assessment using machine learning techniques.

---

# 🏗️ Project Architecture

```text
Data Source
    ↓
Data Ingestion
    ↓
Data Validation
    ↓
Data Transformation
    ↓
Model Training
    ↓
Model Evaluation
    ↓
MLflow Tracking
    ↓
Model Deployment
    ↓
Flask Web Application
```

---

# 📂 Project Structure

```bash
wine-quality-mlops/
│
├── artifacts/                 # Generated artifacts
├── config/                    # Configuration files
├── src/                       # Source code
│   ├── components/            # Pipeline components
│   ├── pipeline/              # Training & prediction pipelines
│   ├── utils/                 # Utility functions
│   ├── entity/                # Config entities
│   └── configuration/         # Configuration manager
│
├── templates/                 # HTML templates
├── static/                    # CSS/JS files
├── research/                  # Jupyter notebooks
├── app.py                     # Flask application
├── main.py                    # Training pipeline entry point
├── params.yaml                # Model parameters
├── schema.yaml                # Data schema
├── requirements.txt           # Dependencies
├── Dockerfile                 # Docker configuration
└── README.md
```

---

# ⚙️ Tech Stack

## Machine Learning

* Python
* Scikit-learn
* Pandas
* NumPy

## MLOps & Deployment

* MLflow
* Flask
* Docker
* GitHub Actions (CI/CD Ready)

---

# 🔬 ML Pipeline Components

## 1. Data Ingestion

* Reads raw dataset
* Splits train/test data
* Stores artifacts

## 2. Data Validation

* Validates schema
* Checks missing values
* Ensures data consistency

## 3. Data Transformation

* Feature engineering
* Data preprocessing
* Scaling and transformation

## 4. Model Training

* Trains ML model
* Saves trained model artifacts

## 5. Model Evaluation

* Evaluates performance metrics
* Tracks experiments with MLflow

## 6. Prediction Pipeline

* Loads trained model
* Generates predictions from user input

---

# 📈 Experiment Tracking with MLflow

This project integrates MLflow for:

* Experiment tracking
* Parameter logging
* Metric logging
* Model versioning
* Artifact management

MLOps workflows with experiment tracking improve reproducibility and deployment reliability.

---

# 🐳 Docker Support

Build Docker image:

```bash
docker build -t wine-quality-mlops .
```

Run container:

```bash
docker run -p 5000:5000 wine-quality-mlops
```

---

# ▶️ Installation & Setup

## 1. Clone Repository

```bash
git clone https://github.com/Ingle-Santosh/wine-quality-mlops.git
cd wine-quality-mlops
```

## 2. Create Virtual Environment

```bash
conda create -n wine python=3.10 -y
conda activate wine
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🚀 Run Training Pipeline

```bash
python main.py
```

---

# 🌐 Run Flask Application

```bash
python app.py
```

Application will run on:

```text
http://localhost:5000
```

---

# 📌 Future Improvements

* Kubernetes deployment
* CI/CD automation using GitHub Actions
* Cloud deployment (AWS/Azure/GCP)
* Model monitoring and drift detection
* Automated retraining pipeline
* FastAPI integration
* LLM-powered data insights

---

# 🧠 Learning Outcomes

This project demonstrates:

* End-to-end ML project structure
* Production-grade ML pipeline design
* MLOps best practices
* Model deployment workflows
* Experiment tracking and reproducibility
* Scalable project architecture

---
