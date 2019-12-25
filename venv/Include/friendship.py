import requests
import json

data ={"translateResult":[[{"tgt":"translation","src":"翻译"}]],"errorCode":0,"type":"zh-CHS2en","smartResult":{"entries":["","translate\r\n","interpret\r\n"],"type":1}}
text =json.dumps(data)

dic={"name":"mcw","age":18}
xu=json.dumps(dic)
date =json.loads(xu)
print(date,type(date),type(data))

xs =json.dumps(data['translateResult'][0])

print(json.loads(xs)[0]['tgt'])
