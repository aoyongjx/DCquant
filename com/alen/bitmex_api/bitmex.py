import pandas as pd
import time
import ccxt

'''
ccxt-引入ccxt框架， 通过pip install ccxt 可以进行安装
https://github.com/ccxt/ccxt

加密货币交易API，支持超过120个比特币/山寨币交换

中文手册：
http://cw.hubwiz.com/card/c/ccxt-dev-manual/?spm=a2c4e.10696291.0.0.2da219a4qM1c7c

交易所API
https://www.bitmex.com/app/apiOverview

'''

# 初始化bitme交易所对象
bitmex = ccxt.bitmex()

# 请求的candles个数
limit = 500
current_time = time.time()//60 * 60 * 1000 #毫秒
# print(current_time)

# 获取请求开始的时间
since_time = current_time - limit * 60 * 1000 # 开始时间

#  'BTC/USD' 比特币对美元的交易对，或者ETH/USD 以太坊对美元的交易对.
data = bitmex.fetch_ohlcv(symbol='BTC/USD', limit=limit, since=since_time)
df = pd.DataFrame(data)
df = df.rename(columns={0: 'open_time', 1: 'open', 2: 'high', 3: 'low', 4: 'close', 5: 'volue'})

# 时间转换成北京时间
df['open_time'] = pd.to_datetime(df['open_time'], unit='ms') + pd.Timedelta(hours=8)

# 设置index(忽略第一行，字段行)
df = df.set_index('open_time', drop=True)

# 保存成csv文件(comma seperate value)
df.to_csv('bitmex_data.csv')  # comma seperate Value

print(df)