from lxml import etree
import requests
import time

# url = "http://www.youmeitu.com"
#
# req = requests.get(url)
# html = etree.HTML(req.text)
# # print(etree.tostring(html).decode('utf-8'))
# # test = html.xpath('/html/head/title')
# # test = html.xpath('//title[@lang="en"]/text()')#获取文本
# # data_url = html.xpath('//div[@class="ShowNav"]/a/@href')
# data_img_url = html.xpath('//img/@src')
#
#
# def print_data(data):
#     for data in data:
#         print(url + data)
#
#
# print_data(data_img_url)

def te(i):
    time.sleep(1)
    i +=1
    print(i)
    if i<10:
        te(i)


if __name__ == '__main__':
    te(1)