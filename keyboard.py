from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, \
                          InlineKeyboardButton, InlineKeyboardMarkup


b2 = KeyboardButton("6")
b3 = KeyboardButton("7")
b4 = KeyboardButton("8")
b5 = KeyboardButton("9")
b6 = KeyboardButton("10")
choose_chat_type_keyboard = ReplyKeyboardMarkup(
    resize_keyboard=True).insert(b2).insert(b3).insert(b4).insert(b5).insert(b6)