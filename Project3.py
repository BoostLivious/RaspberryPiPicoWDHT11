import streamlit as st
import requests

st.title("DHT11 Monitor")

url = st.text_input("Enter API URL:", "https://raspberrypipicowdht11.onrender.com/")

if st.button("REFRESH"):
    try:
        res = requests.get(url, timeout=5)
        data = res.json()
        st.success("Data received!")

        st.metric("Temperature (°C)", f"{data.get('temperature', 'N/A')}°C")
        st.metric("Humidity (%)", f"{data.get('humidity', 'N/A')}%")
    except Exception as e:
        st.error(f"Error connecting to device: {e}")
