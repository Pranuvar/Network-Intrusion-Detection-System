# 🛡️ Network Intrusion Detection System

> **MSc AI Thesis — National College of Ireland, 2025**
> Real-time network attack detection using a hybrid CNN-LSTM deep learning architecture.

---

## The Problem

Network intrusion detection is a critical cybersecurity challenge. Traditional signature-based systems miss novel attacks, and rule-based approaches don't scale. The goal of this project was to build a machine learning system capable of detecting multiple attack types — DDoS, Botnet, and Brute Force — in real time, with high precision and minimal false positives.

---

## Key Results

| Metric | Value |
|---|---|
| **F1-Score** | 98.2% |
| **Dataset** | CIC-IDS2017 (2.8M+ records) |
| **Attack types detected** | DDoS · Botnet · Brute Force |
| **Detection mode** | Real-time |
| **Class imbalance handling** | SMOTE oversampling |

---

## Architecture

```
Raw Network Traffic
       ↓
Data Ingestion Pipeline (Python/Pandas)
       ↓
Feature Engineering (78 network flow features)
       ↓
SMOTE — Class Imbalance Correction
       ↓
Hybrid CNN-LSTM Model (TensorFlow/Keras)
  ├── CNN layers → spatial pattern extraction
  └── LSTM layers → temporal sequence modelling
       ↓
Classification Output (Benign / Attack type)
       ↓
Real-time Streamlit Monitoring Dashboard
```

---

## Tech Stack

| Layer | Tools |
|---|---|
| Language | Python 3.10 |
| Deep Learning | TensorFlow 2.x · Keras |
| Data Processing | Pandas · NumPy · Scikit-learn |
| Class Balancing | imbalanced-learn (SMOTE) |
| Dashboard | Streamlit |
| Containerisation | Docker |
| Version Control | Git |

---

## Dataset

**CIC-IDS2017** — Canadian Institute for Cybersecurity Intrusion Detection dataset.

- 2.8M+ labelled network flow records
- 78 traffic features per record
- Covers: BENIGN, DoS, DDoS, PortScan, Bot, Brute Force, Web Attack, Infiltration
- Severe class imbalance addressed with SMOTE

---

## How to Run

### Prerequisites
- Python 3.9+
- Docker (optional, recommended)

### Option 1 — Docker (recommended)

```bash
git clone https://github.com/Pranuvar/network-intrusion-detection.git
cd network-intrusion-detection
docker build -t intrusion-detection .
docker run -p 8501:8501 intrusion-detection
```

Open `http://localhost:8501` in your browser.

### Option 2 — Local Python

```bash
git clone https://github.com/Pranuvar/network-intrusion-detection.git
cd network-intrusion-detection

pip install -r requirements.txt

# Download dataset and place in /data
# Train the model
python src/train.py

# Launch the dashboard
streamlit run src/dashboard.py
```

---

## Project Structure

```
network-intrusion-detection/
├── data/               # CIC-IDS2017 dataset (not included — see below)
├── notebooks/          # Exploratory data analysis
├── src/
│   ├── ingest.py       # Data ingestion and preprocessing
│   ├── features.py     # Feature engineering
│   ├── model.py        # CNN-LSTM architecture
│   ├── train.py        # Training pipeline
│   └── dashboard.py    # Streamlit real-time dashboard
├── models/             # Saved model weights
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## Model Design Rationale

The hybrid CNN-LSTM architecture was chosen deliberately:

- **CNN layers** extract local spatial patterns from feature windows — effective at capturing correlations between network flow attributes at a point in time.
- **LSTM layers** model temporal dependencies — crucial for detecting attacks that unfold across sequences of packets (e.g., slow DDoS, Botnet C&C cycles).
- **SMOTE** was applied only to the training set to prevent data leakage during evaluation.

---

## Dataset Access

The CIC-IDS2017 dataset is publicly available from the [Canadian Institute for Cybersecurity](https://www.unb.ca/cic/datasets/ids-2017.html). Due to its size (~6GB), it is not included in this repository.

---

## Author

**Praneeth Varma Danthuluri**
MSc Artificial Intelligence — National College of Ireland
[LinkedIn](https://linkedin.com/in/praneeth-varma-danthuluri) · [Portfolio](https://Pranuvar.github.io)
