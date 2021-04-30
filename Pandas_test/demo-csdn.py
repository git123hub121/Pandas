import requests
import base64
import json
import cv2
from PIL import Image
from moviepy.editor import VideoFileClip
from moviepy.editor import AudioFileClip
import time
shipin = 'f4.mp4'
#视频名称
shiPin = cv2.VideoCapture(shipin)
#捕捉视频
totalZhen = int(float(str(shiPin.get(7))))
#总帧数
for j in range(totalZhen):
    ret,frame = shiPin.read()
    cv2.imwrite('taotao'+str(j)+'.jpg',frame)
    j += 1
    print('正在打印第%d张'%j)
shiPin.release()
print('图片切片完成共%d----------'%totalZhen)
#要替换的图片
img = 'meinv.jpg'
for i in range(totalZhen):
    taoimg = 'taotao%d.jpg'%(i)
    url = 'https://api-cn.faceplusplus.com/imagepp/v1/mergeface'
    with open(taoimg,'rb') as f:
        taoimgface = base64.b64encode(f.read())
    with open(img,'rb') as f:
        taoimgface2 = base64.b64encode(f.read())
    data = {
        'api_key':'8QM0Bs2XKEE_AWRVHoeHVuW8yFHOfnJ9',
        'api_secret':'GOoaKKHbOlMMzCUAgHofdXQn4gcjQAe0',
        'template_base64':taoimgface,
        'merge_base64':taoimgface2,
        'merge_rate':30,
        'feature_rate':30
    }
    time.sleep(0.5)
    response = requests.post(url,data).text
    #接口调用
    contents = json.loads(response)['result']
    contents = contents.encode()
    taoimg2 = taoimg.replace('taotao','taotao_new')
    with open(taoimg2,'wb') as f:
        f.write(base64.b64encode(contents))
print('所有图片渲染完成-------')

print('开始合成视频------')
fourcc = cv2.VideoWriter_fourcc(*'mp4')
video = cv2.VideoWriter('taotaonew.mp4',fourcc,30,(1920,1080))
for i in range(totalZhen+1):
    path = str(i)+'.jpg'
    img = cv2.imread(path)
    #写入视频
    video.write(img)
video.release()
print('合成视频完成------')
#有视频，但是播放不了
