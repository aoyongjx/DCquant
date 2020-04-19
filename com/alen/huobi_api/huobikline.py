import requests
import pandas as pd

'''
此接口返回历史K线数据。
1、请求参数
symbol：交易对	
period：返回数据时间粒度，也就是每根蜡烛的时间区间
size：返回 K 线数据条数	

2、响应数据
id：调整为新加坡时间的时间戳，单位秒，并以此作为此K线柱的id
amount：以基础币种计量的交易量
count：交易次数
open：本阶段开盘价
close：本阶段收盘价
low：本阶段最低价
high：本阶段最高价
vol	：以报价币种计量的交易量
'''

url = 'https://api.huobi.pro/market/history/kline?period=30min&size=1000&symbol=ethusdt'
resp = requests.get(url)
# print(resp)
# print(resp.json())
resp_json = resp.json()
# print(resp_json['status'])
data_list = resp_json['data']
# for data in data_list:
#     print(data)

df = pd.DataFrame(data_list)
print(df)