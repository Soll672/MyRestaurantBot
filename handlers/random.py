# handlers/random.py

from aiogram import types
from aiogram.dispatcher import Dispatcher
import random

async def random_command(message: types.Message):
    names = ["Алексей", "Мария", "Дмитрий", "Ольга", "Екатерина"]
    random_name = random.choice(names)
    await message.reply(f"Случайное имя: {random_name}")

# Функция для регистрации хендлера
def register_random_handler(dp: Dispatcher):
    dp.register_message_handler(random_command, commands=["random"])
