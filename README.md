# 🌦️ WeatherNow – Live Weather Application

WeatherNow is a lightweight and interactive weather application built using **Streamlit**.  
It provides real-time weather information and a 5-day forecast for any location worldwide using the **OpenWeatherMap API**.

---

## 🚀 Features

- 📍 Detects current location using IP address
- 🌡️ Displays real-time temperature
- 💧 Shows humidity levels
- 🌬️ Wind speed information
- 🌤️ Weather conditions with official icons
- 🔮 5-Day weather forecast
- 🎨 Simple and clean Streamlit interface

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **Requests**
- **Geocoder**
- **OpenWeatherMap API**

---

## 📂 Project Structure

WeatherNow/

│

├── app.py # Main Streamlit application

├── README.md # Project documentation

└── .gitignore # Ignored files


---

## 📦 Installation & Dependencies

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/your-repository-name.git
cd your-repository-name
pip install streamlit requests geocoder


🔑 API Setup

Visit: https://openweathermap.org/

Create a free account

Generate your API key

Open app.py

Replace:

API_KEY = "your weather api key"


▶️ Running the Application

Inside the project folder, run:

streamlit run app.py


The app will open automatically in your browser.

🌍 How It Works

Uses OpenWeatherMap's weather endpoint for real-time data

Uses forecast endpoint for 5-day predictions

Displays weather icons dynamically

Uses IP-based geolocation for automatic city detection

🔮 Future Improvements

Add hourly forecast visualization

Add temperature trend charts

Add dark/light theme toggle

Store API key using environment variables

Deploy to Streamlit Cloud or AWS

📄 License

This project is created for educational and demonstration purposes.


---

After pasting:

```bash
git add README.md
git commit -m "Added professional README"
git push
