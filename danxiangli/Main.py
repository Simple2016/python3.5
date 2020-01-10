import datetime
import shutil

from danxiangli import bgsetter
from danxiangli import downloader
from danxiangli import imageMaker

tempFileName = r'image\template.jpg'

date = datetime.datetime.now().strftime('%Y-%m-%d')
date2 = datetime.datetime.now().strftime('%Y/%m%d')
url = 'http://img.owspace.com/Public/uploads/Download/'+date2+'.jpg'

if __name__ == '__main__':
    print('开始')
    print('copy当前桌面为模版')
    oldWallPaper = bgsetter.getOldWallPaper()
    shutil.copyfile(oldWallPaper, tempFileName)
    print('下载今天的单向历')
    download_file = downloader.download_image(date, url)
    print('合成')
    compose_file = imageMaker.compose(tempFileName, download_file)
    print('设置桌面')
    bgsetter.setWallPaper(compose_file)
    print('完成')
