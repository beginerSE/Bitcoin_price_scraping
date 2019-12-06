
# ライブラリの読み込み
from datetime import datetime
import pandas as pd
import requests
import json


def get_btcprice(ticker, _max):
    url = 'https://api.coingecko.com/api/v3/coins/' + \
        ticker + '/market_chart?vs_currency=jpy&days=' + _max
    r = requests.get(url)
    r2 = json.loads(r.text)
    return r2



def get_price(r2):
    data = pd.DataFrame(r2['prices'])
    data.columns = ['date', 'price']
    date = []
    for i in data['date']:
        tsdate = int(i / 1000)
        loc = datetime.utcfromtimestamp(tsdate)
        date.append(loc)
    data.index = date
    del data['date']
    return data


# ビットコインの全期間の価格データを取得する
r2 = get_btcprice('bitcoin', 'max')
btcprice = get_price(r2)
btcprice.head()
