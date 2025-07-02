import streamlit as st
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open('heart_model.pkl', 'rb'))

st.title('❤️ Heart Disease Prediction')
st.write("This app predicts whether a person is likely to have heart disease based on input features.")

# User input fields
age = st.number_input("Age", 18, 100)
sex = st.selectbox("Sex", ["Male", "Female"])
cp = st.selectbox("Chest Pain Type", [0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure", 80, 200)
chol = st.number_input("Serum Cholesterol (mg/dl)", 100, 600)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["Yes", "No"])
restecg = st.selectbox("Resting ECG Results", [0, 1, 2])
thalach = st.number_input("Max Heart Rate Achieved", 60, 220)
exang = st.selectbox("Exercise Induced Angina", ["Yes", "No"])
oldpeak = st.number_input("ST depression", 0.0, 10.0, step=0.1)
slope = st.selectbox("Slope of the ST segment", [0, 1, 2])
ca = st.selectbox("Major vessels colored by fluoroscopy (0–3)", [0, 1, 2, 3])
thal = st.selectbox("Thalassemia", [0, 1, 2, 3])

# Convert categorical to numeric
sex = 1 if sex == "Male" else 0
fbs = 1 if fbs == "Yes" else 0
exang = 1 if exang == "Yes" else 0

# Prediction
if st.button("Predict"):
    input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg,
                            thalach, exang, oldpeak, slope, ca, thal]])
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.error("⚠️ High risk of heart disease.")
    else:
        st.success("✅ Low risk of heart disease.")

