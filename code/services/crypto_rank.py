from flask import render_template, jsonify, abort, Response
from ticker_base import MetricsTickerBase
from services import app
import requests
import os

class CryptoRankMetrics(MetricsTickerBase):
    """ PingAPI """

    def _get_rank(self):
        api_req = requests.get('https://www.cryptocompare.com/api/data/coinlist/')
        if api_req.status_code == 200:
            api_data = api_req.json()
            res = []
            rank = []
            for k, v in api_data['Data'].items():
                rank.append({
                    'labels': { 'currency': k, 'name': v['CoinName'] },
                    'value': v['SortOrder'],
                })
            res.append({
                'key': 'crypto_exchange_rank',
                'type': 'gauge',
                'values': rank,
            })
            return res
        return []

    def get(self):
        metrics = self._get_rank()

        self._update_labels_string(metrics)

        return Response(
            render_template('metrics.txt', metrics=metrics),
            mimetype='text/plain',
        )

app.add_url_rule('/metrics/cryptorank', view_func=CryptoRankMetrics.as_view('cryptorank'))
