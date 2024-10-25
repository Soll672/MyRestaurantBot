import os
from aiogram import Bot, Dispatcher, executor
from dotenv import load_dotenv
from handlers.start import register_start_handler
from handlers.myinfo import register_myinfo_handler
from handlers.random import register_random_handler
from handlers.dishes import register_dish_handlers

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Регистрация хендлеров
register_start_handler(dp)
register_myinfo_handler(dp)
register_random_handler(dp)
register_dish_handlers(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
