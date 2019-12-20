import requests
import re
from lxml import etree
import time
'''
爬取优美图网图片
分析：
    网站分三层
    首页
    图片集合页面
    图片详情页面
'''
url = "http://www.youmeitu.com"


def start_parsing(url):
    """开始解析"""
    html_req = requests.get(url)
    # print(html_req)
    get_html_url(html_req)


def get_html_url(html_req):
    """解析首页html得到图片分类集合的地址"""
    print('----------开始爬取-----------')
    html_text = etree.HTML(html_req.text)
    # url_data = html_text.xpath('//div[@class="ShowNav"]/a/@href')
    url_data = html_text.xpath('//div[@class="ShowNav"]/a/@href')
    for url_data in url_data[:3]:
        get_html_url2(url+url_data)


def get_html_url2(html_url):
    """解析网站第二层得到首页图片详情"""
    html_text =etree.HTML(requests.get(html_url).text)
    url_data =html_text.xpath('//div[@class="TypeList"]//ul/li/a/@href')
    for url_data in url_data:
        get_html_url3(url+url_data)


def get_html_url3(html_url):
    """解析图片详情页得到图片url"""
    req =requests.get(html_url)
    print(req)
    # if req.status_code ==200:
    #     html_text =etree.HTML(req.text)
    #     url_data =html_text.xpath('//div[@class="ImageBody"]//img/@src')
    #     print(url_data)


def show_data(data):
    for data in data:
        print(data)


if __name__ == '__main__':
    start_parsing(url)
