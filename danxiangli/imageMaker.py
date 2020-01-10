import os

import PIL.Image as Image


def compose(img1,img2):
    to_image = Image.new('RGB', (1920, 1200))
    from_image = Image.open(img1)
    to_image.paste(from_image, (0, 0))
    # 图片进行翻转后合成，最后再翻转 - 为了合成到右上角
    to_image = to_image.transpose(Image.FLIP_LEFT_RIGHT)
    from_image = Image.open(img2).resize((372, 600), Image.ANTIALIAS)
    from_image = from_image.transpose(Image.FLIP_LEFT_RIGHT)
    to_image.paste(from_image, (0, 50))
    to_image = to_image.transpose(Image.FLIP_LEFT_RIGHT)
    image_save = os.path.abspath('image/final.jpg')
    to_image.save(image_save)
    return image_save


if __name__ == '__main__':
    compose()
