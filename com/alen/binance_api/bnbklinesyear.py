import requests
import time
import pandas as pd
import os

pd.set_option('expand_frame_repr', False)

# 如何获取binance过去一年的数据.  For While.

BASE_URL = 'https://api.binance.com'
limit = 1000
end_time = int(time.time() // 60 * 60 * 1000)
print(end_time)
start_time = int(end_time - limit*60*1000)
print(start_time)

while True:

    url = BASE_URL + '/api/v1/klines' + '?symbol=BTCUSDT&interval=1m&limit=' + str(limit) + '&startTime=' + str(
        start_time) + '&endTime=' + str(end_time)
    print(url)
    resp = requests.get(url)
    data = resp.json()
    df = pd.DataFrame(data, columns={'open_time': 0, 'open': 1, 'high': 2, 'low': 3, 'close': 4, 'volume': 5,
                                     'close_time': 6, 'quote_volume': 7, 'trades': 8, 'taker_base_volue': 9,
                                     'taker_quote_volume': 10, 'ignore': 11})

    df.set_index('open_time', inplace=True)

    path = os.getcwd()
    filename = path + '\\cvs\\' +  str(end_time) + '.csv'
    print("filename-->", filename)
    df.to_csv(filename)
    print(df)

    if len(df) < 1000:
        break

    end_time = start_time
    start_time = int(end_time - limit * 60 * 1000)
