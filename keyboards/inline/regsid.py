from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import types

keyboard_markup = types.InlineKeyboardMarkup()
user_id_btn = types.InlineKeyboardButton('Войти по Telegram ID 🆔', callback_data='press')
keyboard_markup.row(user_id_btn)