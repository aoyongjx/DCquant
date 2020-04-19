"""
#####################################################
Pandas 如何批量导入数据

官方文档： http://pandas.pydata.org/pandas-docs/stable/api.html

#####################################################
"""

import pandas as pd
import os

pd.set_option('expand_frame_repr', False)

project_dir = os.path.dirname(os.path.dirname(__file__))
# print(project_dir)

csv_dir = project_dir + '/binance_api/cvs'
# print(csv_dir)

# for root, dirs, files in os.walk(csv_dir):
#     print('root:', root)  # 当前的目录
#     print('dirs:', dirs)  # 文件件加目录
#     print('files:', files)  # 文件
#     print("**"*20)
#
# print("****"*10)
# 批量读取文件名称
csv_file_paths = []

for root, dirs, files in os.walk(csv_dir):
    # 当files不为空的时候
    if files:
        for f in files:
            if f.endswith('.csv'):
                file_path = os.path.join(root, f)
                # print(file_path)
                csv_file_paths.append(file_path)


# 遍历文件名，批量导入数据
all_df = pd.DataFrame()

print(csv_file_paths)

for file in sorted(csv_file_paths):
    print(file)
    # 导入数据
    df = pd.read_csv(file)
    #  合并数据
    all_df = all_df.append(df, ignore_index=True)

# print(all_df)


# 删除重复的数据.
all_df.drop_duplicates(subset=['open_time'], inplace=True, keep='first')
# print(all_df)


all_df.sort_values(by=['open_time'], ascending=1, inplace=True)

all_df['open_time'] = pd.to_datetime(all_df['open_time'], unit='ms')
all_df = all_df[['open_time', 'open', 'high', 'low', 'close', 'volume']]


# df['open_time'] = pd.to_datetime(df['open_time'], unit='ms')
all_df.set_index('open_time', inplace=True)

all_df.to_csv('binance_btc_1min.csv')
print(all_df)
exit()