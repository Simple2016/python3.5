import time
import datetime
from danxiangli.bgsetter import setWallPaper
from danxiangli.downloader import *

if __name__ == '__main111111111111111__':
    while True:
        get_img()
        pic = 'your_path/image/wallpaper.bmp'  # 写绝对路径
        setWallPaper(pic)
        time.sleep(6)  # 6s切换一次壁纸
    print(1)
if __name__ == '__main222__':
    print('设置墙纸')
    setWallPaper('image/final.jpg')
if __name__ == '__main33333333333__':
    print('下载图片')
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    url = 'http://img.owspace.com/Public/uploads/Download/2020/0109.jpg'
    download_image(date, url)
if __name__ == '__main444444__':
    print('获取文件绝对路径')
    current_path = os.path.abspath("image/2020-01-09.bmp")
    print(current_path)
