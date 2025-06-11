import gradio as gr
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Load model
model = joblib.load("model/modelo_et_1.pkl")

# Placeholder for preprocessing if needed
def preprocess(df):
    # Modify this to match your actual pipeline
    return df

# Predict function
def predict_readmission(file):
    df = pd.read_csv(file.name)
    df_processed = preprocess(df)
    risks = model.predict_proba(df_processed)[:, 1]
    labels = (risks > 0.5).astype(int)
    df["readmission_risk"] = risks
    df["prediction_label"] = labels

    # Optional: Plot ICU risk summary
    fig, ax = plt.subplots()
    ax.hist(risks, bins=10, color='skyblue')
    ax.set_title("Distribution of Readmission Risk")
    ax.set_xlabel("Risk Score")
    ax.set_ylabel("Number of Patients")

    return df[["readmission_risk", "prediction_label"]], fig

# Gradio app
with gr.Blocks() as demo:
    gr.Markdown("# 🧠 ICU Readmission Risk Predictor\nModel trained on MIMIC-IV cohort for intracerebral hemorrhage (ICH) patients.")
    gr.Markdown("Upload your CSV file to get risk predictions and a risk distribution plot.")
    
    file_input = gr.File(label="Upload CSV")
    output_df = gr.Dataframe(label="Predictions")
    output_plot = gr.Plot(label="Risk Distribution")

    file_input.change(fn=predict_readmission, inputs=file_input, outputs=[output_df, output_plot])

demo.launch()
