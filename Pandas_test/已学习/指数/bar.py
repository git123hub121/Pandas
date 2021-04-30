'''
Author: 你爸爸lzm
Date: 2020-12-20 14:52:58
Notes: 使用built命令快速得到一些常用的snippets,右击py文件可以preview代码
LastEditTime: 2020-12-20 18:18:36
'''
import pandas as pd
import bar_chart_race as bcr

# 读取数据
# df = pd.read_csv('word.csv', encoding='utf-8', header=None, names=['name', 'number', 'day'])
# df = pd.read_csv('area.csv', encoding='utf-8', header=None, names=['name', 'number', 'day'])
df = pd.read_csv('D:\Pandas\指数\weibo.csv', encoding='utf-8', header=None, names=['name', 'number', 'day'])

# 数据处理，数据透视表
df_result = pd.pivot_table(df, values='number', index=['day'], columns=['name'], fill_value=0)
print(df_result)

# 生成GIF
# bcr.bar_chart_race(df_result, filename='word.gif', title='爱情公寓5演职人员热度排行')
# bcr.bar_chart_race(df_result, filename='area.gif', title='国内各省市王者荣耀热度排行')
bcr.bar_chart_race(df_result, filename='weibo.gif', title='大明风华演职人员热度排行')
