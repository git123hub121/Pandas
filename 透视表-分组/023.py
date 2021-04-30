import pandas as pd
from datetime import date

orders = pd.read_excel('Orders.xlsx', dtype={'Date': date})
orders['Year'] = pd.DatetimeIndex(orders.Date).year
groups = orders.groupby(['Category', 'Year'])
s = groups['Total'].sum()
c = groups['ID'].count()
pt1 = pd.DataFrame({'Sum': s, 'Count': c})#这里分组得到的s，c依旧是一个series对象
pt2 = orders.pivot_table(index='Category', columns='Year', values='Total', aggfunc='sum')

print(pt1)
print(pt2)
#对呀，我可以去excel里面找透视表的灵感呀
