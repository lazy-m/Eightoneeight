from lxml import etree
import requests
import time
import json


def youdao(keyword):
    """
    有道翻译
    :param keyword: 需要翻译的单词
    :return: 翻译的结果
    """

    import requests
    import time
    import random

    # 翻译的地址
    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    # 伪装请求头
    headers = {
        'Host': 'fanyi.youdao.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest', 'Content-Length': '262', 'Connection': 'keep-alive',
        'Referer': 'http://fanyi.youdao.com/',
        'Cookie': 'YOUDAO_MOBILE_ACCESS_TYPE=1; OUTFOX_SEARCH_USER_ID=1378414660@10.108.160.19; JSESSIONID=aaaBTGxpwV4EQfnO_Oy1w; ___rl__test__cookies=1569154996426; OUTFOX_SEARCH_USER_ID_NCOO=752434577.0207007'
    }

    # 获取当前的时间戳，模仿js的(new Date).getTime()
    ts = int(time.time() * 1000)
    # 构建salt参数
    salt = ts + random.randint(0, 9)
    # 构建bv参数（通过自定义的md5方法）
    bv = md5("5.0 (Windows)")
    # 构建sign参数（通过自定义的md5方法）
    sign = md5(f'fanyideskweb{keyword}{str(salt)}n%A-rKaT5fb[Gy?;N5@Tj')
    # 所有参数字典

    data = {
        "i": keyword,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": salt,
        "sign": sign,
        "ts": salt,
        "bv": bv,
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_CLICKBUTTION"
    }

    # 请求翻译
    try:
        res = requests.post(url=url, headers=headers, data=data, timeout=10).json()
        print(res.get("translateResult")[0][0].get("src"), "----->", res.get("translateResult")[0][0].get('tgt'))
        return res.get("translateResult")[0][0]
    except Exception as e:
        print(f"抱歉有道翻译已经升级了！{e}")
        return None


def md5(keyword):
    """
    自定义的md5加密
    :param keyword:待加密的字符串
    :return: 加密后的32位字符串
    """
    import hashlib
    # 创建md5对象
    m = hashlib.md5()
    # 将字符串转为byte
    b = keyword.encode(encoding='utf-8')
    # 加密字符串
    m.update(b)
    # 获取加密结果（32位字符串）
    str_md5 = m.hexdigest()
    # 返回结果
    return str_md5


if __name__ == '__main__':
    data = youdao("应该是根据系统时间生成的一个时间戳，")
    print(data)


