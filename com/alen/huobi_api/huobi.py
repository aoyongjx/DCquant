"""
什么是API： Application Programming Interface, 应用程序接口.
简单的说是通过  网络请求  给定的资源路径  可以获取到数据或者跟服务器进行 数据交换或者交互

火币文档介绍：https://huobiapi.github.io/docs/spot/v1/cn/#185368440e
baseURL: https://api.huobi.pro   # 科学上网
         https://api.huobi.br.com 
    
限频规则 : 现货/杠杆（api.huobi.pro) 10秒100次  单个API Key 维度限制

"""


"""
python3.7演示 获取火币的api行情数据
"""

# BASEURL = 'https://api.huobi.br.com'
# currencys = '/v1/common/currencys'
#
# currencys_url = BASEURL + currencys
# print(currencys_url)
# import requests
#
# resp = requests.get(currencys_url)
# print(resp)
# print(resp.status_code)
# print(resp.json())
# r_json = resp.json()
# data = r_json['data']
# # print(data)
# # print()
# for d in data:
#     print(d)

# 1、先在pycharm安装requests,pandas
import requests
# 数据处理框架
import pandas as pd
import time

# True就是可以换行显示。设置成False的时候不允许换行
pd.set_option('expand_frame_repr', False)

# 显示的最大行数和列数，如果超额就显示省略号，这个指的是多少个dataFrame的列。如果比较多又不允许换行，就会显得很乱。
pd.set_option('display.max_rows', 1000)

# 请求行数据， Kline data

# url = 'https://api.huobi.br.com/market/history/kline?period=30min&size=1000&symbol=ethusdt'
# resp = requests.get(url)
# # print(resp)
# # print(resp.json())
# resp_json = resp.json()
# # print(resp_json['status'])
# data_list = resp_json['data']
# # for data in data_list:
# #     print(data)
#
# df = pd.DataFrame(data_list)
# print(df)

# /Users/wanglin/anaconda3/lib/python3.7/site-packages/ccxt/base/exchange.py",

# 获取ticker
# 重要：需要科学上网
# 聚合行情（Ticker）
# 此接口获取ticker信息同时提供最近24小时的交易聚合信息。HTTP 请求 GET /market/detail/merged
# 参考：https://huobiapi.github.io/docs/spot/v1/cn/#k
# curl "https://api.huobi.pro/market/detail/merged?symbol=ethusdt"
symbol = 'ethusdt'
# url = 'https://api.huobi.br.com' + '/market/detail/merged' + '?' + 'symbol=' + symbol

# curl "https://api.huobi.pro/market/detail/merged?symbol=ethusdt"
url = 'https://api.huobi.pro' + '/market/detail/merged' + '?' + 'symbol=' + symbol

print(url)
resp = requests.get(url, timeout=5000)
# print(resp.json())

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
    time.sleep(5)


# import requests
# import pandas as pd
# pd.set_option('expand_frame_repr', False)
# pd.set_option('display.max_rows', 1000)
#
#
# resp = requests.get("https://api.huobi.br.com/market/history/kline?period=1day&size=200&symbol=btcusdt")
# print(resp.status_code)
# resp_json = resp.json()
# print(resp_json['status'])
#
# df = pd.DataFrame(resp_json['data'])
# print(df)
