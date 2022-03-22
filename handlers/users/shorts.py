# -*- coding: utf-8 -*-
from aiogram import types
from states.state import StateBot
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from keyboards.inline.analiz_port import analiz
from requests import get, post
from keyboards.default.menu import main_menu1
from loader import dp
import datetime as dt
import csv


@dp.message_handler(state=StateBot.Money)
async def bot_short(message: types.Message, state: FSMContext):
    try:
        price = int(message.text)
        await state.update_data(
            {"money": price}
        )
        data = await state.get_data()

        await message.answer('Данные успешно собраны, теперь вы можете собрать портфель и  посмотреть аналитику',
                             reply_markup=analiz)
    except:
        await state.finish()
        await message.answer(f'Значение должно содержать только цифры \n\n'
                             f'Чтобы узнать больше информации о возможностях введите команду "/help" ✍ ')


@dp.callback_query_handler(text_contains="portfel", state=StateBot.Money)
async def buying_pear(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    data = await state.get_data()
    if len(data) == 3:
        data['tg_id'] = None
    print(data)

    json_resp = post('http://localhost:5000/api/v2/briefcase/', json={
        'date': dt.datetime.now().strftime("%d-%m-%Y"),
        'length_invest_horizon': data['invest_gorizont'],
        'budget': data['money'],
        'tg_id': data['tg_id'],
        'shorts': data['short']
    }).json()
    list_bonds = []
    for item in json_resp['bonds']:
        list_bonds.append(
            f'📍 Эмитент: {item["name"]}\n\n    💰 Купонный доход: {item["coupon_yield"]}\n    📌 Количество облигаций: {item["count"]}\n    ⚖️ Цена покупки/продажи {item["price"]}\n    ⏱ Год погашения: {item["repayment_year"]}\n    ♻ Траты за год: {item["spent_for_years"]}\n\n')

    price = list()
    price_vol = list()
    stoks = json_resp["stoks"]
    for i, k in stoks.get('sharp').get('stoks_and_count').items():
        s = f'\n{i} - {k}'
        price.append(s)

    for v, k in stoks.get('volatility').get('stoks_and_count').items():
        s = f'\n{v} - {k}'
        price_vol.append(s)

    msg = f"📈 Формирование портфеля по максимальному коэфициенту Шарпа:" + \
          f'\n{"".join(price)}\n' + \
          f"\n💵 Остаток средств(по Шарпу)  - {stoks.get('sharp').get('balance')}\n" + \
          f'\n📌 Формирование портфеля по минимальной волатильности:' + \
          f'\n{"".join(price_vol)}\n' + \
          f'\n💵 Остаток средств(Волантильность) - {stoks.get("volatility").get("balance")}\n' + \
          f'\n📅 Дата формирования портфелей: {json_resp["time"]}\n' + \
          f'\n💰 Годовой доход: {json_resp["yield"]}'

    await call.message.answer('💼 Состав портфеля\n', reply_markup=ReplyKeyboardRemove())
    await call.message.answer('📈 Данные об акциях\n')
    await call.message.answer(msg)
    await call.message.answer('📜 Данные об облигациях\n', reply_markup=main_menu1)
    await call.message.answer(''.join(list_bonds))


@dp.callback_query_handler(text_contains="csv", state=StateBot.Money)
async def buying_pear(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    data = await state.get_data()
    if len(data) == 3:
        data['tg_id'] = None
    print(data)

    json_resp = post('http://localhost:5000/api/v2/briefcase/', json={
        'date': dt.datetime.now().strftime("%d-%m-%Y"),
        'length_invest_horizon': data['invest_gorizont'],
        'budget': data['money'],
        'tg_id': data['tg_id'],
        'shorts': data['short']
    }).json()

    path_bond = f"portfolio_with_bonds_{dt.datetime.now().strftime('%d-%m-%Y')}.csv"
    with open(path_bond, 'w') as f:
        wr = csv.DictWriter(f, ["count", "coupon_yield", "name", "price",
                                "repayment_year", "spent_for_years"])
        wr.writeheader()
        wr.writerows(json_resp["bonds"])


    sharp_keys = json_resp['stoks']['sharp']['stoks_and_count'].keys()
    volatility_keys = json_resp['stoks']['volatility']['stoks_and_count'].keys()
    path_stoks = f"portfolio_with_stoks_{dt.datetime.now().strftime('%d-%m-%Y')}.csv"
    with open(path_stoks, 'w') as f:
        spamwriter = csv.writer(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(["sharp_balance", *sharp_keys,
                             "volatility_balance", *volatility_keys])
        spamwriter.writerow([json_resp['stoks']['sharp']["balance"],
                             *json_resp['stoks']['sharp']['stoks_and_count'].values(),
                             json_resp['stoks']['volatility']["balance"],
                             *json_resp['stoks']['volatility']['stoks_and_count'].values()])
    await call.message.answer_document(document=types.InputFile(path_bond), reply_markup=main_menu1)
    await call.message.answer_document(document=types.InputFile(path_stoks), reply_markup=main_menu1)


# await state.finish()
