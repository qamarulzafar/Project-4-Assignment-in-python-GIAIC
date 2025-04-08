import streamlit as st
import requests
from dotenv import load_dotenv
import os

load_dotenv()

st.title("☁️ Weather App")

# User input
city = st.text_input("Enter city name:")

# API call
if st.button("Get Weather"):
    if city:
        api_key = os.getenv("OPENWEATHERMAP_API_KEY")
        if not api_key:
            st.error("Please set the OPENWEATHERMAP_API_KEY environment variable.")
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            temp = data['main']['temp']
            condition = data['weather'][0]['description']
            humidity = data['main']['humidity']
            wind = data['wind']['speed']
            
            st.success(f"🌡 Temperature: {temp}°C")
            st.info(f"🌤 Condition: {condition.title()}")
            st.warning(f"💧 Humidity: {humidity}%")
            st.write(f"💨 Wind Speed: {wind} m/s")
        else:
            st.error("City not found. Please enter a valid city name.")
