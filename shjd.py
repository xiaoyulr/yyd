"""
cron: 10 7 * * *
const $ = new Env("上海家定")
"""
import datetime
import json
import os
import time
from pprint import pprint
import requests

headers = {
    # 'log-header': 'I am the log request header.',
    # 'deviceId': 'cf3fbc4c7a96447e8e852b0fb79bd2b2',
    # 'siteId': '310114',
    'token': '',
    'Content-Type': 'application/json; charset=UTF-8',
    # 'Content-Length': '2',
    'Host': 'jdapi.shmedia.tech',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
    'User-Agent': 'okhttp/4.10.0',

}


def get(url):
    res = requests.post(url=url, headers=headers).json()
    return res


def post(url):
    res = requests.post(url=url, headers=headers).json()
    return res


def post_body(url, body):
    body = json.dumps(body).encode(encoding='utf-8')
    res = requests.post(url=url, data=body, headers=headers).json()
    return res


def get_person():
    url = "https://jdapi.shmedia.tech/media-basic-port/api/app/personal/get"
    res = post(url)
    if res['code'] == 0:
        nickname = res['data']['nickname']
        score = res['data']['score']
        print(f'欢迎会员{nickname},目前积分:{score}')
        return f'会员{nickname},目前积分:{score}'


def login():
    url = "https://jdapi.shmedia.tech/media-basic-port/api/app/points/login/add"
    res = post(url)
    # pprint(res)
    if res['code'] == 0:
        print(f'登录成功')


def sign():
    body = {}
    url = "https://jdapi.shmedia.tech/media-basic-port/api/app/personal/score/sign"
    res = post_body(url, body)
    if res['code'] == 0:
        try:
            score = res['data']['score']
            title = res['data']['title']
            print(f"{title},获得{score}分")
        except:
            pass


def get_tasklist():
    body = {}
    url = "https://jdapi.shmedia.tech/media-basic-port/api/app/personal/score/info"
    res = post_body(url, body)
    # pprint(res)
    if res['code'] == 0:
        list = get_read_list()
        for i in res['data']['jobs']:
            id = i['id']
            title = i['title']
            print(id, title)
            if title == "阅读文章":
                for i in list:
                    read_add()
                    read(i)
                    time.sleep(2)
            if title == "视听积分":
                list_radio = get_radio_list()
                for i in list_radio:
                    radio_add()
                    radio(i)
                    time.sleep(2)


def get_read_list():
    list = []
    body = {"channel": {"id": "9b84ad9dd9664184958bfe83c97d4073"}, "orderBy": "release_desc", "pageNo": 2,
            "pageSize": 10}
    url = "https://jdapi.shmedia.tech/media-basic-port/api/app/news/content/dynamic/list"
    res = post_body(url, body)
    # pprint(res)
    if res['code'] == 0:
        for displayDataList in res['data']['dataList']:
            for i in displayDataList["displayDataList"]:
                try:
                    title = i['title']
                    id = i['id']
                    topLevel = i['topLevel']
                    print(title, id, topLevel)
                    list.append([title, id, topLevel])
                except:
                    pass
    return list


def read(list):
    body = {"liveStatus": "", "topLevel": list[2], "id": f"{list[1]}"}
    print(body)
    url = "https://jdapi.shmedia.tech/media-basic-port/api/app/news/content/get"
    res = post_body(url, body)
    if res['code'] == 0:
        channelName = res['data']['title']
        shareUrl = res['data']['shareUrl']
        title = res['data']['title']
        titleImage = res['data']['displayResources'][0]['sourceUrl']
        read_poster(channelName, shareUrl, title, titleImage)
        print(f"阅读{list[0]}成功")


def read_poster(channelName, shareUrl, title, titleImage):
    body = {"channelName": channelName, "shareUrl": shareUrl, "summary": "123", "title": title,
            "titleImage": titleImage}
    url = "https://jdapi.shmedia.tech/media-basic-port/api/app/content/poster/url"
    res = post_body(url, body)
    if res['code'] == 0:
        pass


def read_add():
    url = "https://jdapi.shmedia.tech/media-basic-port/api/app/points/read/add"
    res = post(url)
    if res['code'] == 0:
        pass


def get_radio_list():
    list = []
    body = {"channel": {"children": [], "contentType": "channel", "displayStyle": "short-video", "title": "嘉视频",
                        "id": "9b6b474533e64789a31eb8ebb1bb49b9"}, "orderBy": "release_desc", "pageNo": 1,
            "pageSize": 10}
    url = "https://jdapi.shmedia.tech/media-basic-port/api/app/news/content/list"
    res = post_body(url, body)
    # pprint(res)
    if res['code'] == 0:
        for i in res['data']['records']:
            title = i['title']
            id = i['id']
            topLevel = i['topLevel']
            print(title, id, topLevel)
            list.append([title, id, topLevel])

    return list


def radio_add():
    url = "https://jdapi.shmedia.tech/media-basic-port/api/app/points/video/add"
    res = post(url)
    if res['code'] == 0:
        pass


def radio(list):
    body = {"id": list[1]}
    print(body)
    url = "https://jdapi.shmedia.tech/media-basic-port/api/app/multimedia/drama/get"
    res = post_body(url, body)
    if res['code'] == 0:
        # channelName = res['data']['channel']['title']
        # shareUrl = res['data']['shareUrl']
        # title = res['data']['title']
        # titleImage = res['data']['displayResources'][0]['sourceUrl']
        # read_poster(channelName, shareUrl, title, titleImage)
        print(f"阅读{list[0]}成功")


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
    shjdtokens = os.environ["shjdtoken"].split("\n")
    send_list = []
    for token in shjdtokens:
        header1 = {
            'token': token,
        }
        headers.update(header1)
        get_person()
        login()
        sign()
        get_tasklist()
        meg = get_person()
        send_list.append(meg)
    message = "上海嘉定积分推送:  \n" + "\n".join(send_list)
    webhook(message, webhook_token)
