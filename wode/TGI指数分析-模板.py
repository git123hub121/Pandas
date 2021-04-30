import pandas as pd
df = pd.read_excel('Pandas/06 TGI指数分析实战/TGI/TGI指数案例数据.xlsx')
# df.head()
#去除无效数据---交易失败
df = df.loc[df['订单状态']=='交易成功',:]
df_m = df.groupby('买家昵称')['实付金额'].mean().reset_index()
df_m['客单类别'] = ['高客单' if x>50 else '低客单' for x in list(df_m['实付金额'])]
df_c = df.drop_duplicates(subset='买家昵称')
df_c = df_c[['买家昵称','省份','城市']]
df_mc = pd.merge(df_m,df_c,left_on='买家昵称',right_on='买家昵称',how='left')
df_mc = df_mc[['买家昵称','客单类别','省份','城市']]
p_table = pd.pivot_table(df_mc,index=['省份','城市'],columns='客单类别',aggfunc='count')
gkd = p_table['买家昵称']['高客单'].reset_index()
dkd = p_table['买家昵称']['低客单'].reset_index()
result = pd.merge(gkd,dkd,left_on=['省份','城市'],right_on=['省份','城市'],how='inner')
#
result['客单总数'] = result['高客单']+result['低客单']
result['占比'] = result['高客单']/result['客单总数']
result = result.dropna()
#
result['总占比'] = result['高客单'].sum()/result['客单总数'].sum()
#
result['最终占比'] = result['占比']/result['总占比']*100
#对数据进行清洗
result = result.loc[(result['高客单']>result['高客单'].mean())&(result['客单总数']>result['客单总数'].mean()),:].sort_values('最终占比',ascending=False)
print(result.head())