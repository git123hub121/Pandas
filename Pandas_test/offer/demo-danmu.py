'''
Date: 2020-12-21 23:27:59
LastEditTime: 2020-12-22 16:36:43
'''
import requests
import json
import time
import pandas as pd
  

def get_danmu_all_page(target_id, vid,filename):
    df = pd.DataFrame()
    for page in range(15, 20000, 30):  #亲测有效
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
        url = 'https://mfm.video.qq.com/danmu?otype=json&timestamp={0}&target_id={1}vid{2}&count=80'.format(page,target_id,vid)
        print("正在提取第" + str(page) + "页")
        html = requests.get(url,headers = headers)
        bs = json.loads(html.text,strict = False)  #strict参数解决部分内容json格式解析报错
        time.sleep(0.5)
        #遍历获取目标字段
        try:
            for i in bs['comments']:
                opername = i['opername']
                content = i['content']  #弹幕
                upcount = i['upcount']  #点赞数
                user_degree =i['uservip_degree'] #会员等级
                timepoint = i['timepoint']  #发布时间
                comment_id = i['commentid']  #弹幕id
                cache = pd.DataFrame({'用户id':[opername],'弹幕':[content],'会员等级':[user_degree],'发布时间':[timepoint],'弹幕点赞':[upcount],'弹幕id':[comment_id]})
                df = pd.concat([df,cache])
        except Exception as e:
            break
    # df.to_csv(f'{filename}.csv',encoding = 'utf-8')
    return df
#自己按需添加
target_id = ['6130942571%26','6164313448%26','6194952391%26','6227063464%26']
vid = ['%3Dt0034o74jpr','%3Dr00346rvwyq','%3Dd0035rctvoh','%3Db0035j0tgo0']
filename = ['面试篇','第1期','第2期','第3期']
df = pd.DataFrame()
for i in range(len(vid)):
    df = get_danmu_all_page(target_id=target_id[i], vid=vid[i],filename=filename[i])#df{}.format(data_dm[i])
    df.insert(0, '所属期数', filename[i])
    df.to_csv(f'{filename[i]}.csv',index=False)
