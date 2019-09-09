
#ライブラリの読み込み
from datetime import datetime
import pandas as pd
import requests
import json
import pandas as pd

def get_btcprice(ticker,_max):
    url=('https://api.coingecko.com/api/v3/coins/')+ticker+('/market_chart?vs_currency=jpy&days=')+_max
    r=requests.get(url)
    r2 = json.loads(r.text)
    return r2


#jsonから価格データだけをPandasに変換して抽出する
def get_price(r2):
    s=pd.DataFrame(r2['prices'])
    s.columns=['date','price']
    date=[]
    for i in s['date']:
        tsdate=int(i/1000)
        loc =datetime.utcfromtimestamp(tsdate)
        date.append(loc)
    s.index=date
    del s['date']
    return s

#ビットコインの全期間の価格データを取得する
r2=get_btcprice('bitcoin','max')
btcprice=get_price(r2)
btcprice.head()
