"""
cron: 1 8,12,13-22 * * *
const $ = new Env("得见小说")
"""

import datetime
import json
import os
from pprint import pprint
import time
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import MD5, SHA1, SHA256
import base64
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; Pixel 4 Build/QD1A.190821.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36',
    'Accept-Encoding': 'gzip, deflate',
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'Host': 'dj.palmestore.com',
    'Referer': 'https://dj.palmestore.com/zycl/gold/index?zyeid=112f18c1-1969-4702-ab6c-aeeccf9a48a5&usr=j91705802&rgt=7&p1=YmkKeycIOFoDADjE6366M8lR&ku=j91705802&source=welfare&pc=10&p2=124020&p3=20000056&p4=501656&p5=19&p6=&p7=__5036784b31d92113&p9=0&p12=&p16=Pixel+4&p21=31303&p22=10&p25=20000156&p26=29&p28=&p30=&p31=__5036784b31d92113&firm=google&pca=channel-visit',
    'Cookie': '',
}


def _encrpt(string, private_key):
    priKey = RSA.importKey(private_key)
    signer = PKCS1_v1_5.new(priKey, )
    hash_obj = SHA1.new(string.encode('utf-8'))
    signature = base64.b64encode(signer.sign(hash_obj))
    return signature.decode()


def gen_body(pwd):
    '''根据账号密码生成请求的body然后调用_encrpt方法加密'''
    public_key = """MIICdQIBADANBgkqhkiG9w0BAQEFAASCAl8wggJbAgEAAoGBAMXGjyS3p+3AVnlBJe5VQ6tC9inh
8tVBve4r+yBjC5HQD6th2n3tSyuNVYaNRAFSEq+OENwnwwhjbYUnjLWb+qZscB43K1+4/WlKdvfg
wQVXm0ZQ2+jMBf+165UBEEuuWT2WqXeKkkUqPQta5lrt4eFfbo53JcOO4D5fDSGQS5bZAgMBAAEC
gYAor4I/AXEQXeLsKtTMxMmY77uIPi0gZdfWqUGOFhIJOw4eKZEzGp++I+MWPPVieCnT55vcTmm2
zg13uP0fVykmukWqZszG/ZNpPKYleOqnZOqQj7O3au8Ywz18F/pqD++PsUzxRVeXxSOOwmjQ0D2P
e/9yutz62pyiFGAzDsaI6QJBAMn8DeBT3AtcWuONdiHL3yC4NkGJDdyBbMOaWyvrcvUUZr13uS9m
ZO6pLTN6v9tkmPUdvYxcPTJ9wdGR7NcNPDsCQQD6qluGI2VAlz4s5UoDnelFKrwDPeiruE3I6wsr
asK6h37DsAE6OrQgx2dm4yH7ntJHUlJCZ5ay1EBNfEexgQv7AkA1r2vUwxVKY7q4nqHWa8SbgrrR
AmePw0qwVreC3erJHyoLk+XBpnqPQKIF+8tAueU5yTTXOLD/WZOJazrDEf5/AkBpwG+Ggu5Xtrcb
d8ynA/sDHElf0MGVmNbwOgFnWs42pa1cX6fU6ilOXvIH3TFcF6A9SMS9kThpz9QlHJaek4P7AkAa
vQillA/wnrha9GsK5UFmzmwNfkjLLW4psAUsXOsqFXWMoxTd0xWuSbuVOzERpbFMBl1VoZQmD9BL
SVOTNe+v"""
    key = '-----BEGIN PRIVATE KEY-----\n' + public_key + '\n-----END PRIVATE KEY-----'
    encrypt_res = _encrpt(pwd, key)
    return encrypt_res


# 登录
def sign():
    url = "https://dj.palmestore.com/zycl/gold/dailyWelfareV4?usr=j56126217&rgt=7&p1=Ym1c6ai%2Fb30DAETst9xTkWwY&p2=124020&p3=20000056&p4=501656&p5=19&p7=__f70b1c61e3dfa4c0&p9=0&p16=Pixel+4&p21=31303&p22=10&p25=20000156&p26=29&p31=__f70b1c61e3dfa4c0&zyeid=b0aa8ad0-f855-49ab-8be3-f8c823a66778&pca=channel-visit&ku=j56126217&kt=991ea219c912e9def1193de24640c580&firm=google&bannerType=2&signSwitch"
    resonse = requests.get(url, headers=headers)
    print(resonse.status_code)


# 登录后签到
def sign_last():
    url = 'https://dj.palmestore.com/zybk/api/bookshelf/index?usr=j56126217&sign=EpSDdolhLUMtBpOaLShXJRWOfC5zuL%2FXAzG24h0g53MRkVfWvz5RCQGjx3tIvpuoB4xoSGr2HthLxpBrHB1mpG3nE2zkN5t2CoSX6DDh%2FdriVcy1KxW7c2TZELLzdDyE9u3NKo%2Fw81ojru8yJsPHz0Ar8JB0Jx4dOmw8ERLGn4g%3D&timestamp=1653351211129&aaid=6ED5628D-A06B-AA3A-D89A-996E10EB13E8&zyeid=b0aa8ad0-f855-49ab-8be3-f8c823a66778&usr=j56126217&rgt=7&p1=Ym1c6ai%2Fb30DAETst9xTkWwY&ku=j56126217&kt=991ea219c912e9def1193de24640c580&pc=10&p2=124020&p3=20000056&p4=501656&p5=19&p6=&p7=__f70b1c61e3dfa4c0&p9=0&p12=&p16=Pixel+4&p21=31303&p22=10&p25=20000156&p26=29&p28=&p30=&p31=__f70b1c61e3dfa4c0&firm=google'
    resonse = requests.get(url, headers=headers).json()
    # print(resonse)
    re_data = resonse['body']['sign']['desc2']
    print(f'已连续签到{re_data}')
    return f'已连续签到{re_data}'


# 领三餐奖励
def three_meal():
    time1 = int(time.time() * 1000)
    sign = f"p2=124020&param=378&timestamp={time1}&usr=j56126217"
    sign1 = gen_body(sign)
    url = f'https://dj.palmestore.com/zycl/gold/receive?usr=j56126217&rgt=7&p1=Ym1c6ai%2Fb30DAETst9xTkWwY&p2=124020&p3=20000056&p4=501656&p5=19&p7=__f70b1c61e3dfa4c0&p9=0&p16=Pixel+4&p21=31303&p22=10&p25=20000156&p26=29&p31=__f70b1c61e3dfa4c0&zyeid=b0aa8ad0-f855-49ab-8be3-f8c823a66778&pca=channel-visit&ku=j56126217&kt=991ea219c912e9def1193de24640c580&firm=google&param=378&sign={sign1}&timestamp={time1}&type=sleepTask&taskId=378&coin=50'
    resonse = requests.get(url, headers=headers).json()
    # print(resonse)
    if resonse['code'] == 0:
        print(f'领三餐奖励{resonse["body"]}')
    else:
        print(resonse["msg"])


def box():
    time1 = int(time.time() * 1000)
    sign = f"p2=124020&param=50&timestamp={time1}&usr=j56126217"
    sign1 = gen_body(sign)
    url = f'https://dj.palmestore.com/zycl/gold/receive?usr=j56126217&rgt=7&p1=Ym1c6ai%2Fb30DAETst9xTkWwY&p2=124020&p3=20000056&p4=501656&p5=19&p7=__f70b1c61e3dfa4c0&p9=0&p16=Pixel+4&p21=31303&p22=10&p25=20000156&p26=29&p31=__f70b1c61e3dfa4c0&zyeid=b0aa8ad0-f855-49ab-8be3-f8c823a66778&pca=channel-visit&ku=j56126217&kt=991ea219c912e9def1193de24640c580&firm=google&param=50&sign={sign1}&timestamp={time1}&type=boxTask&incrId=50'
    resonse = requests.get(url, headers=headers).json()
    # print(resonse)
    if resonse['code'] == 0:
        print(f'开宝箱获得{resonse["body"]["coin"]}金币')
    else:
        print(resonse["msg"])
    param = 10182
    time.sleep(20)
    look_box_video(param)


def look_box_video(param):
    time1 = int(time.time() * 1000)
    sign = f"p2=124020&param={param}&timestamp={time1}&usr=j56126217"
    sign1 = gen_body(sign)
    url = f'https://dj.palmestore.com/zycl/gold/notice/video?usr=j56126217&rgt=7&p1=Ym1c6ai%2Fb30DAETst9xTkWwY&p2=124020&p3=20000056&p4=501656&p5=19&p7=__f70b1c61e3dfa4c0&p9=0&p16=Pixel+4&p21=31303&p22=10&p25=20000156&p26=29&p31=__f70b1c61e3dfa4c0&zyeid=b0aa8ad0-f855-49ab-8be3-f8c823a66778&pca=channel-visit&ku=j56126217&kt=991ea219c912e9def1193de24640c580&firm=google&param={param}&sign={sign1}&timestamp={time1}&type=globalPopVideo&videoId={param}&pos=VIDEO_POP_WINDOW'
    resonse = requests.get(url, headers=headers).json()
    if resonse['code'] == 0:
        print(f'开宝箱获得{resonse["body"]["goldNum"]}金币')
    else:
        print(resonse["msg"])


def look_video():
    time1 = int(time.time() * 1000)
    sign = f"p2=124020&param=10348-0&timestamp={time1}&usr=j56126217"
    sign1 = gen_body(sign)
    url = f'https://dj.palmestore.com/zycl/gold/receive?usr=j56126217&rgt=7&p1=Ym1c6ai%2Fb30DAETst9xTkWwY&p2=124020&p3=20000056&p4=501656&p5=19&p7=__f70b1c61e3dfa4c0&p9=0&p16=Pixel+4&p21=31303&p22=10&p25=20000156&p26=29&p31=__f70b1c61e3dfa4c0&zyeid=b0aa8ad0-f855-49ab-8be3-f8c823a66778&pca=channel-visit&ku=j56126217&kt=991ea219c912e9def1193de24640c580&firm=google&param=10348-0&sign={sign1}&timestamp={time1}&type=videoTask&videoId=10348&itemId=0&param=10348-0'
    resonse = requests.get(url, headers=headers).json()
    if resonse['code'] == 0:
        print(f'开宝箱获得{resonse["body"]["coin"]}金币,{resonse["body"]["num"]}声望')
    else:
        print(resonse["msg"])


def push_plus_bot(content):
    b = content
    headers = {
        "Host": "www.pushplus.plus",
        "Origin": "http://www.pushplus.plus",
        "Referer": "http://www.pushplus.plus/push1.html",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.44",
        "X-Requested-With": "XMLHttpRequest",

    }
    url = 'http://www.pushplus.plus/api/send'
    data = {
        "token": 'f41e605cf752414d9cc832b6c144c302',
        "title": '得见小说签到',
        "content": b,
        "channel": "wechat",
        "template": "html",
        'webhook': ""
    }
    body = json.dumps(data).encode(encoding='utf-8')
    response = requests.post(url=url, data=body, headers=headers).json()
    print(response)
    if response['code'] == 200:
        print('推送成功！')
    else:
        print('推送失败！')


def user_coin():
    time1 = int(time.time() * 1000)
    sign = f"timestamp={time1}&usr=j56126217"
    sign1 = gen_body(sign)
    url = f'https://dj.palmestore.com/zyuc/api/user/accountInfo?pluginVersion=182.0&sign={sign1}&timestamp={time1}&usr=j56126217&zyeid=b0aa8ad0-f855-49ab-8be3-f8c823a66778&usr=j56126217&rgt=7&p1=Ym1c6ai%2Fb30DAETst9xTkWwY&ku=j56126217&kt=991ea219c912e9def1193de24640c580&pc=10&p2=124020&p3=20000056&p4=501656&p5=19&p6=&p7=__f70b1c61e3dfa4c0&p9=0&p12=&p16=Pixel+4&p21=31303&p22=10&p25=20000156&p26=29&p28=&p30=&p31=__f70b1c61e3dfa4c0&firm=google'
    resonse = requests.get(url, headers=headers).json()
    pprint(resonse)
    if resonse['code'] == 0:
        print(f'得见小说目前{resonse["body"]["gold"]["goldAmount"]}金币')
        return '得见小说目前{resonse["body"]["gold"]["goldAmount"]}金币'
    # else:
    #     print(resonse["msg"])


def webhook(message, webhook_token):
    url = f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={webhook_token}'
    headers = {
        'Content-Type': 'application/json'

    }
    data = {
        "msgtype": "text",
        "text": {
            "content": message
        }
    }
    body = json.dumps(data).encode(encoding='utf-8')
    # headers = {'Content-Type': 'application/json'}
    response = requests.post(url=url, data=body, headers=headers).json()
    if response["errmsg"] == 'ok':
        print("企业微信推送成功")
    else:
        print("推送失败")


if __name__ == '__main__':
    webhook_token = os.environ['QYWX_KEY']
    cookie = os.environ["djcookie"].split("@")
    start_time = datetime.datetime.now().strftime('%H')

    header1 = {

        'Cookie': cookie
    }
    headers.update(header1)
    start_time = datetime.datetime.now().strftime('%H')
    if start_time == "08":
        three_meal()
        sign()
    elif start_time == "12":
        three_meal()
    else:
        box()
        look_video()
    mes = user_coin()
    webhook(message, webhook_token)


