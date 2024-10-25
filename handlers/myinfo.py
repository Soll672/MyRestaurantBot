# handlers/myinfo.py

from aiogram import types
from aiogram.dispatcher import Dispatcher

async def myinfo_command(message: types.Message):
    user_info = (
        f"Ваш id: {message.from_user.id}\n"
        f"Ваше имя: {message.from_user.first_name}\n"
        f"Ваш username: {message.from_user.username}"
    )
    await message.reply(user_info)

# Функция для регистрации хендлера
def register_myinfo_handler(dp: Dispatcher):
    dp.register_message_handler(myinfo_command, commands=["myinfo"])
