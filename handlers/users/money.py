# -*- coding: utf-8 -*-
from aiogram.dispatcher.filters import Text
from aiogram import types
from aiogram.types import Message, CallbackQuery

from loader import dp
from states.state import StateBot
from aiogram.dispatcher import FSMContext
from keyboards.inline.short_bool import short


# @dp.message_handler(state=StateBot.Short)
# async def bot_money(message: types.Message, state: FSMContext):
#     await message.answer("Учитывать ли короткие позиции по акциям?", reply_markup=short)



@dp.callback_query_handler(text_contains="bool", state=StateBot.Short)
async def shorts(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    callback_data = str(call.data).split(':')[-1]
    await state.update_data(
        {"short": callback_data}
    )
    await StateBot.Money.set()
    await call.message.answer('Теперь введите ваш бюджет (в валюте 💲)')



