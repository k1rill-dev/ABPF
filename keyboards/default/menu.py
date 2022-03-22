# -*- coding: utf-8 -*-

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⚖ Курсы валют ⚖"),
        ],
        [
            KeyboardButton(text="📝 Справка 📝"),
        ],
        [
            KeyboardButton(text="📚 Информация о надежных брокерах 📚"),
        ],
        [
            KeyboardButton(text="📈 Лидеры Роста/Падения 📉"),
        ]

    ],
    resize_keyboard=True
)

main_menu1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🏠 Главное меню 🏠"),
        ]

    ],
    resize_keyboard=True
)