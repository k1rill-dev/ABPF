# -*- coding: utf-8 -*-
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.inline.short_bool import short

from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import Message, CallbackQuery
import logging
from states.state import StateBot
from aiogram.dispatcher.filters.builtin import CommandHelp

# from keyboards.default.button import year_button
from loader import dp

from keyboards.inline.year_goriz import choice


@dp.message_handler(text='🚪 Начать 🚪',state=StateBot.Invest_gorizont)
async def bot_year(message: types.Message):

    await message.answer("Укажите длину инвестиционного горизонта", reply_markup=choice)

@dp.callback_query_handler(text_contains="year", state=StateBot.Invest_gorizont)
async def buying_pear(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    callback_data = str(call.data).split(':')[-1]

    await state.update_data(
        {"invest_gorizont": callback_data}
    )
    await StateBot.Short.set()
    await call.message.answer("Учитывать короткие позиции по ценным бумагам при анализе?", reply_markup=short)

@dp.message_handler(CommandHelp(), state=StateBot.Short)
async def bot_help(message: types.Message):
    text = 'Какой функционал имеет сервис ABPF 🧐\n\n' \
           'Мы предоставляем аналитику актуальных ценных бумаг 📈 \n\n' \
           'Основной функционал:\n\n' \
           '   <strong>1) Отображение состояния актуальных синих фишек на данный момент</strong>\n' \
           '   <strong>2) Прогнозирование доходности портфеля</strong>\n' \
           '   <strong>3) Вывод подробной информации о каждой синей фишке</strong>\n' \
           '   <strong>4) Показ полной цены портфеля на текущий и будущий моменты</strong>\n' \
           '   <strong>5) Рекомендации к покупке доходных облигаций</strong>\n\n' \

    await message.answer(text)