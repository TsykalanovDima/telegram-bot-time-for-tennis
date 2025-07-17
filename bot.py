import os
from dotenv import load_dotenv
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)
from weather import get_tennis_windows
from flask import Flask
from threading import Thread

load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")


app = Flask(__name__)


@app.route('/')
def health_check():
    return "Tennis Bot is running! 🎾"


@app.route('/health')
def health():
    return {"status": "ok"}


def run_web_server():
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port, debug=False)


location_keyboard = ReplyKeyboardMarkup(
    [[KeyboardButton("📍 Send location", request_location=True)]],
    resize_keyboard=True
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hi! I'm your Tennis Weather Bot 🎾\nSend your location to get the best time slots.",
        reply_markup=location_keyboard
    )


async def handle_location(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lat = update.message.location.latitude
    lon = update.message.location.longitude
    result = get_tennis_windows(lat, lon)
    await update.message.reply_text(result)


def main():
    web_thread = Thread(target=run_web_server)
    web_thread.daemon = True
    web_thread.start()

    telegram_app = Application.builder().token(TELEGRAM_TOKEN).build()
    telegram_app.add_handler(CommandHandler("start", start))
    telegram_app.add_handler(MessageHandler(filters.LOCATION, handle_location))

    print("Starting Tennis Bot...")
    try:
        telegram_app.run_polling(drop_pending_updates=True)
    except Exception as e:
        print(f"Error: {e}")
        telegram_app.stop()
        telegram_app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()