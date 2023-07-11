"""from config import TOKEN

from aiogram import Bot, Dispatcher, executor, types

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'], state='*')
async def start_handler(message: types.Message, state: FSMContext):
    await message.answer("Привет, как тебя зовут?")
    await state.set_state("name")


@dp.message_handler(state="age")
async def age_handler(message: types.Message, state: FSMContext):
    await message.answer("Эта функция никогда не вызовется")


@dp.message_handler(state="name")
async def name_handler(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data({"name": name})
    await message.answer(f"{name}, добро пожаловать в эхо бота!")
    await state.set_state("echo")

@dp.message_handler(state="echo")
async def echo_nadler(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    await message.answer(f'{user_data["name"]} сказал: {message.text}')

executor.start_polling(dp, skip_updates=True)

from config import TOKEN

from aiogram import Bot, Dispatcher, executor, types

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

active_users: set[int] = set()


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    active_users.add(message.from_user.id)
    await message.answer("Добро пожаловать в комнату!")


@dp.message_handler()
async def chatting_handler(message: types.Message):
    for id in active_users:
        await bot.send_message(chat_id=id, text=message.text)

executor.start_polling(dp, skip_updates=True)

from __future__ import annotations

from config import TOKEN
from aiogram import Bot, Dispatcher, executor, types

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, \

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

waiting_users: set[int] = set()
connected_pairs: dict[int, int] = {}


@dp.message_handler(commands='start', state='*')
async def start_handler(message: types.Message, state: FSMContext):
    await message.answer('Привет! Добро пожаловать в чат-рулетку! Как тебя зовут?')
    await state.set_state('name')


@dp.message_handler(state='name')
async def name_handler(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data({'name': name})
    await message.reply(f'Приятно {name}! Жми /find чтобы начать общаться')
    await state.set_state('ready')


@dp.message_handler(commands='find', state='ready')
async def find_handler(message: types.Message, state: FSMContext):
    await message.answer('Ищем собеседника...')
    waiting_users.add(message.from_user.id)
    print(message.from_user.username)
    while len(waiting_users) >= 2:
        user_1_id = waiting_users.pop()
        user_2_id = waiting_users.pop()

        await dp.current_state(chat=user_1_id, user=user_1_id).set_state('chatting')
        await dp.current_state(chat=user_2_id, user=user_2_id).set_state('chatting')
        # TODO: посмотреть всё ли нормально

        connected_pairs[user_1_id] = user_2_id
        connected_pairs[user_2_id] = user_1_id

        await bot.send_message(chat_id=user_1_id, text='Вы начали общаться')
        await bot.send_message(chat_id=user_2_id, text='Вы начали общаться')


@dp.message_handler(state='chatting')
async def chatting_handler(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    chatmate_id = connected_pairs[user_id]
    await bot.send_message(chat_id=chatmate_id, text=message.text)


@dp.message_handler(state='*')
async def error_handler(message: types.Message, state: FSMContext):
    await message.reply(f'Неверный формат сообщения. Ваш текущий state: {await state.get_state()}')


executor.start_polling(dp, skip_updates=True)

from __future__ import annotations

from config import TOKEN
from aiogram import Bot, Dispatcher, executor, types

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, \
    InlineKeyboardButton, InlineKeyboardMarkup

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

b1 = KeyboardButton("чат 1 на 1")
b2 = KeyboardButton("групповой чат")

choose_chat_type_keyboard = ReplyKeyboardMarkup(
    resize_keyboard=True).insert(b1).insert(b2)

bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

waiting_users: set[int] = set()
connected_pairs: dict[int, int] = {}


@dp.message_handler(commands='start', state='*')
async def start_handler(message: types.Message, state: FSMContext):
    await message.answer('Привет! Добро пожаловать в чат-рулетку! Как тебя зовут?')
    await state.set_state('name')


 (state='name')
async def name_handler(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data({'name': name})
    await message.reply(f'Приятно познакомиться {name}! Как ты  хочешь общаться?',
                        reply_markup=choose_chat_type_keyboard)
    await state.set_state('ready')


@dp.message_handler(commands='find', state='ready')
async def find_handler(message: types.Message, state: FSMContext):
    await message.answer('Ищем собеседника...')
    waiting_users.add(message.from_user.id)
    print(message.from_user.username)
    while len(waiting_users) >= 2:
        user_1_id = waiting_users.pop()
        user_2_id = waiting_users.pop()

        await dp.current_state(chat=user_1_id, user=user_1_id).set_state('chatting')
        await dp.current_state(chat=user_2_id, user=user_2_id).set_state('chatting')
        # TODO: посмотреть всё ли нормально

        connected_pairs[user_1_id] = user_2_id
        connected_pairs[user_2_id] = user_1_id

        await bot.send_message(chat_id=user_1_id, text='Вы начали общаться')
        await bot.send_message(chat_id=user_2_id, text='Вы начали общаться')


@dp.message_handler(state='chatting')
async def chatting_handler(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    chatmate_id = connected_pairs[user_id]
    await bot.send_message(chat_id=chatmate_id, text=message.text)


@dp.message_handler(state='*')
async def error_handler(message: types.Message, state: FSMContext):
    await message.reply(f'Неверный формат сообщения. Ваш текущий state: {await state.get_state()}')


executor.start_polling(dp, skip_updates=True)"""
from aiogram.dispatcher.filters import state

from config import TOKEN
from aiogram import Bot, Dispatcher, executor, types

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, \
    InlineKeyboardButton, InlineKeyboardMarkup

from keyboard import choose_chat_type_keyboard
b2 = KeyboardButton("6")
b3 = KeyboardButton("7")
b4 = KeyboardButton("8")
b5 = KeyboardButton("9")
b6 = KeyboardButton("10")

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

waiting_users6: set[int] = set()
waiting_users7: set[int] = set()
waiting_users8: set[int] = set()
waiting_users9: set[int] = set()
waiting_users10: set[int] = set()

from dataclasses import dataclass
@dataclass
class Player:
    name: str
    telegram_id: int
    is_alive: bool
    role: str

@dataclass
class Game:
    COUNT: int
    players: list[Player]

connected_groups: dict[int, Game] = {}
@dp.message_handler(commands='start', state='*')
async def start_handler(message: types.Message, state: FSMContext):
    await message.answer('Привет! Добро пожаловать в чат-мафию! Как тебя зовут?')
    await state.set_state('name')


@dp.message_handler(state="name")
async def name_handler(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data({"name" : name})
    await message.reply(f'Приятно познакомиться {name}! С каким кол-вом игроков хочешь играть?',
    reply_markup = choose_chat_type_keyboard)
    await state.set_state('ready')

@dp.message_handler(state='ready')
async def process_room_number(message: types.Message, state: FSMContext):
    if message.text == '6':

        @dp.callback_query_handler(state='*')
        async def find_handler(message: types.Message, state: FSMContext):
            await message.answer('Ищем игроков...')
            waiting_users6.add(message.from_user.id)
            print(message.from_user.username)
            while len(waiting_users6) >= 6:
                user_1_id = waiting_users6.pop()
                user_2_id = waiting_users6.pop()
                user_3_id = waiting_users6.pop()
                user_4_id = waiting_users6.pop()
                user_5_id = waiting_users6.pop()
                user_6_id = waiting_users6.pop()

                await dp.current_state(chat=user_1_id, user=user_1_id).set_state('chatting')
                await dp.current_state(chat=user_2_id, user=user_2_id).set_state('chatting')
                await dp.current_state(chat=user_3_id, user=user_3_id).set_state('chatting')
                await dp.current_state(chat=user_4_id, user=user_4_id).set_state('chatting')
                await dp.current_state(chat=user_5_id, user=user_5_id).set_state('chatting')
                await dp.current_state(chat=user_6_id, user=user_6_id).set_state('chatting')
                # TODO: посмотреть всё ли нормально




                await bot.send_message(chat_id=user_1_id, text='Вы начали игру')
                await bot.send_message(chat_id=user_2_id, text='Вы начали игру')
                await bot.send_message(chat_id=user_3_id, text='Вы начали игру')
                await bot.send_message(chat_id=user_4_id, text='Вы начали игру')
                await bot.send_message(chat_id=user_5_id, text='Вы начали игру')
                await bot.send_message(chat_id=user_6_id, text='Вы начали игру')



executor.start_polling(dp, skip_updates=True)


