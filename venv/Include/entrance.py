import requests
import re
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
}


def gat_data(url):
    """请求网页"""
    r = requests.get(url, headers=headers)
    r.encoding = "utf-8"
    # print(r.request.headers)
    # print(r.text)
    return r.text


def parsing_html(_html):
    """解析网站"""
    # url =re.findall('<a class=".*?" target=".*?" rel=".*?" href="(.*?)">',_html)
    url = re.findall('<a href="(.*?)" alt=".*?" title=".*?">', _html)
    # 下载所有的图片
    # for url in url:
    #     """下载图片本地"""
    #     time.sleep(1)
    #     # 1 通过requests下载图片
    #     img_name =url.split('/')[-1]
    #     img_ = requests.get(url,headers =headers)
    #     with open(img_name,"wb") as img:
    #         img.write(img_.content)
    # 下载第一张图片
    img_name = url[0].split('/')[-1]
    img_ = requests.get(url[0], headers=headers)
    # with open(img_name,"wb") as img:
    #     img.write(img_.content)

    # for img_url in url:
    #     print(img_url)


if __name__ == '__main__':
    html = gat_data("https://www.vmgirls.com/12985.html")
    parsing_html(html)
