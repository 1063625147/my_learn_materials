from PIL import Image  # 导入pillow库下的image模块，主要用于图片缩放、图片灰度化、获取像素灰度值
import time


def grayscale_Image(image, resize_width=8, resize_heith=8):  # image为图片的路径，resize_width为缩放图片的宽度，resize_heith为缩放图片的高度
    # image = "D:/study/python/Graduation_project" + image
    im = Image.open(image)  # 使用Image的open方法打开图片
    smaller_image = im.resize((resize_width, resize_heith))  # 将图片进行缩放
    grayscale_image = smaller_image.convert('L')  # 将图片灰度化
    return grayscale_image


def hash_String(image, resize_width=8, resize_heith=8):
    hash_string = ""  # 定义空字符串的变量，用于后续构造比较后的字符串
    pixels = list(grayscale_Image(image, resize_width, resize_heith).getdata())
    # 上一个函数grayscale_Image()缩放图片并返回灰度化图片，.getdata()方法可以获得每个像素的灰度值，使用内置函数list()将获得的灰度值序列化
    avg_number = sum(pixels) / len(pixels)

    for row in range(1, len(pixels) + 1):  # 获取pixels元素个数，从1开始遍历
        if pixels[row - 1] > avg_number:
            hash_string += '1'  # 当为真时，构造字符串为1
        else:
            hash_string += '0'  # 否则，构造字符串为0
            # 最后可得出由0、1组64位数字字符串，可视为图像的指纹
    return int(hash_string, 2)  # 把64位数当作2进制的数值并转换成十进制数值


def Difference(dhash1, dhash2):
    difference = dhash1 ^ dhash2  # 将两个数值进行异或运算
    return bin(difference).count('1')


def main(imgname):
    time1 = time.time()
    # Image1 = r'C:/Users/ye/Desktop/graduation_photos/img5.jpg'  # 待搜索图片
    grayscale_Image(imgname)
    dhash1 = hash_String(imgname)
    for i in range(530):  # 遍历图片库
        a = '/img%s.jpg' % i
        Image2 = 'static/graduation_photos' + a
        grayscale_Image(Image2)
        dhash2 = hash_String(Image2)
        count = Difference(dhash1, dhash2)
        if count < 5:
            yield Image2
        else:
            continue
    time2 = time.time()
    s_time = time2 - time1
    print('用时%s秒' % s_time)


if __name__ == '__main__':
    print(main('static/graduation_photos/img6.jpg'))
