
# ライブラリの読み込み
from datetime import datetime
import pandas as pd
import requests
import json


def get_btcprice(ticker, _max):
    """[CoingeckoのAPIからビットコインの価格を取得する関数]

    Arguments:
        ticker {[Sting]} -- [通貨のティッカー例：bitcoin,ethereum]
        _max {[String]} -- [期間例：max,14days]

    Returns:
        [Dataframe] -- [価格と日付データを格納したデータフレーム]
    """

    url = 'https://api.coingecko.com/api/v3/coins/' + \
        ticker + '/market_chart?vs_currency=jpy&days=' + _max
    r = requests.get(url)
    r2 = json.loads(r.text)

    data = pd.DataFrame(r2['prices'])
    data.columns = ['date', 'price']
    date = [datetime.utcfromtimestamp(int(i / 1000)) for i in data['date']]
    data.index = date
    del data['date']
    return data


# ビットコインの全期間の価格データを取得する
btcprice = get_btcprice('bitcoin', 'max')
print(btcprice.head())
