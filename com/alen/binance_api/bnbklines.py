'''
K线数据

每根K线代表一个交易对。
每根K线的开盘时间可视为唯一ID

响应

[
  [
    1499040000000,      // 开盘时间
    "0.01634790",       // 开盘价
    "0.80000000",       // 最高价
    "0.01575800",       // 最低价
    "0.01577100",       // 收盘价(当前K线未结束的即为最新价)
    "148976.11427815",  // 成交量
    1499644799999,      // 收盘时间
    "2434.19055334",    // 成交额
    308,                // 成交笔数
    "1756.87402397",    // 主动买入成交量
    "28.46694368",      // 主动买入成交额
    "17928899.62484339" // 请忽略该参数
  ]
]
'''

import requests
import pandas as pd
pd.set_option('expand_frame_repr', False)

BASE_URL = 'https://api.binance.com'

kline = '/api/v3/klines'
kline_url = BASE_URL + kline + '?' + 'symbol=BTCUSDT&interval=1h&limit=50'
print(kline_url)

headers = ''

resp = requests.get(kline_url, headers=headers, timeout=500)
print(resp.json())
df = pd.DataFrame(resp.json())
print(df)
exit()