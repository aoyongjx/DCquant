'''
聚合行情（Ticker）
此接口获取ticker信息同时提供最近24小时的交易聚合信息。

一、请求参数
symbol：交易对

二、响应数据
id	long	NA
amount	float	以基础币种计量的交易量（以滚动24小时计）
count	integer	交易次数（以滚动24小时计）
open	float	本阶段开盘价（以滚动24小时计）
close	float	本阶段最新价（以滚动24小时计）
low	float	本阶段最低价（以滚动24小时计）
high	float	本阶段最高价（以滚动24小时计）
vol	float	以报价币种计量的交易量（以滚动24小时计）
bid	object	当前的最高买价 [price, quote volume]
ask	object	当前的最低卖价 [price, quote volume]

此性能没有websocket好
'''

import requests
# 数据处理框架
import pandas as pd
import time

# True就是可以换行显示。设置成False的时候不允许换行
pd.set_option('expand_frame_repr', False)

# 显示的最大行数和列数，如果超额就显示省略号，这个指的是多少个dataFrame的列。如果比较多又不允许换行，就会显得很乱。
pd.set_option('display.max_rows', 1000)


symbol = 'ethusdt'

url = 'https://api.huobi.pro' + '/market/detail/merged' + '?' + 'symbol=' + symbol

print(url)
resp = requests.get(url, timeout=5000)
ticker = resp.json()['tick']
print(ticker)

print(ticker['ask'])
print(ticker['bid'])

print("卖价：", ticker['ask'][0])
print("--"*10)
print("买家：", ticker['bid'][0])



while True:
    # 获取ticker
    symbol = 'ethusdt'

    # curl "https://api.huobi.pro/market/detail/merged?symbol=ethusdt"
    url = 'https://api.huobi.pro' + '/market/detail/merged' + '?' + 'symbol=' + symbol
    print(url)

    # 科学上网，网络不稳定，容易造成断网，所以加上timeout
    resp = requests.get(url, timeout=5000)
    # print(resp.json())

    ticker = resp.json()['tick']
    print(ticker)

    print(ticker['ask'])
    print(ticker['bid'])

    print("卖价：", ticker['ask'][0])
    print("--" * 10)
    print("买家：", ticker['bid'][0])

    #
    time.sleep(5)