# -*- coding: utf-8 -*-

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

choice = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🟩 1 г. 🟩", callback_data="year:1")
    ],
    [
        InlineKeyboardButton(text="🟨 3 г. 🟨", callback_data="year:3")
    ],
    [
        InlineKeyboardButton(text="🟥 5 л. 🟥", callback_data="year:5")
    ]
])