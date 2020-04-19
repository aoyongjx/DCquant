"""
#####################################################
Pandas 2

DataFrame shift、 diff、pct_change函数
如何删除列、 还有数据排序、合并DataFrame、删除重复数据、reset_index重置索引、set_index设置索引

官方文档： http://pandas.pydata.org/pandas-docs/stable/api.html

#####################################################
"""
import pandas as pd
import os

pd.set_option('expand_frame_repr', False)  # 当列太多时不换行
# pd.set_option('display.max_rows', 1000)  # 最多显示行数.
# pd.set_option('precision', 6)  # 浮点数的精度】
# pd.set_option('display.float_format', lambda x:'%.2f' % x)  # 设置不用科学计数法，保留两位小数.

# print(os.path.dirname(__file__))

current_dir = os.path.dirname(os.path.dirname(__file__))
print(current_dir)

# file_name = '1560038820000.csv'
#
# path = current_dir + '/binance_api/' + file_name

path = 'E:\\02-py\\51bitqunt\\binance_api\\cvs\\1586495340000.csv'
# /Users/wanglin/51bitquant/51bitqunt/binance_api/1560038820000.csv
# /Users/wanglin/51bitquant/51bitqunt/binance_api/1560038820000.csv

df = pd.read_csv(filepath_or_buffer=path)

df = df[['open_time', 'open', 'high', 'low', 'close', 'volume']]
# print(df)
# exit()


# shift类函数
# df['下个close'] = df['close'].shift(-1)  # shift 表示移动，负数表示向上移动，正数表示向下移动
# df['上个close'] = df['close'].shift(1)
# print(df)
# # 读取上一行的数据，若参数设定为3，就是读取上三行的数据；若参数设定为-1，就是读取下一行的数据
# print(df)

# exit()
# 删除某一列
# del df['下个close']  # 删除某一列的方法  del  dict
# df = df[['open_time', 'open', 'high', 'low', 'close', 'volume', '下个close']]
# print(df)
# df.drop(['上个close'], axis=1, inplace=True)  # 删除某一列的另外一种方式，inplace参数指是否替代原来的df
# print(df)


# diff 计算价格涨跌
# df['涨跌'] = df['close'].diff(0)  # 跟自己比较 difference
# print(df)

# df['涨跌'] = df['close'].diff(-1)  # 当前的close 减去shift(-1)
# print(df)
# df['shift-1'] = df['close'].shift(-1)
# df['涨跌计算'] = df['close'] - df['shift-1']
# print(df)

# 涨跌幅度
# df['涨跌幅'] = df['close'].pct_change(1)  # 类似于diff，但是求的是两个数直接的比例，相当于求涨跌幅  pct  = percentage change
# print(df)
#
# df['shift1'] = df['close'].shift(1)
# df['涨跌幅计算'] = (df['close'] - df['shift1'])/df['close']
# print(df)


# cum(cumulative)类函数  accumulative
# df['volume_cum'] = df['volume'].cumsum()  # 该列的累加值
# print(df[['volume', 'volume_cum']])
# df['涨'] = (df['涨跌幅'] + 1.0).cumprod()  # 累乘 product 乘积的意思 产品
# print(df)


# 排序函数
# print(df.sort_values(by=['open_time'], ascending=1))  # by参数指定按照什么进行排序，acsending 上升的意思,参数指定是顺序还是逆序，1顺序，0逆序
# print(df.sort_values(by=['volume', 'open_time'], ascending=[0, 0]))  # 按照多列进行排序
# print(df)


# 多个DataFrame上下合并操作，append操作

# df1 = pd.read_csv(filepath_or_buffer=current_dir + '/binance_api/1560218820000.csv')
# df2 = pd.read_csv(filepath_or_buffer=current_dir + '/binance_api/1560278820000.csv')
# print(df1)
# print(df2)

# df3 = df1.append(df2)  # # append操作，将df1和df2上下拼接起来。注意观察拼接之后的index。index可以重复
# print(df3)
# df3 = df1.append(df2, ignore_index=True)  # ignore_index参数，用户重新确定index
# # print(df3)
# df4 = df3.append(df2, ignore_index=True)
# print(df3)
# print(df4)
# =====对数据进行去重
# df3中有重复的行数，我们如何将重复的行数去除
# df4.drop_duplicates(  # duplicates
#     subset=['open_time'],  # subset参数用来指定根据哪类类数据来判断是否重复。若不指定，则用全部列的数据来判断是否重复
#     keep='first',  # 在去除重复值的时候，我们是保留上面一行还是下面一行？first保留上面一行，last保留下面一行，False就是一行都不保留
#     inplace=True
# )
# print(df4)


# =====其他常用重要函数

# df4.reset_index(inplace=True, drop=False)  # 重置index, 是否保留之前的index
# df4.reset_index(inplace=True, drop=True)  # 重置index, 是否保留之前的index
# print(df4)

# df4.set_index('open_time', inplace=True)
# print(df4)

# print(df4rename.(columns={'close': '收盘价', 'open': '开盘价'}))  # rename函数给变量修改名字。使用dict将要修改的名字传给columns参数
# print(df.empty)  # 判断一个df是不是为空，此处输出不为空
# df0 = pd.DataFrame()
# print(df0)
# print(df0.empty)
# print(pd.DataFrame().empty)  # pd.DataFrame()创建一个空的DataFrame，此处输出为空
# print(df.T)  # 转置 将数据转置，行变成列
