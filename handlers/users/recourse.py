# -*- coding: utf-8 -*-
import requests
import json
from keyboards.default.menu import main_menu
import requests
from bs4 import BeautifulSoup
from aiogram.utils.markdown import hbold, hlink

from aiogram import types
from states.state import StateBot
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery
from keyboards.inline.analiz_port import analiz
from loader import dp
import datetime as dt


@dp.message_handler(text='🏠 Главное меню 🏠', state=StateBot.Money)
async def bot_zxc(message: types.Message, state: FSMContext):
    await message.answer('Теперь вы в главном меню 😊\n'
                         '<b>Теперь вам доступны</b>:\n'
                         '1. <strong>⚖ Курсы валют ⚖</strong>\n'
                         '2. <strong>📝 Справка 📝</strong>\n'
                         '3. <strong>📚 Информация о надежных брокерах 📚</strong>\n'
                         '4. <strong>📈 Лидеры Роста/Падения 📉</strong>', reply_markup=main_menu)
    await state.finish()


@dp.message_handler(text='⚖ Курсы валют ⚖')
async def bot_zxc(message: types.Message):
    import requests
    import json
    import datetime as dt
    dot = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()

    # URL = "https://api.bittrex.com/api/v1.1/public/getticker?market=USD-BTC"
    URL = "https://api.bittrex.com/api/v1.1/public/getticker?market=USD-BTC"
    old_price = 0
    j = requests.get(URL)
    data = json.loads(j.text)
    price = data['result']['Ask']
    if price != 0:
        old_price = price

    uah = int(dot['Valute']['CNY']['Value'])
    kazah = int(dot['Valute']['KZT']['Value'])
    euro = int(dot['Valute']['EUR']['Value'])
    dollar = int(dot['Valute']['USD']['Value'])
    price = f'💶 Цена за €:  {euro} ₽\n💴 Цена за KZT:  {kazah / 100} ₽\n💴 Цена за ¥:  {uah} ₽\n💵 Цена за $:  {dollar} ₽\n🪙 Цена за BTC:  {price} $\n'
    await message.answer(price)


@dp.message_handler(text='📚 Информация о надежных брокерах 📚')
async def inf(message: types.Message):
    url = 'https://www.sravni.ru/invest/brokerskoe-obsluzhivanie/rating/'
    req = requests.get(url)
    response = req.text
    soup = BeautifulSoup(response, 'lxml')
    s_list = list()
    br = soup.find_all('div', class_='style_lineBefore__5dKhW style_card__Ekris style_main__ZqUIo')
    for b in br:
        name = b.find('div', class_='style_row__uzjMQ style_spaceSubGrid__f2PlW').find('div',
                                                                                       class_='style_row__uzjMQ style_spaceSubGrid__f2PlW').text
        comision = b.find('div', class_='style_range__cjBhD').text
        href = b.find('a').get("href")
        msg = f'📍 Брокер и лицензия: {str(name.replace("«", "").replace("»", " ")).split("№")[:-1][0]}' + \
              f'\n     📉 Комиссия за операцию: {comision}' \
              f'\n     🔗 Ссылка на сайт брокера: {hlink(str(name.replace("«", "").replace("»", " ")).split("№")[:-1][0], href)}'
        s_list.append(msg)

    await message.answer('\n\n'.join(s_list))


@dp.message_handler(text='📈 Лидеры Роста/Падения 📉')
async def inf(message: types.Message):
    url = 'https://bcs-express.ru/webapi2/api/quotes/leaders?delay=true&datefilter=month&volume=more3kk&portfolioId=0'
    req = requests.get(url)
    get_json = req.json()
    leaders_up = get_json.get("up")
    leaders_down = get_json.get("down")
    ld_up = list()
    ld_down = list()
    for lead in leaders_up:
        msg = f'📌 Название акционерного общества: {lead.get("shortName")}' + \
              f'\n⬆   Изменение цены: {round(float(lead.get("change")), 2)} %' + \
              f'\n💵  Цена акции: {float(lead.get("value"))} ₽' + \
              f'\n🔎  Подробная информация - ' + 'https://bcs-express.ru/kotirovki-i-grafiki' + lead.get(
            "hyperlink") + '\n'
        ld_up.append(msg)

    for lead in leaders_down:
        msg = f'📌 Название акционерного общества: {lead.get("shortName")}' + \
              f'\n⬇   Изменение цены: {round(float(lead.get("change")), 2)} %' + \
              f'\n💵  Цена акции: {float(lead.get("value"))} ₽' + \
              f'\n🔎  Подробная информация - ' + 'https://bcs-express.ru/kotirovki-i-grafiki' + lead.get(
            "hyperlink") + '\n'
        ld_down.append(msg)
    up = '\n'.join(ld_up[:5])
    down = '\n'.join(ld_down[:5])
    await message.answer(f'📈 <strong>Лидеры Роста</strong> 📈\n\n{up}\n')
    await message.answer(f'📉 <strong>Лидеры Падения</strong> 📉\n\n{down}\n')
