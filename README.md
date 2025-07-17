# 🎾 Telegram Bot — Time and location for Tennis

A simple Telegram bot that helps you find the best time to play tennis outdoors based on hourly weather forecasts and locate nearby tennis courts.

---

## 🔧 Features

- ⛅ **Analyzes hourly weather** (Open-Meteo API)
- 🕒 Suggests best time windows for tennis (6:00 to 21:00)
- 🎯 Weather conditions:
  - Temperature: 15–30°C (ideal), 13–32°C (acceptable)
  - Precipitation: < 0.4 mm (ideal), < 1.0 mm (acceptable)
  - Wind speed: < 6 m/s (ideal), < 7 m/s (acceptable)
- 📍 **Finds nearby tennis courts** using Foursquare Places API
- 🌍 Works globally — input your live geolocation

---

## 🚀 Try it on Telegram

👉 [@weather_for_tennis_bot](https://t.me/weather_for_tennis_bot)

---

## 📦 Project structure

## 🔧 Setup  
1. Clone the repo: `git clone https://github.com/TsykalanovDima/telegram-bot-time-for-tennis.git && cd telegram-bot-time-for-tennis`  
2. Create and activate a virtual environment: `python3 -m venv venv && source venv/bin/activate`  
3. Install dependencies: `pip install -r requirements.txt`  
4. Create a `.env` file and insert your tokens:  
5. Run the bot: `python bot.py`  
## 💡 Features  
⛅ Analyzes hourly weather (Open-Meteo API) | 🕒 Suggests best time slots from 6:00 to 21:00 | ✅ Ideal weather: 15–30°C, < 0.4 mm rain, < 6 m/s wind | ➖ Acceptable weather also supported | 📍 Finds nearby tennis courts via Foursquare | 🌍 Works globally with shared geolocation 
## 📁 Project Structure  
bot.py – Telegram bot logic | weather.py – Weather forecast analysis | foursquare.py – Tennis court search via Foursquare | config.py – Env loader | .env.example – Template for secrets | requirements.txt – Dependencies  
## 🌐 Deploy on Render
Create new Web Service 
## 📱 Example  
User: `/start` → shares 📍 location → bot replies with tennis weather + nearby courts  

