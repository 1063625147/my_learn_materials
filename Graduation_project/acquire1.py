import requests
from bs4 import BeautifulSoup
import bs4


def GetHtml(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        # r.encoding = r.apparent_encoding
        return r.text
    except:
        return '000000'


def fillPictureList(count, html):
    soup = BeautifulSoup(html, 'html.parser')
    for item in soup.select('#gallery-list'):
        for img in item.find_all('img'):
            print('img', img)
            # m 是 img标签中存在的属性
            img_path = img.get('m')
            count.append(img_path)


def save(count):
    for i, v in enumerate(count):
        # 将获取的v值再次放入request中进行与网站相应
        image = requests.get(v)
        # 存取图片过程中，出现不能存储 int 类型，故而，我们对他进行类型转换 str()。w:读写方式打开，b：二进制进行读写。图片一般用到的都是二进制。
        with open('./static/graduation_photos/' + str(i) + '.jpg', 'wb') as file:
            # content：图片转换成二进制，进行保存。
            file.write(image.content)


def main():
    count = []
    url = 'http://travel.quanjing.com/tag/12975/%E9%A9%AC%E5%B0%94%E4%BB%A3%E5%A4%AB'
    html = GetHtml(url)
    fillPictureList(count, html)
    save(count)
    print(len(count))


main()
