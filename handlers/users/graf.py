# -*- coding: utf-8 -*-
import io
from aiogram import types
import os
from PIL import Image
from aiogram import types
from states.state import StateBot
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery
from keyboards.inline.analiz_port import analiz
from requests import get, post
from loader import dp, bot
import datetime as dt
from keyboards.default.menu import main_menu1


@dp.callback_query_handler(text_contains="analiz", state=StateBot.Money)
async def buying_pear(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    data = await state.get_data()
    if len(data) == 3:
        data['tg_id'] = None
    # print(data)
    # print(12312)
    for i in range(1, 4):
        json_resp = post(f'http://localhost:5000/api/v2/test/{i}', json={
            'date': dt.datetime.now().strftime("%d-%m-%Y"),
            'length_invest_horizon': data['invest_gorizont'],
            'budget': data['money'],
            'tg_id': data['tg_id'],
            'shorts': data['short']
        }).content
        saved = Image.open(io.BytesIO(json_resp))
        saved.save(f'{i}.png')
        await bot.send_photo(call.message.chat.id, types.InputFile(path_or_bytesio=f'{i}.png'), reply_markup=main_menu1)



# @dp.message_handler(text='aaa', state=StateBot.Money)
# async def bot_short(message: types.Message, state: FSMContext):
#     # await call.answer(cache_time=60)
#     data = await state.get_data()
#     if len(data) == 3:
#         data['tg_id'] = None
#     print(data)
#     for i in range(1, 4):
#         json_resp = post(f'http://localhost:5000/api/v2/test/{i}', json={
#             'date': dt.datetime.now().strftime("%d-%m-%Y"),
#             'length_invest_horizon': data['invest_gorizont'],
#             'budget': data['money'],
#             'tg_id': data['tg_id'],
#             'shorts': data['short']
#         }).content
#         print(json_resp)
#         saved = Image.open(io.BytesIO(json_resp))
#         saved.save(f'{i}.png')
#
#         await bot.send_photo(chat_id=message.from_user.id,
#                              photo=f'{i}.png')
