import pandas as pd  # 别名
# print(pd.__version__)

pd.set_option('expand_frame_repr', False)  # 当列太多时不换行
pd.set_option('display.max_rows', 1000)  # 最多显示行数.
# pd.set_option('precision', 6)  # 浮点数的精度】
pd.set_option('display.float_format', lambda x:'%.2f' % x)  # 设置不用科学计数法，保留两位小数.

#更多设置可以参考文档：http://pandas.pydata.org/pandas-docs/stable/user_guide/options.html

# =====导入数据
import os
print(os.path.dirname(__file__))
print(os.path.dirname(os.path.dirname(__file__)))

# comma separate value ,

df = pd.read_csv(filepath_or_buffer= '../binance_api/1559978820000.csv',  # '/Users/wanglin/51bitquant/51bitqunt/binance_api/1559978820000.csv',
                 skiprows=1,
                 # usecols=['open_time', 'open', 'close', 'high', 'low', 'volume'],
                 # nrows=10
                 )
# pd.read_excel()
# pd.read_hdf()

print(df)

# df = pd.read_csv(
    # 该参数为数据在电脑中的路径
    # filepath_or_buffer='/Users/wanglin/51bitquant/51bitqunt/binance_api/1559978820000.csv', # 绝对路径.
    # filepath_or_buffer='../binance_api/1559978820000.csv',  # 相对路径

    # skiprows=1,
    # sep=sep,  ,  ;
    # delimiter=None,
    # Column and Index Locations and Names
    # header='infer',
    # names=None,
    # index_col=None,
    # usecols=None,
    # squeeze=False,
    # prefix=None,
    # mangle_dupe_
    # General Parsing Configuration
    # dtype=None,
    # engine=None,
    # converters=None,
    # true_values=None,
    # false_values=None,
    # skiprows=None,
    # skipfooter=0,
    # nrows=None,
    # # NA and Missing Data Handling
    # na_values=None,
    # keep_default_na=True,
    # na_filter=True,
    # verbose=False,
    # skip_blank_lines=True,
    # # Datetime Handling
    # parse_dates=False,
    # infer_datetime_format=False,
    # keep_date_col=False,
    # date_parser=None,
    # dayfirst=False,
    # Error Handling
    # error_bad_lines=True,
    # warn_bad_lines=True,
# )


# 还可以导入 read_table、read_excel、read_json

# print(df)
# print(df.dtypes)


# =====看数据
# print(df.shape)  # 输出dataframe有多少行、多少列。
# print(df.shape[0])

# print(df.columns)  # 顺序输出每一列的名字
# for col in df.columns:
#     print(col)
# print(df.index)  # 顺序输出每一行的名字
# for index in df.index:
#     print(index)
#


# print(df.dtypes)  # 数据每一列的类型不一样，比如数字、字符串、日期等。该方法输出每一列变量类型
# print(df.head())  # 默认是5。与自然语言很接近
# print(df.head(3))  #  看前3行的数据
# print(df.tail(3))  # 看最后3行的数据，默认是5。
# print(df.sample(n=3))  # 随机抽取3行，
# print(df.sample(frac=0.3))  # 想要去固定比例的话，可以用frac参数
# print(df.describe())  # 非常方便的函数，对每一列数据有直观感受；只会对数字类型的列有效


################## Pandas对数据的访问和操作######################
# print(df)
# =====如何选取指定的行、列
# print(df['open'])  # 根据列名称来选取，读取的数据是Series类型
# print(df['open', 'open_time'])
# print(df[['open_time', 'close']])  # 同时选取多列，需要两个括号，读取的数据是DataFrame类型


# 增加列
# df["mark"] = "北京时间"
# df["exchange"] = "Binance"
# nums = [i for i in range(0, 940, 1)]
# df['number'] = nums
# print(df)

# 对列进行计算

df['rmb_price'] = df['close'] *7

# print(df['close'] * 7)  # 数字列直接加上或者乘以数字，对整列进行操作。
df['total_trade'] = (df['close'] * df['volume'])  # 计算两类的乘积。

df = df[['open_time', 'open', 'high', 'low', 'close', 'rmb_price', 'total_trade',  'volume']]  # 对列的数据进行筛选和显示.
# print(df)
# print(df.dtypes)
# 时间计算.

df['open_time'] = pd.to_datetime(df['open_time'], unit='ms')  # UTC 0时区的时间，格林威治的时间。
# print(df)

df['open_time'] = df['open_time'] + pd.Timedelta(hours=8)
# df['open_time'] = pd.to_datetime(df['open_time'], unit='ms')  # unit of the arg (D,s,ms,us,ns)

# 增加一天，Timedelta用于表示时间差数据，[weeks, days, hours, minutes, seconds, milliseconds, microseconds, nanoseconds]

# print(df)
# print(df.dtypes)

print(df)
# # iloc操作：通过position来读取数据  loc
# print(df.iloc[0])  # 以index选取某一行，读取的数据是Series类型
# print(df.iloc[0]['open'])  # 获取某一行某一列的元素的值
# print(df.iloc[1:3])  # 选取在此范围内的多行，读取的数据是DataFrame类型
# print(df.iloc[:, 1:3])  # 选取在此范围内的多列，读取的数据是DataFrame类型
# print(df.iloc[1:3, 1:3])  # 读取指定的多行、多列，读取的数据是DataFrame类型
# print(df.iloc[:, :])  # 读取所有行、所有列，读取的数据是DataFrame类型
# print(df.iloc[-1])  # 获取最后一行的数据
# print(df.iat[1, 1])  # 使用iat读取指定的某个元素。使用iloc也行，但是iat更高效。
#


# =====统计函数
print(df['close'].mean())  # 求一整列的均值，返回一个数。会自动排除空值。
print(df[['close', 'volume']].mean())  # 求两列的均值，返回两个数
# print(df[['close', 'volume']])


# print(df[['close', 'volume']].mean(axis=1))  # 求两列的均值, axis=0或者1要搞清楚。
# df['close_V'] = df[['close', 'volume']].mean(axis=1)
# print(df)
# axis=1，代表对整几列进行操作。axis=0（默认）代表对几行进行操作。
# 实际中弄混很正常，多去试下，打印出来观察下.

print(df['high'].max())  # 最大值
print(df['low'].min())  # 最小值
print(df['close'].std())  # 标准差
print(df['close'].count())  # 非空的数据的数量
print(df['close'].median())  # 中位数
print(df['close'].quantile(0.25))  # 25%分位数
# 还有其他的函数计算其他的指标，在实际使用中遇到可以自己搜索

