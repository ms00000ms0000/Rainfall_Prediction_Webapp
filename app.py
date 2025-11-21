import streamlit as st
import numpy as np
import pickle

# Load model
model = pickle.load(open("rainfall_prediction_model.pkl", "rb"))

st.title("🌧️ Rainfall Prediction System")
st.write("Enter the values below to predict rainfall.")

temperature = st.number_input("Temperature (°C)", value=30.0)
humidity = st.number_input("Humidity (%)", value=60.0)
pressure = st.number_input("Pressure (hPa)", value=1000.0)
maxtemp = st.number_input("Max Temperature (°C)", value=35.0)
mintemp = st.number_input("Min Temperature (°C)", value=25.0)
windspeed = st.number_input("Wind Speed (km/h)", value=10.0)

if st.button("Predict"):
    input_data = np.array([[temperature, humidity, pressure, maxtemp, mintemp, windspeed]])
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("🌧️ Rainfall Expected!")
    else:
        st.info("☀️ No Rainfall Expected.")
