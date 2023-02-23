"""
cron: 10 8 * * *
const $ = new Env("阅隆湾")
"""
import random
from hashlib import sha256
import hmac, urllib.parse
import json
import os
from urllib.parse import quote_plus
from pprint import pprint
import requests
import base64, time
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5


# headers = {
#
# }


def get(url, headers):
    res = requests.get(url=url, headers=headers).json()
    return res


def post(url, headers):
    res = requests.post(url=url, headers=headers).json()
    return res


# def post_body(url, body):
#     body = json.dumps(body).encode(encoding='utf-8')
#     res = requests.post(url=url, data=body, headers=headers).json()
#     return res


def get_HmacSHA256(data):
    key = "fPfdqGwWwuAtDm4nR95Y"
    key = key.encode('utf-8')
    message = data.encode('utf-8')
    sign = hmac.new(key, message, digestmod=sha256).hexdigest()
    print(sign)
    return sign


def rsa_encrypt(text):
    pubkey = '''-----BEGIN PUBLIC KEY-----
    MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQD6XO7e9YeAOs+cFqwa7ETJ+WXi
    zPqQeXv68i5vqw9pFREsrqiBTRcg7wB0RIp3rJkDpaeVJLsZqYm5TW7FWx/iOiXF
    c+zCPvaKZric2dXCw27EvlH5rq+zwIPDAJHGAfnn1nmQH7wR3PCatEIb8pz5GFlT
    HMlluw4ZYmnOwg+thwIDAQAB    
    -----END PUBLIC KEY-----'''
    # text = "3FB276EB0DE6CE91ABD80273F1295578A82EAC22410AB6C6F340765A8367257E"
    # pubkey = '-----BEGIN PUBLIC KEY-----\n' + p_key + '\n-----END PUBLIC KEY-----' 这种写法也可以， 注意的是要加'\n'来换行
    rsakey = RSA.importKey(pubkey.encode())
    ciper = Cipher_pkcs1_v1_5.new(rsakey)
    en_data = base64.b64encode(ciper.encrypt(text.encode())).decode()
    return en_data


def sha256_secret_str(plainText):
    plainTextBytes = plainText.encode('utf-8')  # 字符串在哈希之前，需要编码
    encryptor = sha256()
    encryptor.update(plainTextBytes)
    hashCode = encryptor.hexdigest()
    return hashCode


def get_code(number, password):
    password = rsa_encrypt(password)
    data = f"post%%/web/oauth/credential_auth?client_id=10008&password={password}&phone_number={number}%%e2c7ecf7-d05f-4b3a-8973-8a7b02dd9c9d%%"
    url = f"https://passport.tmuyun.com/web/oauth/credential_auth"
    X_SIGNATURE = get_HmacSHA256(data)
    headers = {
        'Cache-Control': 'no-cache',
        'User-Agent': 'ANDROID;10;10008;1.7.0;1.0;null;Pixel 4',
        'X-REQUEST-ID': 'e2c7ecf7-d05f-4b3a-8973-8a7b02dd9c9d',
        'X-SIGNATURE': X_SIGNATURE,
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'COOKIE': 'SESSION=ZjZkZGI0ZGItNzY3ZC00OWNjLWI2NGUtMjAxOTM2OWJhNDBm; Path=/; HttpOnly; SameSite=Lax',
        'Host': 'passport.tmuyun.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        # 'Content-Length': '236',
    }

    data = {
        "client_id": "10008",
        "password": password,
        "phone_number": number,
    }
    redata = urllib.parse.urlencode(data)
    res = requests.post(url, headers=headers, data=redata).json()
    if res["code"] == 0:
        code = res["data"]["authorization_code"]["code"]
        print(code)
        return code


def get_login(code):
    time1 = str(int(time.time() * 1000))
    data = f"/api/zbtxz/login&&63f0aabe81336f75c4036315&&0a85af96-8dc0-44b6-96ab-9f1c6727e289&&{time1}&&FR*r!isE5W&&51"
    url = f"https://vapp.tmuyun.com/api/zbtxz/login"
    print(url)
    X_SIGNATURE = sha256_secret_str(data)
    headers = {
        'X-SESSION-ID': '63f0aabe81336f75c4036315',
        'X-REQUEST-ID': '0a85af96-8dc0-44b6-96ab-9f1c6727e289',
        'X-TIMESTAMP': time1,
        'X-SIGNATURE': X_SIGNATURE,
        'X-TENANT-ID': '51',
        'User-Agent': '1.7.0;00000000-6641-8422-0000-00006963f438;Google Pixel 4;Android;10;tencent',
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'vapp.tmuyun.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',

    }

    data = {
        "code": code,
        "token": '',
        "type": '-1',
        "union_id": '',
    }
    redata = urllib.parse.urlencode(data)
    res = requests.post(url, headers=headers, data=redata).json()
    if res["code"] == 0:
        nick_name = res["data"]["account"]["nick_name"]
        mobile = res["data"]["account"]["mobile"]
        id = res["data"]["session"]["id"]
        # print(id)
        print(f"欢迎电话号码为{mobile},读友为{nick_name}")
        return id


def get_sign(id):
    time1 = str(int(time.time() * 1000))
    data = f"/api/user_mumber/sign&&{id}&&0a85af96-8dc0-44b6-96ab-9f1c6727e289&&{time1}&&FR*r!isE5W&&51"
    url = "https://vapp.tmuyun.com/api/user_mumber/sign"
    X_SIGNATURE = sha256_secret_str(data)
    headers = {
        'X-SESSION-ID': id,
        'X-REQUEST-ID': '0a85af96-8dc0-44b6-96ab-9f1c6727e289',
        'X-TIMESTAMP': time1,
        'X-SIGNATURE': X_SIGNATURE,
        'X-TENANT-ID': '51',
        'User-Agent': '1.7.0;00000000-6641-8422-0000-00006963f438;Google Pixel 4;Android;10;tencent',
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'vapp.tmuyun.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',

    }

    res = requests.get(url, headers=headers).json()
    if res["code"] == 0:
        serialdays = res['data']["serialdays"]
        signIntegral = res['data']["signIntegral"]
        print(f"签到第{serialdays}天,获得{signIntegral}积分")
    else:
        print(res)


def get_do_task(id, name, memberType):
    time1 = str(int(time.time() * 1000))
    data = f"/api/user_mumber/doTask&&{id}&&0a85af96-8dc0-44b6-96ab-9f1c6727e289&&{time1}&&FR*r!isE5W&&51"
    url = "https://vapp.tmuyun.com/api/user_mumber/doTask"
    X_SIGNATURE = sha256_secret_str(data)
    headers = {
        'X-SESSION-ID': id,
        'X-REQUEST-ID': '0a85af96-8dc0-44b6-96ab-9f1c6727e289',
        'X-TIMESTAMP': time1,
        'X-SIGNATURE': X_SIGNATURE,
        'X-TENANT-ID': '51',
        'User-Agent': '1.7.0;00000000-6641-8422-0000-00006963f438;Google Pixel 4;Android;10;tencent',
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'vapp.tmuyun.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',

    }
    data = {
        "memberType": memberType,
        "member_type": memberType,
    }
    redata = urllib.parse.urlencode(data)
    res = requests.post(url, headers=headers, data=redata).json()
    # pprint(res)
    if res["code"] == 0:
        experience = res['data']["experience"]
        # signIntegral = res['data']["signIntegral"]
        print(f"完成{name}任务成功,获得{experience}积分")
    else:
        print(res)


def get_task_list(id):
    time1 = str(int(time.time() * 1000))
    data = f"/api/user_mumber/numberCenter&&{id}&&0a85af96-8dc0-44b6-96ab-9f1c6727e289&&{time1}&&FR*r!isE5W&&51"
    url = "https://vapp.tmuyun.com/api/user_mumber/numberCenter?is_new=1"
    X_SIGNATURE = sha256_secret_str(data)
    headers = {
        'X-SESSION-ID': id,
        'X-REQUEST-ID': '0a85af96-8dc0-44b6-96ab-9f1c6727e289',
        'X-TIMESTAMP': time1,
        'X-SIGNATURE': X_SIGNATURE,
        'X-TENANT-ID': '51',
        'User-Agent': '1.7.0;00000000-6641-8422-0000-00006963f438;Google Pixel 4;Android;10;tencent',
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'vapp.tmuyun.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',

    }

    res = requests.get(url, headers=headers).json()
    if res["code"] == 0:
        cur_experience = res["data"]["rst"]["cur_experience"]
        print(f"目前积分为{cur_experience}")
        for i in res['data']['rst']['user_task_list']:
            name = i['name']
            member_task_type = i['member_task_type']
            print(name, member_task_type)

            if name == '分享资讯给好友':
                for i in range(3):
                    get_do_task(id, name, member_task_type)
                    time.sleep(5)
            elif name == '使用本地服务':
                get_do_task(id, name, member_task_type)
                time.sleep(5)
            elif name == '邀请好友':
                pass
            elif name == '新闻资讯阅读':
                get_read_list(id)
            else:
                pass


def get_read_list(id):
    time1 = str(int(time.time() * 1000))
    data = f"/api/article/channel_list&&{id}&&0a85af96-8dc0-44b6-96ab-9f1c6727e289&&{time1}&&FR*r!isE5W&&51"
    page_number = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    page = random.choice(page_number)
    print(page)
    url = f"https://vapp.tmuyun.com/api/article/channel_list?channel_id=62c53767373c550ecabd9d6a&isDiFangHao=false&is_new=true&list_count={page}&size=10"
    X_SIGNATURE = sha256_secret_str(data)
    headers = {
        'X-SESSION-ID': id,
        'X-REQUEST-ID': '0a85af96-8dc0-44b6-96ab-9f1c6727e289',
        'X-TIMESTAMP': time1,
        'X-SIGNATURE': X_SIGNATURE,
        'X-TENANT-ID': '51',
        'User-Agent': '1.7.0;00000000-6641-8422-0000-00006963f438;Google Pixel 4;Android;10;tencent',
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'vapp.tmuyun.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',

    }
    res = get(url, headers)
    number = 1
    if res["code"] == 0:
        for i in res['data']['article_list']:
            doc_title = i['doc_title']
            title_id = i['id']
            print(doc_title, title_id)
            get_read(id, title_id, doc_title)
            time.sleep(2)
            get_like(id, title_id, doc_title)
            time.sleep(2)
            get_comment(id, title_id, doc_title)
            time.sleep(5)
            number += 1
            if number == 4:
                return

    else:
        print(res)


def get_read(id, page_id, name):
    time1 = str(int(time.time() * 1000))
    data = f"/api/article/detail&&{id}&&0a85af96-8dc0-44b6-96ab-9f1c6727e289&&{time1}&&FR*r!isE5W&&51"
    url = f"https://vapp.tmuyun.com/api/article/detail?id={page_id}"
    X_SIGNATURE = sha256_secret_str(data)
    headers = {
        'X-SESSION-ID': id,
        'X-REQUEST-ID': '0a85af96-8dc0-44b6-96ab-9f1c6727e289',
        'X-TIMESTAMP': time1,
        'X-SIGNATURE': X_SIGNATURE,
        'X-TENANT-ID': '51',
        'User-Agent': '1.7.0;00000000-6641-8422-0000-00006963f438;Google Pixel 4;Android;10;tencent',
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'vapp.tmuyun.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',

    }
    res = get(url, headers)
    if res["code"] == 0:
        print(f"阅读{name}文章成功")
        time.sleep(5)
    else:
        print(res)


def get_like(id, page_id, name):
    time1 = str(int(time.time() * 1000))
    data = f"/api/favorite/like&&{id}&&0a85af96-8dc0-44b6-96ab-9f1c6727e289&&{time1}&&FR*r!isE5W&&51"
    url = "https://vapp.tmuyun.com/api/favorite/like"
    X_SIGNATURE = sha256_secret_str(data)
    headers = {
        'X-SESSION-ID': id,
        'X-REQUEST-ID': '0a85af96-8dc0-44b6-96ab-9f1c6727e289',
        'X-TIMESTAMP': time1,
        'X-SIGNATURE': X_SIGNATURE,
        'X-TENANT-ID': '51',
        'User-Agent': '1.7.0;00000000-6641-8422-0000-00006963f438;Google Pixel 4;Android;10;tencent',
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'vapp.tmuyun.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',

    }
    data = {
        "action": True,
        "id": page_id,
    }
    redata = urllib.parse.urlencode(data)
    res = requests.post(url, headers=headers, data=redata).json()
    # pprint(res)
    if res["code"] == 0:
        print(f"完成{name}点赞任务成功")
        time.sleep(5)
    else:
        print(res)


def get_comment(id, page_id, name):
    time1 = str(int(time.time() * 1000))
    data = f"/api/comment/create&&{id}&&0a85af96-8dc0-44b6-96ab-9f1c6727e289&&{time1}&&FR*r!isE5W&&51"
    url = "https://vapp.tmuyun.com/api/comment/create"
    X_SIGNATURE = sha256_secret_str(data)
    comment = ['不错', '好', '点赞', '值得期待', '推荐', '对', '很好', '真棒', '优秀', '赞']
    comment_1 = random.choice(comment)
    headers = {
        'X-SESSION-ID': id,
        'X-REQUEST-ID': '0a85af96-8dc0-44b6-96ab-9f1c6727e289',
        'X-TIMESTAMP': time1,
        'X-SIGNATURE': X_SIGNATURE,
        'X-TENANT-ID': '51',
        'User-Agent': '1.7.0;00000000-6641-8422-0000-00006963f438;Google Pixel 4;Android;10;tencent',
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'vapp.tmuyun.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',

    }
    data = {
        "channel_article_id": page_id,
        "content": quote_plus(comment_1),
    }
    redata = urllib.parse.urlencode(data)
    res = requests.post(url, headers=headers, data=redata).json()
    # pprint(res)
    if res["code"] == 0:
        print(f"完成{name}评论任务成功")
        time.sleep(5)
    else:
        print(res)


def get_score(id):
    time1 = str(int(time.time() * 1000))
    data = f"/api/user_mumber/numberCenter&&{id}&&0a85af96-8dc0-44b6-96ab-9f1c6727e289&&{time1}&&FR*r!isE5W&&51"
    url = "https://vapp.tmuyun.com/api/user_mumber/numberCenter?is_new=1"
    X_SIGNATURE = sha256_secret_str(data)
    headers = {
        'X-SESSION-ID': id,
        'X-REQUEST-ID': '0a85af96-8dc0-44b6-96ab-9f1c6727e289',
        'X-TIMESTAMP': time1,
        'X-SIGNATURE': X_SIGNATURE,
        'X-TENANT-ID': '51',
        'User-Agent': '1.7.0;00000000-6641-8422-0000-00006963f438;Google Pixel 4;Android;10;tencent',
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'vapp.tmuyun.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',

    }

    res = requests.get(url, headers=headers).json()
    if res["code"] == 0:
        cur_experience = res["data"]["rst"]["cur_experience"]
        print(f"目前积分为{cur_experience}")
        return cur_experience


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
    tokens = os.environ["ylwtoken"].split("\n")
    message = ""
    for i in tokens:
        count = i.split("#")
        number = count[0]
        password = count[1]
        code = get_code(number, password)
        id = get_login(code)
        get_sign(id)
        get_task_list(id)
        score = get_score(id)
        message += f"账号{number},目前有{score}积分"
    webhook(message, webhook_token)
