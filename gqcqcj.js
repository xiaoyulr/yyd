"""
cron: 10 19 * * *
new Env('广汽传祺抽奖');

"""
import os
from pprint import pprint
import requests


def luck_car(token):
    url = "https://gsp.gacmotor.com/gw/app/activity/api/red/packet/rain/open?activityCode=red_packet_rain&isClick=1&source=app"
    headers = {
        'Host': 'gsp.gacmotor.com',
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'Accept': 'application/json, text/plain, */*',
        'Cache-Control': 'no-cache',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; Pixel 4 Build/QD1A.190821.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 MQQBrowser/6.2 TBS/046011 Mobile Safari/537.36;GACClient',
        'token': token,
        'Origin': 'https://gsp.gacmotor.com',
        'X-Requested-With': 'com.cloudy.component',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://gsp.gacmotor.com/h5/activity/redPacket/index.html',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    }
    res = requests.post(url=url, headers=headers).json()
    pprint(res)


if __name__ == '__main__':
    tokens = os.environ["gqcqCookie"].split("\n")
    for token in tokens:
        print(token)
        luck_car(token)
