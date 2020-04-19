import wxpy  # pip install -U wxpy 或者 pip install -U wxpy -i "https://pypi.doubanio.com/simple/"

"""
1.  wxpy github地址: https://github.com/youfou/wxpy
2.  wxpy文档地址: https://wxpy.readthedocs.io/zh/latest/
2.  要有两个微信才能测试, 其中一个微信必须是老号，且要经过实名认证, 身份证和银行卡， 另一个作为测试使用
    新号老号都可以.
    
"""

from wxpy import *
import requests

bot = Bot(cache_path=True, console_qr=-2)  # Bot() #


# # 查找好友.
bitquant = bot.friends().search('51bitquant')[0]  # 搜索昵称为51bitquant的朋友
bitquant_signal_group = bot.groups().search('51bitquant信号群')[0]  # 搜索群名字为51bitquant信号群的群，该群要求添加到通讯录才可以找到。

print(bitquant)
# print(bitquant_signal_group)
#
# # 发送信息, 通过send的方法
bitquant.send("Hello world")  # 当前登录的这个微信账号，给他发送信息.  给bitquant发送信息
#
# # 注册相应的信息
#
# @bot.register()  # 装饰器.
# def print_others(msg):
#     print('收到的其他信息:-->', msg)

#
# # 回复 my_friend 的消息 (优先匹配后注册的函数!)
# @bot.register([bitquant])
# def reply_my_friend(msg):
#     if msg.type == 'Text':
#         print("收到的信息：", msg.text)
#         content = msg.text.replace('吗', '')
#         content = content.replace('?', '!')  # 英文的问号?
#         content = content.replace('？', '!')  # 中文的问号？
#         print("回复的信息：", content)
#
#         return content
#
# 自动接受新的好友请求
# @bot.register(msg_types=FRIENDS)
# def auto_accept_friends(msg):
#     # 接受好友请求
#     new_friend = msg.card.accept()
#     # 向新的好友发送消息
#     new_friend.send('哈哈，我自动接受了你的好友请求')

# @bot.register([bitquant, bitquant_1], msg_types=TEXT), 注册多个人的信息， 且只处理TEXT文字类型.


BASE_URL = 'https://api.huobi.br.com'
currencys_url = BASE_URL + '/v1/common/currencys'
resp = requests.get(currencys_url)
currencys = []
if resp.status_code == 200:
    currencys = resp.json()['data']

print(currencys)

# btcusdt

#  bchusdt --> bchbtc --> bcheth
def request_symbol_price(symbol, sender):

    try:
        resp = requests.get(BASE_URL+'/market/detail/merged'+'?symbol='+symbol+'usdt')
        if resp.status_code == 200:
            tick = resp.json()['tick']
            price_str = "火币"+ symbol+'/usdt'+'价格为: ', tick['bid'][0]
            print(price_str)
            sender.send(price_str)
    except Exception as error:
        try:
            resp = requests.get(BASE_URL + '/market/detail/merged' + '?symbol=' + symbol + 'btc')
            if resp.status_code == 200:
                tick = resp.json()['tick']
                price_str = "火币" + symbol + '/btc' + '价格为: ', tick['bid'][0]
                print(price_str)
                sender.send(price_str)
        except Exception as error:
            try:
                resp = requests.get(BASE_URL + '/market/detail/merged' + '?symbol=' + symbol + 'eth')

                if resp.status_code == 200:
                    tick = resp.json()['tick']
                    price_str = "火币" + symbol + '/eth' + '价格为: ', tick['bid'][0]
                    print(price_str)
                    sender.send(price_str)
            except Exception as error:
                pass


@bot.register([bitquant, bitquant_signal_group], msg_types=TEXT)
def receive_message(msg: Message):
    txt = msg.text
    sender = msg.sender
    print(msg.sender)
    print(msg.text)
    if txt in currencys:
        request_symbol_price(txt, sender)


embed()  # 进入 Python 命令行、让程序保持运行