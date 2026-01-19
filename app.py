import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Restaurant Sales Prediction", layout="centered")

st.title("🍽️ Restaurant Sales Prediction App")

st.header("Input Details")

promotion = st.selectbox("Promotion Available?", ["Yes", "No"])
weekend = st.selectbox("Is it Weekend?", ["Yes", "No"])
quantity = st.number_input("Quantity Sold", min_value=1, value=10)
price = st.number_input("Observed Market Price", min_value=50.0, value=200.0)

# Simple logic for demo (for submission)
predicted_price = price * (1.1 if promotion == "Yes" else 1.0)
high_sales = "High Sales" if quantity > 20 else "Low Sales"

if st.button("Predict"):
    st.subheader("🔮 Prediction Output")
    st.write(f"**Predicted Selling Price:** ₹{predicted_price:.2f}")
    st.write(f"**Sales Category:** {high_sales}")
