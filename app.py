import streamlit as st
import pandas as pd
import pickle

# Load model and feature names
model_data = pickle.load(open("rainfall_prediction_model.pkl", "rb"))
model = model_data["model"]
feature_names = model_data["feature_names"]

st.title("🌧️ Rainfall Prediction System")
st.write("Enter the values below to predict rainfall.")

# Input fields (must match model training features)
pressure = st.number_input("Pressure (hPa)", value=1015.0)
dewpoint = st.number_input("Dew Point (°C)", value=20.0)
humidity = st.number_input("Humidity (%)", value=70.0)
cloud = st.number_input("Cloud Cover (%)", value=50.0)
sunshine = st.number_input("Sunshine (hours)", value=5.0)
winddirection = st.number_input("Wind Direction (°)", value=90.0)
windspeed = st.number_input("Wind Speed (km/h)", value=10.0)

if st.button("Predict"):
    # Build input in correct order
    input_df = pd.DataFrame([[
        pressure, dewpoint, humidity, cloud, sunshine, winddirection, windspeed
    ]], columns=feature_names)

    # Make prediction
    prediction = model.predict(input_df)[0]

    # Display result
    if prediction == 1:
        st.success("🌧️ Rainfall Expected!")
    else:
        st.info("☀️ No Rainfall Expected.")
