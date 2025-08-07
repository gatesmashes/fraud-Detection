import streamlit as st
import numpy as np
import joblib

# Load the trained model and scaler
model = joblib.load("fraud_model.pkl")
scaler = joblib.load("fraud_scaler.pkl")

# App title
st.title("💳 Credit Card Fraud Detection App")
st.write("Enter the transaction details to check if it's fraudulent:")

# --- Collect Input from User ---

# 1. Time input
time = st.number_input("Time", value=0.0)

# 2. V1 to V28 features
v_features = []
for i in range(1, 29):
    value = st.number_input(f"V{i}", value=0.0)
    v_features.append(value)

# 3. Amount input
amount = st.number_input("Amount", value=0.0)

# Combine all features into a single array
input_data = [time] + v_features + [amount]  # Total 30 features
input_array = np.array(input_data).reshape(1, -1)

# --- Make Prediction ---
if st.button("Detect Fraud"):
    try:
        # Scale input and predict
        scaled_input = scaler.transform(input_array)
        prediction = model.predict(scaled_input)

        # Show result
        if prediction[0] == 1:
            st.error("🚨 Fraudulent Transaction Detected!")
        else:
            st.success("✅ Legitimate Transaction")

    except Exception as e:
        st.error(f"Something went wrong: {e}")
