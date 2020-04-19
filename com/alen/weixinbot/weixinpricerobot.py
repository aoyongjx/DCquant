'''
1、微信报价机器人
wxpy github地址: https://github.com/youfou/wxpy
wxpy文档地址: https://wxpy.readthedocs.io/zh/latest/

参数:
cache_path –
设置当前会话的缓存路径，并开启缓存功能；为 None (默认) 则不开启缓存功能。
开启缓存后可在短时间内避免重复扫码，缓存失效时会重新要求登陆。
设为 True 时，使用默认的缓存路径 ‘wxpy.pkl’。
console_qr –
在终端中显示登陆二维码，需要安装 pillow 模块 (pip3 install pillow)。
可为整数(int)，表示二维码单元格的宽度，通常为 2 (当被设为 True 时，也将在内部当作 2)。
也可为负数，表示以反色显示二维码，适用于浅底深字的命令行界面。
例如: 在大部分 Linux 系统中可设为 True 或 2，而在 macOS Terminal 的默认白底配色中，应设为 -2。
qr_path – 保存二维码的路径
qr_callback – 获得二维码后的回调，可以用来定义二维码的处理方式，接收参数: uuid, status, qrcode
login_callback – 登陆成功后的回调，若不指定，将进行清屏操作，并删除二维码文件
logout_callback – 登出时的回调

'''

# 导入wxpy框架、requests网络请求框架
from wxpy import *
import os
import requests

path = os.getcwd()

# 初始化机器人.
# bot = Bot(cache_path=True, console_qr=2, qr_path='E:\02-py\51bitqunt')
bot = Bot(cache_path=True)

# 1、查找好友
# 搜索昵称为aoyongjx的朋友或搜索群名字为aoyongjx信号群的群，该群要求添加到通讯录才可以找到。
binquant = bot.friends().search('aoyongjx')[0]
bitquant_signal_group = bot.groups().search('aoyongjx')[0]

print(bitquant)
print(bitquant_signal_group)
