# handlers/start.py

from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher import Dispatcher

# Уникальные пользователи для учета
unique_users = set()

async def start_command(message: types.Message):
    if message.from_user.id not in unique_users:
        unique_users.add(message.from_user.id)
    greeting = f"Привет, {message.from_user.first_name}!"
    
    # Создание кнопок
    keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton("Наш адрес", url="https://example.com"),
        InlineKeyboardButton("Контакты", url="https://example.com"),
        InlineKeyboardButton("О нас", url="https://example.com"),
        InlineKeyboardButton("Наш сайт", url="https://example.com")
    )
    
    await message.reply(greeting, reply_markup=keyboard)

# Функция для регистрации хендлера
def register_start_handler(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=["start"])
