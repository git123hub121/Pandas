'''
Author: 你爸爸lzm
Date: 2020-12-21 22:26:09
Notes: 使用built命令快速得到一些常用的snippets,右击py文件可以preview代码
LastEditTime: 2020-12-22 12:44:34
'''
import requests
import json
import time
import pandas as pd

target_id = "6130942571%26"#面试篇的target_id   
vid = "%3Dt0034o74jpr"#面试篇的vid  
df = pd.DataFrame()
for page in range(15, 3214, 30):  #视频时长共3214秒
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    url = 'https://mfm.video.qq.com/danmu?otype=json&timestamp={0}&target_id={1}vid{2}&count=80'.format(page,target_id,vid)
    print("正在提取第" + str(page) + "页")
    html = requests.get(url,headers = headers)
    bs = json.loads(html.text,strict = False)  #strict参数解决部分内容json格式解析报错
    time.sleep(1)
    #遍历获取目标字段
    for i in bs['comments']:
        opername = i['opername']
        content = i['content']  #弹幕
        upcount = i['upcount']  #点赞数
        user_degree =i['uservip_degree'] #会员等级
        timepoint = i['timepoint']  #发布时间
        comment_id = i['commentid']  #弹幕id
        cache = pd.DataFrame({'用户id':[opername],'弹幕':[content],'会员等级':[user_degree],'发布时间':[timepoint],'弹幕点赞':[upcount],'弹幕id':[comment_id]})
        df = pd.concat([df,cache])
df.to_csv('面试篇.csv',encoding = 'utf-8')