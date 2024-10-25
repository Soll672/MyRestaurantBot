from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

class RestaurantReview(StatesGroup):
    name = State()
    contact = State()
    visit_date = State()
    food_quality = State()
    cleanliness = State()
    comments = State()
