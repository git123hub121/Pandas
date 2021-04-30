'''
Author: 你爸爸lzm
Date: 2020-12-21 12:43:42
Notes: 使用built命令快速得到一些常用的snippets,右击py文件可以preview代码
LastEditTime: 2020-12-21 13:41:58
'''


#处理万，转换为10000
def get_wan(x):
    if '万' in str(x):
        return (float(x[:-1])*10000)
    else:
        return float(x)

#适用于分组统计
def get_groupby(df,data,i):
    data = str(data)
    datalist = []
    data_index = df.groupby(data)[data].count().index.tolist()#[data].count() == value_counts()
    data_value = df.groupby(data)[data].count().values.tolist()
    if i == 0:
        return data_index,data_value
    #如果需要构建饼图和地图    Pie Map     构建zip
    elif i == 1:
        for data in zip(data_index,data_value):
            datalist.append(data)
    return datalist

#适用于统计tOP10,不适合写函数，因为返回值不是一个列表

