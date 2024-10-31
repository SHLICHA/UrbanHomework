import os

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters.state import State, StatesGroup
from dotenv import load_dotenv

from crud_functions import *


load_dotenv()
api = os.getenv('TOKEN_BY_TELEGRAM')
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_1 = KeyboardButton('Рассчитать')
button_2 = KeyboardButton('Информация')
button_3 = KeyboardButton('Купить')
button_4 = KeyboardButton('Регистрация')
keyboard.row(button_1, button_2)
keyboard.row(button_3)
keyboard.row(button_4)

buy_keyboard = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [InlineKeyboardButton(text='Продукт1', callback_data="product_buying")],
        [InlineKeyboardButton(text='Продукт2', callback_data="product_buying")],
        [InlineKeyboardButton(text='Продукт3', callback_data="product_buying")],
        [InlineKeyboardButton(text='Продукт4', callback_data="product_buying")]
    ],
    resize_keyboard=True
)
inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')],
        [InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')]
    ],
    resize_keyboard=True
)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State()


@dp.message_handler(commands='start')
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=keyboard)


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer(text='Выберите опцию:', reply_markup=inline_keyboard)


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    products = get_all_products()
    for product in products:
        with open(f'foto/photo{product[0]}.jpg', 'rb') as photo:
            await message.answer_photo(
                photo,
                f'Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]}'
            )
    await message.answer(text='Выберите продукт для покупки:', reply_markup=buy_keyboard)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer(text='Вы успешно приобрели продукт!')
    await call.answer()


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer(text='10 х вес(кг) + 6,25 x рост(см) – 5 х возраст(г) + 5')
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:', reply_markup=None)
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    result = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5
    await message.answer(f'Ваша ежедневная норма составялет {int(result)} калорий в день', reply_markup=keyboard)


@dp.message_handler(text='Регистрация')
async def sign_up(message):
    await message.answer('Введите имя пользователя (только латинский алфавит):', reply_markup=None)
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async  def set_username(message, state):
    if is_included(message.text):
        await message.answer('Пользователь существует, введите другое имя')
        await RegistrationState.username.set()
    else:
        await state.update_data(username=message.text)
        await message.answer('Введите свой email:')
        await RegistrationState.email.set()


@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer('Введите свой возраст:')
    await RegistrationState.age.set()


@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age=message.text)
    data = await state.get_data()
    add_user(data['username'], data['email'], data['age'])
    await message.answer("Регистрация прошла успешно!", reply_markup=keyboard)
    await state.finish()


@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    initiate_db() #инициализируем базу данных
    executor.start_polling(dp, skip_updates=True)
