from flask import render_template, jsonify, abort, Response
from flask.views import MethodView
import os

class MetricsTickerBase(MethodView):
    """ PingAPI """

    def _get_params(self, from_param, to_param):
        _from = [x.strip().upper() for x in os.environ.get(from_param, '').split(',') if x]
        _to = [x.strip().upper() for x in os.environ.get(to_param, '').split(',') if x]
        if not _from or not _to:
            abort(500, 'Must set env: {}'.format(', '.join([from_param, to_param])))
        return _from, _to

    def _update_labels_string(self, metrics):
        for metric in metrics:
            for value in metric['values']:
                if 'labels' in value:
                    print(value['labels'])
                    value['labels_string'] = ', '.join(['{}="{}"'.format(
                        k, v.encode('ascii', 'ignore')
                        ) for k, v in value['labels'].items()])
