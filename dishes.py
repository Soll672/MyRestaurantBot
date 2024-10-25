from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('myrestaurantbot.db')
cursor = conn.cursor()

# Машинное состояние для добавления блюда
class AddDish(StatesGroup):
    name = State()
    category = State()
    price = State()

# Команда /add_dish для начала добавления блюда
async def add_dish_start(message: types.Message):
    await message.reply("Введите название блюда:")
    await AddDish.name.set()

# Обработчик для получения названия блюда
async def add_dish_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.reply("Введите категорию блюда:")
    await AddDish.category.set()

# Обработчик для получения категории блюда
async def add_dish_category(message: types.Message, state: FSMContext):
    await state.update_data(category=message.text)
    await message.reply("Введите цену блюда:")
    await AddDish.price.set()

# Обработчик для получения цены блюда и сохранения в БД
async def add_dish_price(message: types.Message, state: FSMContext):
    try:
        price = float(message.text)
        data = await state.get_data()
        name = data['name']
        category = data['category']

        # Сохранение блюда в таблице dishes
        cursor.execute('INSERT INTO dishes (name, category, price) VALUES (?, ?, ?)', (name, category, price))
        conn.commit()

        await message.reply(f"Блюдо '{name}' успешно добавлено.")
        await state.finish()
    except ValueError:
        await message.reply("Пожалуйста, введите корректное число для цены.")

# Команда для отображения всех блюд с сортировкой
async def show_dishes(message: types.Message):
    # Запрос на получение блюд с сортировкой по цене и названию
    cursor.execute('SELECT name, category, price FROM dishes ORDER BY price, name')
    dishes = cursor.fetchall()
    if not dishes:
        await message.reply("Нет добавленных блюд.")
    else:
        reply_text = "Список блюд:\n\n"
        for dish in dishes:
            reply_text += f"{dish[0]} — {dish[1]}, {dish[2]} сом\n"
        await message.reply(reply_text)

# Регистрация обработчиков
def register_dish_handlers(dp: Dispatcher):
    dp.register_message_handler(add_dish_start, commands="add_dish", state="*")
    dp.register_message_handler(add_dish_name, state=AddDish.name)
    dp.register_message_handler(add_dish_category, state=AddDish.category)
    dp.register_message_handler(add_dish_price, state=AddDish.price)
    dp.register_message_handler(show_dishes, commands="show_dishes")
