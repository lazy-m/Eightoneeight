import requests


def friendship(url):
    wordes = {
        # i: 苹果
        # from: AUTO
        # to: AUTO
        # smartresult: dict
        # client: fanyideskweb
        # salt: 15761247058465
        # sign: 49
        # fc1824090c2eb1063694918ae4e86e
        # ts: 1576124705846
        # bv: ca3dedaa9d15daa003dbdaaa991540d1
        # doctype: json
        # version: 2.1
        # keyfrom: fanyi.web
        # action: FY_BY_CLICKBUTTION
        "i": "苹果",
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "15761247058465",
        "sign": "49fc1824090c2eb1063694918ae4e86e",
        "ts": "1576124705846",
        "bv": "ca3dedaa9d15daa003dbdaaa991540d1",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_CLICKBUTTION"

    }
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": "258",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "P_INFO=m18201781171@163.com|1567489754|0|other|00&99|null&null&null#shh&null#10#0#0|182171&1|qn&qn_qrcode&mtoken_client|18201781171@163.com; OUTFOX_SEARCH_USER_ID=-244319722@10.169.0.83; OUTFOX_SEARCH_USER_ID_NCOO=995075801.2015764; JSESSIONID=aaaVfklMV1P8X4vZvq47w; ___rl__test__cookies=1576124705841",
        "Host": "fanyi.youdao.com",
        "Origin": "http://fanyi.youdao.com",
        "Referer": "http://fanyi.youdao.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
    req = requests.post(url, data=wordes, headers=headers)
    req.encoding = "utf-8"
    print(req)
    print(req.text)


if __name__ == '__main__':
    friendship("http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule")
