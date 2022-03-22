# -*- coding: utf-8 -*-

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters.builtin import CommandHelp
from keyboards.inline.regsid import keyboard_markup
from aiogram.dispatcher import FSMContext

from keyboards.default.button import start_button
from loader import dp

from states.state import StateBot

@dp.message_handler(CommandStart(), state=None)
async def bot_start(message: types.Message):
    await message.answer(f"Привет  👋 ,  {message.from_user.full_name}!\n\n"
                         f"ABPF - это высокоточный и качественный сервис для отслеживания акций и составления плана покупок актуальных облигаций 💵 \n\n", reply_markup=keyboard_markup)

    await StateBot.Invest_gorizont.set()

@dp.callback_query_handler(lambda c: c.data == 'press',state=StateBot.Invest_gorizont)
async def about_bot_message(call: types.CallbackQuery, state: FSMContext):
    await call.answer('Вы успешно вошли', True)
    print(call.from_user.id)
    await state.update_data(
        {"tg_id": call.from_user.id}
    )
    await call.message.answer('<strong>Отлично ✅</strong>\n'
                              'Теперь вы зарегестрированы, чтобы продолжить, нажмите кнопку "🚪 Начать 🚪"', reply_markup=start_button)

@dp.message_handler(CommandHelp(), state=StateBot.Invest_gorizont)
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