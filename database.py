import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('myrestaurantbot.db')
cursor = conn.cursor()

# Создание таблиц
def create_tables():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER UNIQUE,
            name TEXT,
            contact TEXT,
            visit_date TEXT,
            food_quality INTEGER,
            cleanliness INTEGER,
            comments TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dishes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            category TEXT,
            price REAL
        )
    ''')
    conn.commit()

# Вызов функции создания таблиц при запуске
create_tables()
