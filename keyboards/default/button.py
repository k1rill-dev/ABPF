# -*- coding: utf-8 -*-

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🚪 Начать 🚪"),
        ]

    ],
    resize_keyboard=True
)