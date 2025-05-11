import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc

# Set page configuration
st.set_page_config(page_title="Clinical Risk Prediction App", layout="wide")

# Load model, scaler, and feature names
model = joblib.load('rf_model.joblib')
scaler = joblib.load('scaler.joblib')
with open('feature_names.txt', 'r') as f:
    feature_names = f.read().split(',')

# App title
st.title("Clinical Risk Prediction App")
st.write("Predict hospital readmission risk using clinical variables.")

# Sidebar for navigation
st.sidebar.header("Navigation")
app_mode = st.sidebar.selectbox("Choose mode", ["Individual Prediction", "Bulk Prediction"])

# Individual Prediction
if app_mode == "Individual Prediction":
    st.header("Enter Clinical Variables")
    
    # Create input fields for clinical variables
    input_data = {}
    for feature in feature_names:
        # Use number_input for numeric features, adjust min/max as needed
        input_data[feature] = st.number_input(f"{feature}", min_value=-1000.0, max_value=1000.0, value=0.0, step=0.1)
    
    # Predict button
    if st.button("Predict"):
        # Prepare input data
        input_df = pd.DataFrame([input_data])
        input_scaled = scaler.transform(input_df[feature_names])
        
        # Make prediction
        risk_score = model.predict_proba(input_scaled)[0, 1]
        prediction = model.predict(input_scaled)[0]
        
        # Display results
        st.subheader("Prediction Results")
        st.write(f"**Risk Score (Probability of Readmission):** {risk_score:.2%}")
        st.write(f"**Prediction:** {'Readmitted' if prediction == 1 else 'Not Readmitted'}")

# Bulk Prediction
elif app_mode == "Bulk Prediction":
    st.header("Upload CSV for Bulk Predictions")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file is not None:
        # Read CSV
        df_input = pd.read_csv(uploaded_file)
        
        # Validate CSV
        missing_cols = [col for col in feature_names if col not in df_input.columns]
        if missing_cols:
            st.error(f"CSV missing required columns: {', '.join(missing_cols)}")
        else:
            # Scale features
            input_scaled = scaler.transform(df_input[feature_names])
            
            # Make predictions
            df_input['Risk_Score'] = model.predict_proba(input_scaled)[:, 1]
            df_input['Prediction'] = model.predict(input_scaled)
            df_input['Prediction'] = df_input['Prediction'].map({1: 'Readmitted', 0: 'Not Readmitted'})
            
            # Display results
            st.subheader("Bulk Prediction Results")
            st.dataframe(df_input)
            
            # Download results
            csv = df_input.to_csv(index=False)
            st.download_button("Download Results", csv, "predictions.csv", "text/csv")

# ROC Curve
st.header("Model Performance: ROC Curve")
# Generate ROC curve using a train-test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    scaler.transform(df[feature_names]), df['readmitted'], test_size=0.2, random_state=42, stratify=df['readmitted']
)
y_scores = model.predict_proba(X_test)[:, 1]
fpr, tpr, _ = roc_curve(y_test, y_scores)
roc_auc = auc(fpr, tpr)

# Plot ROC curve
fig, ax = plt.subplots()
ax.plot(fpr, tpr, label=f'ROC curve (AUC = {roc_auc:.2f})')
ax.plot([0, 1], [0, 1], 'k--')
ax.set_xlim([0.0, 1.0])
ax.set_ylim([0.0, 1.05])
ax.set_xlabel('False Positive Rate')
ax.set_ylabel('True Positive Rate')
ax.set_title('Receiver Operating Characteristic')
ax.legend(loc="lower right")
st.pyplot(fig)

# Instructions
st.write("""
### Instructions
- **Individual Prediction**: Enter values for each clinical variable and click "Predict" to see the risk score and readmission prediction.
- **Bulk Prediction**: Upload a CSV with columns matching the clinical variables. The app will add risk scores and predictions.
- **CSV Format**: Ensure the CSV has columns: {', '.join(feature_names)}.
- **ROC Curve**: Shows model performance with the Area Under the Curve (AUC).
""")