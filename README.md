# 🎾 Tennis Weather Bot

**Tennis Weather Bot** is a Telegram bot that helps you find the best time to play tennis outdoors during the week. It checks hourly weather forecasts for your location and suggests time slots with comfortable conditions.

👉 Try it here: [@tennis_weather_bot](https://t.me/tennis_weather_bot)

---

## 💡 Features

- Forecasts hourly weather for the next 7 days
- Finds suitable outdoor tennis windows between **6:00 and 21:00**
- Conditions considered:
  - 🌡 Temperature: **15–30°C**
  - 💧 Precipitation: **less than 0.4 mm**
  - 🌬 Wind speed: **under 6 m/s**
- Groups consecutive good hours into time intervals, like `13:00 — 15:00`
- Works via location sharing (from phone)

---

## 🚀 How to Use

1. Open Telegram
2. Start the bot: [@tennis_weather_bot](https://t.me/weather_for_tennis_bot)
3. Send `/start`
4. Share your **location**
5. The bot will reply with the best hours to play tennis 🎾

---

## ⚙️ Local Setup

```bash
git clone https://github.com/yourusername/tennis-weather-bot.git
cd tennis-weather-bot
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
