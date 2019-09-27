

import sqlite3
import requests
import datetime
import json

# データベースのパスを指定
dbpath = 'crypto.sqlite'

# データベースに接続する
c = sqlite3.connect(dbpath)
cur = c.cursor()

# テーブルの作成(初回のみ)
try:
    #c.execute('create table crypto_id(id integer, ticker, text)')
    c.execute('create table price_data(date datetime, id integer, price, float)')
except Exception as e:
    print(e)
    pass

# ビットコインのid
btc_id = 1
btcfx_id = 2
bsv_id = 3
xrp_id = 4

# ビットフライヤーのAPIから価格データを取得
url = ('https://api.bitflyer.com/v1/ticker')
r = requests.get(url)
r = json.loads(r.text)
price = r['ltp']

# 今日の日付と時間(hour)を取得する
now = datetime.datetime.now()
date = now.strftime('%Y-%m-%d %H:%M:00')

# 文字列の作成
exe = f"'{date}','{btc_id}','{price}'"
sql = f'insert into price_data(date,id,price) VALUES ({exe});'

# sqlに書いた処理を実行する
cur.execute(sql)

# 保存する（忘れると保存されないので注意）
c.commit()

# データベースとの接続を終了する
c.close()
print(sql, 'OK')
