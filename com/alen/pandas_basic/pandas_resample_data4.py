"""
#####################################################
Pandas对行情数据周期的转换.

官方文档： http://pandas.pydata.org/pandas-docs/stable/api.html

resample 文档：http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.resample.html?highlight=resample

#####################################################
"""

import pandas as pd

pd.set_option('expand_frame_repr', False)

df = pd.read_csv('binance_btc_1min.csv')
# print(df)
# print(df.dtypes)

df['open_time'] = pd.to_datetime(df['open_time'])

# print(df.dtypes)
# print(df)
# exit()

# df['open_time'] >= pd.to_datetime('2019-06-07 15:00:00')
df = df[df['open_time'] >= pd.to_datetime('2019-06-07 15:00:00')]  # 筛选时间周期的 df['open_time'] >= pd.to_datetime('2019-06-07 15:00:00')
# print(df)
#
# exit()

# 第一种方法，通过Series进行转换.
# 将时间周期相关的列设置为索引index
df.set_index('open_time', inplace=True)
# 周期转换方法：resample
rule_cycle = '1D'  # rule_cycle='5T'：意思是5分钟，意味着转变为5分钟数据  # 15T  1H  1D 一天

cycle_df = pd.DataFrame()
cycle_df['close'] = df['close'].resample(rule=rule_cycle).last()  # last：取这5分钟的最后一行数据
# # 开、高、低的价格，成交量
cycle_df['open'] = df['open'].resample(rule=rule_cycle).first()  # 五分钟内的第一个值就是开盘价
cycle_df['high'] = df['high'].resample(rule=rule_cycle).max()  # 五分钟内的最高价就是High
cycle_df['low'] = df['low'].resample(rule=rule_cycle).min()  # 五分钟内的最低价就是low
cycle_df['volume'] = df['volume'].resample(rule=rule_cycle).sum()  # 五分钟内的成交量的综合就是成交量

print(cycle_df)
exit()


# 通过DataFrame直接进行转换.

rule_cycle = '5T'
df.set_index('open_time', inplace=True)
cycle_df1 = df.resample(rule=rule_cycle).agg(
    {'open': 'first',
     'high': 'max',
     'low': 'min',
     'close': 'last',
     'volume': 'sum',
     })

print(cycle_df1)
# exit()

# 通过DataFrame直接进行转换.
rule_cycle = '5T'
# df.reset_index(drop=False, inplace=True)  #
cycle_df1 = df.resample(rule=rule_cycle, on='open_time').agg(
    {'open': 'first',
     'high': 'max',
     'low': 'min',
     'close': 'last',
     'volume': 'sum',
     })




cycle_df1 = cycle_df1[['open', 'high', 'low', 'close', 'volume']]
print(cycle_df1)


# 去除不必要的数据 去除一天都没有交易的周
cycle_df1.dropna(subset=['open'], inplace=True)
# 去除成交量为0的交易周期

cycle_df1 = cycle_df1[cycle_df1['volume'] > 0] # cycle_df1['volume'] > 0
print(cycle_df1)  #

"""
    B       business day frequency
    C       custom business day frequency (experimental)
    D       calendar day frequency
    W       weekly frequency
    M       month end frequency
    SM      semi-month end frequency (15th and end of month)
    BM      business month end frequency
    CBM     custom business month end frequency
    MS      month start frequency
    SMS     semi-month start frequency (1st and 15th)
    BMS     business month start frequency
    CBMS    custom business month start frequency
    Q       quarter end frequency
    BQ      business quarter endfrequency
    QS      quarter start frequency
    BQS     business quarter start frequency
    A       year end frequency
    BA      business year end frequency
    AS      year start frequency
    BAS     business year start frequency
    BH      business hour frequency
    H       hourly frequency
    T       minutely frequency
    S       secondly frequency
    L       milliseonds
    U       microseconds
    N       nanoseconds
"""
