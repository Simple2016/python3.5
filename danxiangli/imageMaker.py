import os

import PIL.Image as Image
import cv2
import numpy as np


# 转透明1
def transparent_back(img):
    img = img.convert('RGBA')
    L, H = img.size
    color_0 = img.getpixel((0, 0))
    for h in range(H):
        for l in range(L):
            dot = (l, h)
            color_1 = img.getpixel(dot)
            if color_1 == color_0:
                color_1 = color_1[:-1] + (0,)
                img.putpixel(dot, color_1)
    return img


# 转透明2
def transparent_back2(img):
    img = img.convert("RGBA")  # 转换获取信息
    pixdata = img.load()

    for y in range(img.size[1]):
        for x in range(img.size[0]):
            if pixdata[x, y][0] > 150 and pixdata[x, y][1] > 150 and pixdata[x, y][2] > 150 and pixdata[x, y][3] > 150:
                pixdata[x, y] = (255, 255, 255, 0)
    return img

# 转透明2 二值化
def transparent_back21(img):
    img = img.convert("RGBA")  # 转换获取信息
    pixdata = img.load()

    for y in range(img.size[1]):
        for x in range(img.size[0]):
            thresh = 200
            if pixdata[x, y][0] > thresh and pixdata[x, y][1] > thresh and pixdata[x, y][2] > thresh and pixdata[x, y][3] > thresh:
                pixdata[x, y] = (255, 255, 255, 0)
            else:
                pixdata[x, y] = (255, 255, 255, 255)
    return img



# 转透明4 使用矩阵 代替循环，提高效率
def transparent_back4(img1):
    img = img1.convert('RGBA')
    r, g, b, a = img.split()
    a0 = np.array(b)  # 转换为np矩阵
    a1 = cv2.threshold(a0, 255, 255, cv2.THRESH_BINARY)  # 设定阈值
    a2 = Image.fromarray(a1[1])  # 转换为Image的tube格式，注意为a1[1]
    a3 = np.array(a2)
    a4 = Image.fromarray(a3.astype('uint8'))  # 由float16转换为uint8
    img = Image.merge("RGBA", (b, g, r, a4))
    return img


def compose(img1, img2):
    to_image = Image.new('RGB', (1920, 1200))
    from_image = Image.open(img1)
    to_image.paste(from_image, (0, 0))
    # 图片进行翻转后合成，最后再翻转 - 为了合成到右上角
    to_image = to_image.transpose(Image.FLIP_LEFT_RIGHT)
    from_image = Image.open(img2).resize((372, 600), Image.ANTIALIAS)
    from_image = from_image.transpose(Image.FLIP_LEFT_RIGHT)
    # from_image = transparent_back2(from_image)
    to_image.paste(from_image, (0, 50))
    # to_image.paste(from_image, (0, 50), from_image)
    to_image = to_image.transpose(Image.FLIP_LEFT_RIGHT)
    image_save = os.path.abspath('image/final.jpg')
    to_image.save(image_save)
    return image_save

#合成png(透明)图片，并保存为jpg格式
def composePngToJpg(img1, img2):
    to_image = Image.new('RGBA', (1920, 1200)) #RGBA
    from_image = Image.open(img1)
    to_image.paste(from_image, (0, 0))
    # 图片进行翻转后合成，最后再翻转 - 为了合成到右上角
    to_image = to_image.transpose(Image.FLIP_LEFT_RIGHT)
    from_image = Image.open(img2)
    from_image = transparent_back21(from_image)  # 转换白色为透明
    from_image=from_image.resize((420, 700), Image.ANTIALIAS)
    from_image = from_image.transpose(Image.FLIP_LEFT_RIGHT)
    to_image.paste(from_image, (0, 20), from_image) #最后一个参数为蒙版
    to_image = to_image.transpose(Image.FLIP_LEFT_RIGHT)
    image_save = os.path.abspath('image/final.jpg')
    to_image=to_image.convert('RGB')
    to_image.save(image_save)
    return image_save


if __name__ == '__main__':
    compose()
