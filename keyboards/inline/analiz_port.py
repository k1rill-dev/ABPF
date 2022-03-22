# -*- coding: utf-8 -*-

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

analiz = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="💼 Собрать портфель 💼", callback_data="portfel")
    ],
    [
        InlineKeyboardButton(text="📊 Посмотреть аналитику 📊", callback_data="analiz")
    ],
    [
        InlineKeyboardButton(text="📤 Выгрузить портфель в CSV файл 📤", callback_data="csv")
    ]
])
