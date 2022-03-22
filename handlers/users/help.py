from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = 'Какой функционал имеет сервис ABPF 🧐\n\n' \
           'Мы предоставляем аналитику актуальных ценных бумаг 📈 \n\n' \
           'Основной функционал:\n\n' \
           '   <strong>✅ Отображение состояния актуальных синих фишек на данный момент</strong>\n' \
           '   <strong>✅ Прогнозирование доходности портфеля</strong>\n' \
           '   <strong>✅ Вывод подробной информации о каждой синей фишке</strong>\n' \
           '   <strong>✅ Выгрузка портфеля в удобном CSV файле</strong>\n' \
           '   <strong>✅ Рекомендации к покупке доходных облигаций</strong>\n' \
           '   <strong>✅ Визуализация статистики по ценным бумагам в портфеле</strong>\n' \
           '   <strong>✅ Отображение актуального курса валют</strong>\n' \
           '   <strong>✅ Информация о надежных брокерах</strong>\n' \
           '   <strong>✅ Информация о Лидерах Роста/Падения акционерных обществ</strong>\n'

    await message.answer(text)


@dp.message_handler(text='📝 Справка 📝')
async def bot_help(message: types.Message):
    text = 'Какой функционал имеет сервис ABPF 🧐\n\n' \
           'Мы предоставляем аналитику актуальных ценных бумаг 📈 \n\n' \
           'Основной функционал:\n\n' \
           '   <strong>✅ Отображение состояния актуальных синих фишек на данный момент</strong>\n' \
           '   <strong>✅ Прогнозирование доходности портфеля</strong>\n' \
           '   <strong>✅ Вывод подробной информации о каждой синей фишке</strong>\n' \
           '   <strong>✅ Выгрузка портфеля в удобном CSV файле</strong>\n' \
           '   <strong>✅ Рекомендации к покупке доходных облигаций</strong>\n' \
           '   <strong>✅ Визуализация статистики по ценным бумагам в портфеле</strong>\n' \
           '   <strong>✅ Отображение актуального курса валют</strong>\n' \
           '   <strong>✅ Информация о надежных брокерах</strong>\n' \
           '   <strong>✅ Информация о Лидерах Роста/Падения акционерных обществ</strong>\n'
    await message.answer(text)
