from flask import render_template, jsonify, abort, Response
from flask.views import MethodView
from services import app
import requests
import os

class CryptoTickerMetrics(MethodView):
    """ PingAPI """

    def _get_rates(self, from_currency, to_currency):
        if type(from_currency) is not list:
            from_currency = [from_currency]
        if type(to_currency) is not list:
            to_currency = [to_currency]
        api_req = requests.get(
            'https://min-api.cryptocompare.com/data/pricemultifull?fsyms={}&tsyms={}'.format(
                ','.join(from_currency),
                ','.join(to_currency),
            )
        )
        if api_req.status_code == 200:
            api_data = api_req.json()
            res = []
            prices = []
            supply = []
            for ka, va in api_data['RAW'].items():
                supply.append({
                    'labels': { 'currency': ka, },
                    'value': va.values()[0]['SUPPLY'],
                })
                for kb, vb in va.items():
                    prices.append({
                        'labels': { 'to': kb, 'from': ka, },
                        'value': vb['PRICE'],
                    })
            res.append({
                'key': 'crypto_exchange_supply',
                'type': 'gauge',
                'values': supply,
            })
            res.append({
                'key': 'crypto_exchange_price',
                'type': 'gauge',
                'values': prices,
            })
            return res
        return []

    def get(self):
        _from = [x.strip().upper() for x in os.environ.get('FROM_CURRENCIES').split(',')]
        _to = [x.strip().upper() for x in os.environ.get('TO_CURRENCIES').split(',')]

        metrics = self._get_rates(
            from_currency=_from,
            to_currency=_to,
            )

        for metric in metrics:
            for value in metric['values']:
                if 'labels' in value:
                    value['labels_string'] = ', '.join(['{}="{}"'.format(k, v) for k, v in value['labels'].items()])

        return Response(
            render_template('metrics.txt', metrics=metrics),
            mimetype='text/plain',
        )

app.add_url_rule('/metrics/cryptoticker', view_func=CryptoTickerMetrics.as_view('cryptoticker'))
