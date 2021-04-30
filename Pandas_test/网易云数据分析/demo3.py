'''
Author: 你爸爸lzm
Date: 2020-12-21 15:38:38
Notes: 使用built命令快速得到一些常用的snippets,右击py文件可以preview代码
LastEditTime: 2020-12-21 22:12:09
'''
import pandas as pd
import numpy as np

df = pd.read_csv('D:\Pandas\网易云数据分析\music_message.csv',header=0,error_bad_lines=False,names=['title','tag','text','collection','play','songs','comments'],encoding='utf-8-sig')
df.to_excel('demo.xlsx',index=False)