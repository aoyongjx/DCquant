from wxpy import *
import requests



BASE_URL = 'https://api.huobi.pro'
currencys_url = BASE_URL + '/v1/common/currencys'
resp = requests.get(currencys_url)
currencys = []
if resp.status_code == 200:
    currencys = resp.json()['data']

print(currencys)


#  bchusdt --> bchbtc --> bcheth
def request_symbol_price(symbol):
    try:
        resp = requests.get(BASE_URL + '/market/detail/merged' + '?symbol=' + symbol + 'usdt')
        if resp.status_code == 200:
            tick = resp.json()['tick']
            price_str = "火币" + symbol + '/usdt' + '价格为: ', tick['bid'][0]
            print(price_str)
    except Exception as error:
        try:
            resp = requests.get(BASE_URL + '/market/detail/merged' + '?symbol=' + symbol + 'btc')
            if resp.status_code == 200:
                tick = resp.json()['tick']
                price_str = "火币" + symbol + '/btc' + '价格为: ', tick['bid'][0]
                print(price_str)
        except Exception as error:
            try:
                resp = requests.get(BASE_URL + '/market/detail/merged' + '?symbol=' + symbol + 'eth')

                if resp.status_code == 200:
                    tick = resp.json()['tick']
                    price_str = "火币" + symbol + '/eth' + '价格为: ', tick['bid'][0]
                    print(price_str)
            except Exception as error:
                pass


# def receive_message(tex):
#     print(txt)
#     if txt in currencys:
#         request_symbol_price(txt)
#
# embed()  # 进入 Python 命令行、让程序保持运行

while True:
    c = input('请输入将查询的币种>>>')
    request_symbol_price(c)