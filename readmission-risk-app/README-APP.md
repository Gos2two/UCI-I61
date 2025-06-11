# ICU Readmission Risk Predictor

This web app uses a machine learning model trained on the MIMIC-IV dataset (ICH cohort) to predict ICU readmission risk.

## 🧠 Model Info

- Data: MIMIC-IV, ICH-specific ICU patients
- Features: Vitals, labs, comorbidities (see notebook)
- Output: Risk score (0 to 1) and binary prediction (readmit or not)

## 🧪 How to Use

1. Upload a CSV file with the same structure as training data.
2. View predictions and readmission risk plot.

## ⚠️ Disclaimer

This tool is intended for academic/research purposes. It is **not** for clinical decision-making.
