import requests
import json

def top_n_crypto(n=25):
    api_req = requests.get('https://www.cryptocompare.com/api/data/coinlist/')
    if api_req.status_code == 200:
        api_data = api_req.json()
        res = []
        for k, v in api_data['Data'].items():
            res.append({
                'currency': k,
                'name': v['CoinName'],
                'value': v['SortOrder'],
            })
        res = sorted(res, key=lambda x: int(x['value']))
        if len(res) > n:
            res = res[:n]
        return res
    return []


print('-----')

res = top_n_crypto(n=25)
c = []
for x in res:
    c.append(x['currency'])

print(json.dumps(c, indent=2))

print ','.join(c)
