import streamlit as st
import requests
import geocoder
from datetime import datetime

API_KEY = "your  weather api key"
BASE_URL = "https://api.openweathermap.org/data/2.5/"

def get_weather(city):
    url = f"{BASE_URL}weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

def get_forecast(city):
    url = f"{BASE_URL}forecast?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

def get_location_by_ip():
    g = geocoder.ip('me')
    return g.city if g.city else None


st.set_page_config(page_title="WeatherNow", page_icon="☁️", layout="centered")

st.title("🌦️ WeatherNow")
st.write("Get live weather info for any location")


if st.button("📍 Use My Current Location"):
    location = get_location_by_ip()
    if location:
        st.success(f"Detected location: {location}")
    else:
        st.error("Couldn't detect your location.")
else:
    location = st.text_input("Enter City / Zip Code / Landmark:")

if location:
    data = get_weather(location)
    if data.get("cod") != 200:
        st.error("City not found. Try again.")
    else:
        city = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"].title()
        icon = data["weather"][0]["icon"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]

        st.subheader(f"📍 {city}, {country}")
        st.image(f"http://openweathermap.org/img/wn/{icon}@2x.png")
        st.write(f"**🌡️ Temperature:** {temp}°C")
        st.write(f"**💧 Humidity:** {humidity}%")
        st.write(f"**🌬️ Wind Speed:** {wind} m/s")
        st.write(f"**🌤️ Condition:** {desc}")

       
        forecast_data = get_forecast(location)
        st.markdown("### 🔮 5-Day Forecast")
        for i in range(0, len(forecast_data["list"]), 8):
            day = forecast_data["list"][i]
            date = datetime.fromtimestamp(day["dt"]).strftime("%a %d %b")
            temp = day["main"]["temp"]
            desc = day["weather"][0]["description"].title()
            icon = day["weather"][0]["icon"]
            st.write(f"{date}: {temp}°C, {desc}")
            st.image(f"http://openweathermap.org/img/wn/{icon}.png", width=50)
