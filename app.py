import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load the trained model and scaler
model = pickle.load(open('models/modelForPrediction.pkl', 'rb'))
scaler = pickle.load(open('models/standardScaler.pkl', 'rb'))

# Custom CSS for styling
st.markdown("""
<style>
    .reportview-container {
        background-color: #f0f2f6;
    }
    .main {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    h1 {
        color: #007bff;
    }
    .stButton>button {
        background-color: #007bff;
        color: white;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# Streamlit UI
st.title("Diabetes Risk Assessment Tool")
st.write("Provide your health metrics below to assess your risk of diabetes.")

# Define feature names
feature_names = ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", 
                 "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"]

# Input fields arranged in two columns
col1, col2 = st.columns(2)

with col1:
    pregnancies = st.number_input("🤰 Pregnancies", min_value=0, max_value=20, value=0, help="Number of times pregnant")
    glucose = st.number_input("🍬 Glucose", min_value=0, max_value=300, value=100, help="Fasting blood sugar level (mg/dL)")
    blood_pressure = st.number_input("🩸 Blood Pressure", min_value=0, max_value=200, value=80, help="Diastolic blood pressure (mm Hg)")
    skin_thickness = st.number_input("📏 Skin Thickness", min_value=0, max_value=100, value=20, help="Triceps skin fold thickness (mm)")

with col2:
    insulin = st.number_input("💉 Insulin", min_value=0, max_value=1000, value=80, help="2-Hour serum insulin (mu U/ml)")
    bmi = st.number_input("⚖️ BMI", min_value=0.0, max_value=100.0, value=25.0, format="%.1f", help="Body Mass Index")
    diabetes_pedigree_function = st.number_input("🧬 Diabetes Pedigree Function", min_value=0.0, max_value=2.5, value=0.5, format="%.2f", help="Diabetes pedigree function")
    age = st.number_input("🎂 Age", min_value=0, max_value=120, value=30, help="Age in years")

# Predict button
if st.button("Predict"):
    # Collect input data as a DataFrame
    input_data = pd.DataFrame([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]], 
                              columns=feature_names)
    
    # Scale the input data
    scaled_data = scaler.transform(input_data)
    
    # Make prediction and get probability
    prediction_prob = model.predict_proba(scaled_data)[0][1]  # Probability of being diabetic
    
    # Display result based on probability
    if prediction_prob < 0.3:
        st.success(f"Low risk of diabetes ({prediction_prob:.2%} probability). Keep maintaining a healthy lifestyle!")
    elif prediction_prob < 0.7:
        st.warning(f"Medium risk of diabetes ({prediction_prob:.2%} probability). Consider consulting a doctor.")
    else:
        st.error(f"High risk of diabetes ({prediction_prob:.2%} probability). Please consult a doctor immediately.")

# Disclaimer
st.markdown("**Disclaimer:** This tool is for informational purposes only and should not be used as a substitute for professional medical advice.")