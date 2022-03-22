# -*- coding: utf-8 -*-

from flask import Flask, make_response
from flask_restful import Api
from flask import jsonify
from flask_restful import Resource
from flask_restful import reqparse
from stocks_analiz import Stock
import os
import datetime as dt
from bonds import Bond

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('date', required=True)
parser.add_argument('length_invest_horizon', required=True)
parser.add_argument('shorts', required=True)
parser.add_argument('budget', required=True, type=int)
parser.add_argument('tg_id', required=True, type=int)


class Briefcase(Resource):
    def get(self):
        args = parser.parse_args()
        news = {
            'date': args['date'],
            'length_invest_horizon': args['length_invest_horizon'],
            'budget': args['budget'],
            'tg_id': args['tg_id'],
            'shorts': args['shorts']
        }
        if int(news['length_invest_horizon']) == 1:
            mon_stoks = int(news['budget']) * 0.2
            mon_bonds = int(news['budget']) * 0.8

        elif int(news['length_invest_horizon']) == 3:
            mon_stoks = int(news['budget']) * 0.3
            mon_bonds = int(news['budget']) * 0.7

        elif int(news['length_invest_horizon']) == 5:
            mon_stoks = int(news['budget']) * 0.5
            mon_bonds = int(news['budget']) * 0.5

        stock = Stock(money=mon_stoks, shorts=bool(news['shorts']))
        stock.sharp()
        stock.profit()
        stock.volatility()
        name_file = stock.plot()
        bond = Bond()
        bond.get_bonds(mon_bonds, int(news['length_invest_horizon']))

        with open(name_file, 'rb') as file:
            image_binary = file.read(-1)
        response = make_response(image_binary)
        response.headers.set('Content-Type', 'image/png')
        response.headers.set(
            'Content-Disposition', 'attachment', filename=name_file)
        return response

    def post(self):
        args = parser.parse_args()
        news = {
            'date': args['date'],
            'length_invest_horizon': args['length_invest_horizon'],
            'budget': args['budget'],
            'tg_id': args['tg_id'],
            'shorts': args['shorts']
        }
        if int(news['length_invest_horizon']) == 1:
            mon_stoks = int(news['budget']) * 0.2
            mon_bonds = int(news['budget']) * 0.8

        elif int(news['length_invest_horizon']) == 3:
            mon_stoks = int(news['budget']) * 0.3
            mon_bonds = int(news['budget']) * 0.7

        elif int(news['length_invest_horizon']) == 5:
            mon_stoks = int(news['budget']) * 0.5
            mon_bonds = int(news['budget']) * 0.5

        stock = Stock(money=mon_stoks, shorts=bool(news['shorts']))
        sharp = stock.sharp()
        profit = stock.profit()
        volatility = stock.volatility()
        # name_file = stock.plot()
        bond = Bond()
        gbonds = bond.get_bonds(mon_bonds, int(news['length_invest_horizon']))

        # with open(name_file, 'rb') as file:
        #     image_binary = file.read(-1)
        # response = make_response(image_binary)
        # response.headers.set('Content-Type', 'image/png')
        # response.headers.set(
        #     'Content-Disposition', 'attachment', filename=name_file)

        return jsonify({
            'success': 'OK',
            'time': dt.datetime.now().strftime("%d-%m-%Y"),
            'stoks': {
                'volatility': {
                    'stoks_and_count': volatility[0],
                    'balance': volatility[1]
                },
                'sharp': {
                    'stoks_and_count': sharp[0],
                    'balance': sharp[1]
                }
            },
            'bonds': gbonds,
            'yield': profit
        })


class Test(Resource):

    def post(self, id_img):
        args = parser.parse_args()
        news = {
            'date': args['date'],
            'length_invest_horizon': args['length_invest_horizon'],
            'budget': args['budget'],
            'tg_id': args['tg_id'],
            'shorts': args['shorts']
        }
        if int(news['length_invest_horizon']) == 1:
            mon_stoks = int(news['budget']) * 0.2
            mon_bonds = int(news['budget']) * 0.8

        elif int(news['length_invest_horizon']) == 3:
            mon_stoks = int(news['budget']) * 0.3
            mon_bonds = int(news['budget']) * 0.7

        elif int(news['length_invest_horizon']) == 5:
            mon_stoks = int(news['budget']) * 0.5
            mon_bonds = int(news['budget']) * 0.5

        stock = Stock(money=mon_stoks, shorts=bool(news['shorts']))
        stock.sharp()
        stock.volatility()
        if id_img == 1:
            name_file = stock.plot()
        elif id_img == 2:
            name_file = stock.plot_equal_sharp()
        elif id_img == 3:
            name_file = stock.plot_equal_volatility()
        # bond = Bond()
        # bond.get_bonds(mon_bonds, int(news['length_invest_horizon']))

        with open(name_file, 'rb') as file:
            image_binary = file.read(-1)
        response = make_response(image_binary)
        response.headers.set('Content-Type', 'image/png')
        response.headers.set(
            'Content-Disposition', 'attachment', filename=name_file)
        return response


def main():
    api.add_resource(Briefcase, '/api/v2/briefcase/')
    api.add_resource(Test, '/api/v2/test/<int:id_img>')

    # db_session.global_init("db/db_users.db")
    app.run()


if __name__ == '__main__':
    main()
