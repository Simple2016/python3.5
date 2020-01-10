import requests
import json
import random
import os

# 存放Ajax图片地址数据
from requests import RequestException

img_url_dict = {}
# 创建图片tmp文件夹
if not os.path.exists('image'):
    os.mkdir('image')


# 爬取图片url地址
def getImgurl(root_url, sn):
    params = {
        'ch': 'wallpaper',
        't1': 157,
        'sn': sn,
        'listtype': 'new',
        'temp': 1
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit / 537.36(KHTML, like Gecko)Chrome/62.0 3202.62 Safari / 537.36'
    }
    try:
        response = requests.get(root_url, params=params, headers=headers)
    except RequestException:
        return None
    print(response.text)
    data = json.loads(response.text).get('list')
    img_url_list = []
    for item in data:
        img_url_list.append(item.get('cover_imgurl'))
    img_url_dict[sn] = img_url_list


# 下载图片
def download_image(name, image_url):
    try:
        response = requests.get(image_url)
    except RequestException:
        return "图像请求出错"
    file_name = '{}/{}.{}'.format('image', name, 'bmp');
    with open(file_name, 'wb') as file:
        file.write(response.content)
    return os.path.abspath(file_name)


# 获取随机url地址并下载至image文件夹
def get_img():
    sn =random.randint(1, 30)
    print(sn)
    try:
        img_url_dict[sn]
    except KeyError:
        getImgurl('http://image.so.com/zj', sn)
    index = random.randint(0, len(img_url_dict[sn]) - 1)
    url = img_url_dict[sn][index]
    download_image('wallpaper', url)
