"""
cron: 1 6 * * *
const $ = new Env("掌上天津")
"""

import json
import time, base64, hashlib, execjs, urllib.parse, os
import hmac
from hashlib import sha1
import requests


js_function = """
function genmac(){var ran1=ran1=Math.floor(Math.random()*256);ran1=ran1.toString(16).toUpperCase();if(ran1.length==1)ran1="0"+ran1;var ran2=Math.floor(Math.random()*256);ran2=ran2.toString(16).toUpperCase();if(ran2.length==1)ran2="0"+ran2;var ran3=Math.floor(Math.random()*256);ran3=ran3.toString(16).toUpperCase();if(ran3.length==1)ran3="0"+ran3;var ran4=Math.floor(Math.random()*256);ran4=ran4.toString(16).toUpperCase();if(ran4.length==1)ran4="0"+ran4;var ran5=Math.floor(Math.random()*256);ran5=ran5.toString(16).toUpperCase();if(ran5.length==1)ran5="0"+ran5;var ran6=Math.floor(Math.random()*256);ran6=ran6.toString(16).toUpperCase();if(ran6.length==1)ran6="0"+ran6;var res="";res=ran1+":"+ran2+":"+ran3+":"+ran4+":"+ran5+":"+ran6;return res;}
"""


def sha1_secret_str(key, code):
    hmac_code = hmac.new(key.encode(), code, sha1)
    return hmac_code.hexdigest()


def sign_data(userId, salf):
    macs = execjs.compile(js_function).call("genmac")
    macs = urllib.parse.quote(macs, 'utf-8')
    timestamp = str(int(time.time()))
    sa = f'brand=google&client=android&deviceInfo=google_Pixel 4_5831595_10&interfaceVersion=v2.8&lat=40.14988&lng=116.658974&mac={macs}&model=Pixel 4&privacyStatus=1&region=%E9%A1%BA%E4%B9%89%E5%8C%BA&salf={salf}&timestamp={timestamp}&uid={userId}&userId={userId}&version=2.8.4&versionCode=154'
    # sa = 'brand=OPPO&client=android&deviceInfo=OPPO_PCAM00_2021040100_10&interfaceVersion=v2.8&lat=30.1&lng=114.2&mac=16:20:B8:EA:31:57&model=PCAM00&privacyStatus=1&region=天津市&salf=9e2e14&timestamp=1675259130&uid=454242&userId=454242&version=2.8.4&versionCode=154'
    s = bytes(sa, encoding='utf-8')
    code = base64.b64encode(s)
    key = "1s_vsegymTasdgKxiKvRz5vDlyzmc92A_H6A8zg6I"
    signs = sha1_secret_str(key, code).upper()
    url = f"https://bbs.zaitianjin.net/zstj/v2.8/index.php"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'bbs.zaitianjin.net',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/4.9.3'
    }
    data = {
        'c': 'User',
        'lng': '116.658974',
        'privacyStatus': '1',
        'sign': signs,
        'interfaceVersion': 'v2.8',
        'version': '2.8.4',
        'userId': userId,
        'm': 'signInfo',
        'mac': macs,
        'versionCode': '154',
        'deviceInfo': 'google_Pixel 4_5831595_10',
        'uid': userId,
        'client': 'android',
        'model': 'Pixel 4',
        'region': '%E9%A1%BA%E4%B9%89%E5%8C%BA',
        'salf': salf,
        'brand': 'google',
        'lat': '40.14988',
        'timestamp': timestamp,
    }
    redata = urllib.parse.urlencode(data)
    res = requests.post(url, headers=headers, data=redata).json()
    if res['code'] == 1:
        signDays = res['data']['signDays']
        signAllDays = res['data']['signAllDays']
        signStatue = res['data']['signStatue']
        signData = res['data']['signData']
        print(f'签到天数为{signDays}天;累计签到天数{signAllDays}天;今日是否签到{signStatue};连续签到7天奖励{signData}')
        return f'掌上天津极速版,签到天数为{signDays}天;累计签到天数{signAllDays}天;今日是否签到{signStatue};连续签到7天奖励{signData}'


def sign(userId, salf):
    macs = execjs.compile(js_function).call("genmac")
    macs = urllib.parse.quote(macs, 'utf-8')
    timestamp = str(int(time.time()))
    sa = f'brand=google&client=android&deviceInfo=google_Pixel 4_5831595_10&interfaceVersion=v2.8&lat=40.14988&lng=116.658974&mac={macs}&model=Pixel 4&privacyStatus=1&region=%E9%A1%BA%E4%B9%89%E5%8C%BA&salf={salf}&timestamp={timestamp}&uid={userId}&userId={userId}&version=2.8.4&versionCode=154'
    # sa = 'brand=OPPO&client=android&deviceInfo=OPPO_PCAM00_2021040100_10&interfaceVersion=v2.8&lat=30.1&lng=114.2&mac=16:20:B8:EA:31:57&model=PCAM00&privacyStatus=1&region=天津市&salf=9e2e14&timestamp=1675259130&uid=454242&userId=454242&version=2.8.4&versionCode=154'
    s = bytes(sa, encoding='utf-8')
    code = base64.b64encode(s)
    key = "1s_vsegymTasdgKxiKvRz5vDlyzmc92A_H6A8zg6I"
    signs = sha1_secret_str(key, code).upper()
    url = f"https://bbs.zaitianjin.net/zstj/v2.8/index.php"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'bbs.zaitianjin.net',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/4.9.3'
    }
    data = {
        'c': 'Credit',
        'lng': '116.658974',
        'privacyStatus': '1',
        'sign': signs,
        'interfaceVersion': 'v2.8',
        'version': '2.8.4',
        'userId': userId,
        'm': 'sign',
        'mac': macs,
        'versionCode': '154',
        'deviceInfo': 'google_Pixel 4_5831595_10',
        'uid': userId,
        'client': 'android',
        'model': 'Pixel 4',
        'region': '%E9%A1%BA%E4%B9%89%E5%8C%BA',
        'salf': salf,
        'brand': 'google',
        'lat': '40.14988',
        'timestamp': timestamp,
    }
    redata = urllib.parse.urlencode(data)
    res = requests.post(url, headers=headers, data=redata).json()
    if res['code'] == 1:
        codemsg = res['data']['code']
        print(f"签到获得{codemsg}元")


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
    zstjhd = os.environ['zstjhd'].split("\n")
    webhook_token = os.environ['QYWX_KEY']
    for i in zstjhd:
        userId = i.split("&")[0]
        salf = i.split("&")[1]
        sign(userId, salf)
        message = sign_data(userId, salf)
        webhook(message, webhook_token)
