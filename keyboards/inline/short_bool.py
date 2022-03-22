# -*- coding: utf-8 -*-

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

short = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="✅ Да ✅", callback_data="bool:true")
    ],
    [
        InlineKeyboardButton(text="❎ Нет ❎", callback_data="bool:false")
    ]
])
