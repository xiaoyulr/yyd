"""
cron: 10 8,10,12,18,22 * * *
const $ = new Env("得wu果园")
"""
import datetime
import json
import os
import time
from pprint import pprint
import requests

headers = {
    'Host': 'app.dewu.com',
    # 'Content-Length': '35',
    'isProxy': '1',
    'ua': 'duapp/5.9.0(android;10)',
    # 'shumeiId': '20230128225413a87ee709cfb952d3f10e37c551ce95e0011afe32d1b7ff11',
    'deviceTrait': 'Pixel+4',
    'x-auth-token': '',
    # 'uuid': '4ebb5a84c26fa4f8',
    'channel': 'xiaomi',
    'emu': '0',
    # 'cookieToken': '5aa06c71|1363611967|1674918939|04ee4187934f33d4',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; Pixel 4 Build/QD1A.190821.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36/duapp/5.9.0(android;10)',
    'Content-Type': 'application/json;charset=UTF-8',
    'isRoot': '0',
    'Accept': 'application/json, text/plain, */*',
    'imei': '',
    'appId': 'h5',
    'appVersion': '5.9.0',
    'Origin': 'https://cdn-fast.dewu.com',
    'X-Requested-With': 'com.shizhuang.duapp',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://cdn-fast.dewu.com/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cookie': 'duToken=5aa06c71|1363611967|1674918939|04ee4187934f33d4; smidV2=202301291402328b4f2756b1c33cd10d837e711417fb6f000d6bf2224651fd0',
    'Connection': 'keep-alive',

}


def get_info():
    url = "https://app.dewu.com/hacking-tree/v1/user/target/info"
    res = requests.get(url, headers=headers).json()
    if res['code'] == 200:
        level = res['data']['level']
        name = res['data']['name']
        lastLevel = res['data']['lastLevel']
        lastLevel = int(lastLevel) - int(level)
        print(f'目前种植{name},现在{level}级,还差{lastLevel}级领取物品')
        return f'目前种植{name},现在{level}级,还差{lastLevel}级领取物品'


def receive_water():
    url = "https://app.dewu.com/hacking-tree/v1/droplet/get_generate_droplet"
    res = requests.post(url=url, headers=headers).json()
    # pprint(res)
    if res['code'] == 200:
        droplet = res["data"]["droplet"]
        print(f'收水车水滴{droplet}滴')


def get_list():
    url = "https://app.dewu.com/hacking-tree/v1/task/list"
    res = requests.get(url, headers=headers).json()
    # pprint(res)
    if res['code'] == 200:
        for i in res['data']["taskList"]:
            taskId = i["taskId"]
            taskName = i["taskName"]
            taskType = i["taskType"]
            classify = i["classify"]
            print(f"开始{taskName}任务, {taskId}, {taskType}, {classify}".center(50, "*"))
            if taskName == "服装会场水滴翻倍大放送":
                print(taskName, taskId, taskType)
                pre_commit_task(taskName, taskId)
                task_status(taskId)
                body_commit = {"taskId": taskId, "taskType": '16'}
                commit_task(taskName, body_commit)
                time.sleep(10)
                body = {"classify": classify, "taskId": taskId, "completeFlag": 1}
                receive_task(body)
            elif taskName == "授权开通一次借钱":
                body_commit = {"taskId": taskId, "taskType": f'{taskType}'}
                commit_task(taskName, body_commit)
                time.sleep(10)
                body = {"classify": classify, "taskId": taskId}
                receive_task(body)
            elif taskName == "参与1次九元购":
                body_commit = {"taskId": taskId, "taskType": f'{taskType}'}
                commit_task(taskName, body_commit)
                time.sleep(10)
                body = {"classify": classify, "taskId": taskId}
                receive_task(body)
            elif taskName == "参与1次0元抽奖":
                body_commit = {"taskId": taskId, "taskType": f'{taskType}'}
                commit_task(taskName, body_commit)
                time.sleep(10)
                body = {"classify": classify, "taskId": taskId}
                receive_task(body)
            elif taskName == "去95分App逛潮奢尖货":
                body_commit = {"taskId": taskId, "taskType": f'{taskType}'}
                commit_task(taskName, body_commit)
                time.sleep(10)
                body = {"classify": classify, "taskId": taskId}
                receive_task(body)
            elif taskName == "逛逛国潮棉服专场":
                print(taskName, taskId, taskType)
                body_commit = {"taskId": taskId, "taskType": f'{taskType}', "activityType": '', "activityId": '',
                               "taskSetId": '', "venueCode": '', "venueUnitStyle": '', "taskScene": ''}
                pre_commit_task(taskName, taskId)
                task_status(taskId)
                commit_task(taskName, body_commit)
                time.sleep(10)
                body = {"classify": classify, "taskId": taskId}
                receive_task(body)
            elif taskName == "收集一次水滴生产":
                pass
            elif taskName == "完成五次浇灌":
                pass
            elif taskName == "从购买页进入到星愿森林":
                body_commit = {"taskId": taskId, "taskType": f'{taskType}'}
                commit_task(taskName, body_commit)
                time.sleep(10)
                body = {"classify": classify, "taskId": taskId}
                receive_task(body)
            elif taskName == "美妆会场水滴大放送":
                pre_commit_task(taskName, taskId)
                task_status(taskId)
                body_commit = {"taskId": taskId, "taskType": '16'}
                commit_task(taskName, body_commit)
                body = {"classify": classify, "taskId": taskId}
                print(body)
                receive_task(body)
            elif taskName == "逛逛国潮棉服专场":
                pre_commit_task(taskName, taskId)
                time.sleep(16)
                body_commit = {"taskId": taskId, "taskType": f'{taskType}', "activityType": '', "activityId": '',
                               "taskSetId": '', "venueCode": '', "venueUnitStyle": '', "taskScene": ''}
                commit_task(taskName, body_commit)
                time.sleep(10)
                body = {"classify": classify, "taskId": taskId}
                receive_task(body)
            elif taskName == "新春配饰会场水滴翻倍大放送":
                pre_commit_task(taskName, taskId)
                time.sleep(16)
                body_commit = {"taskId": taskId, "taskType": '16'}
                commit_task(taskName, body_commit)
                time.sleep(10)
                body = {"classify": classify, "taskId": taskId}
                receive_task(body)
            elif taskName == "新春家居会场水滴翻倍大放送":
                pre_commit_task(taskName, taskId)
                time.sleep(16)
                body_commit = {"taskId": taskId, "taskType": '16'}
                commit_task(taskName, body_commit)
                time.sleep(10)
                body = {"classify": classify, "taskId": taskId}
                receive_task(body)
            else:
                body_commit = {"taskId": taskId, "taskType": f'{taskType}'}
                commit_task(taskName, body_commit)
                body = {"classify": classify, "taskId": taskId}
                receive_task(body)


def task_status(taskId):
    for i in range(5):
        url = f"https://app.dewu.com/hacking-task/v1/task/status?taskId={taskId}&taskType=251"
        res = requests.get(url=url, headers=headers).json()
        print(res)
        time.sleep(6)


# 1天领4次水滴
def receive_task_4water():
    url = "https://app.dewu.com/hacking-tree/v1/task/receive"
    body = {"classify": 1, "taskId": "multi_times"}
    body = json.dumps(body).encode(encoding='utf-8')
    res = requests.post(url=url, data=body, headers=headers).json()
    if res['code'] == 200:
        num = res["data"]["num"]
        print(f'完成任务获得{num}水滴')
    else:
        print(res['msg'])


def receive_task(body):
    url = "https://app.dewu.com/hacking-tree/v1/task/receive"
    body = json.dumps(body).encode(encoding='utf-8')
    res = requests.post(url=url, data=body, headers=headers).json()
    if res['code'] == 200:
        num = res["data"]["num"]
        print(f'完成任务获得{num}水滴')
    else:
        print(res['msg'])


def pre_commit_task(taskName, taskId):
    url = 'https://app.dewu.com/hacking-task/v1/task/pre_commit'
    body_commit = {"taskId": taskId, "taskType": 16}
    body = json.dumps(body_commit).encode(encoding='utf-8')
    res = requests.post(url=url, data=body, headers=headers).json()
    if res['code'] == 200:
        print(f"提交{taskName},任务{res['msg']}")
    else:
        print(res['msg'])


def commit_task(taskName, body_commit):
    url = 'https://app.dewu.com/hacking-task/v1/task/commit'
    body = json.dumps(body_commit).encode(encoding='utf-8')
    res = requests.post(url=url, data=body, headers=headers).json()
    # pprint(res)
    if res['code'] == 200:
        print(f"提交{taskName},任务{res['msg']}")
    else:
        print(res['msg'])


def extra_task_reward():
    url = 'https://app.dewu.com/hacking-tree/v1/task/extra'
    list = [2, 5, 8, 12]
    for i in list:
        body = {"condition": i}
        body = json.dumps(body).encode(encoding='utf-8')
        res = requests.post(url=url, data=body, headers=headers).json()
        if res['code'] == 200:
            num = res["data"]["num"]
            print(f"完成任务获得额外水滴{num}")


# 水滴投资
def invest_commit_water():
    url = "https://app.dewu.com/hacking-tree/v1/invest/commit"
    body = {}
    body = json.dumps(body).encode(encoding='utf-8')
    res = requests.post(url=url, data=body, headers=headers).json()
    print(res)
    if res['code'] == 200:
        print(f'投资成功')


def invest_water():
    url = "https://app.dewu.com/hacking-tree/v1/invest/receive"
    res = requests.post(url=url, headers=headers).json()
    if res['code'] == 200:
        profit = res["data"]["profit"]
        print(f'获得投资收益{profit}水滴')


def watering(number=1):
    url = "https://app.dewu.com/hacking-tree/v1/tree/watering"
    body = {}
    body = json.dumps(body).encode(encoding='utf-8')
    res = requests.post(url=url, data=body, headers=headers).json()
    droplet_extra_water_del()
    if number < 5:
        time.sleep(59)
        data = droplet_extra_info()
        if data == 99:
            droplet_extra_water()
    elif number == 5:
        reveive_five_water()
        invest_commit_water()

    if res['code'] == 200:
        print(f'浇水成功')
        nextWateringTimes = res['data']['nextWateringTimes']
        showLevel = res['data']['levelReward']['showLevel']
        print(f"目前树为{showLevel}级")
        if nextWateringTimes == 0:
            get_watering_reward()
            watering(number=number + 1)
        else:
            time.sleep(2)
            watering(number=number + 1)
    else:
        return


def get_watering_reward():
    url = "https://app.dewu.com/hacking-tree/v1/tree/get_watering_reward"
    body = {"promote": ""}
    body = json.dumps(body).encode(encoding='utf-8')
    res = requests.post(url=url, data=body, headers=headers).json()
    if res['code'] == 200:
        print(f'浇水成功')
        rewardNum = res['data']['currentWateringReward']['rewardNum']
        print(f"获得浇水礼包{rewardNum}水滴")


def droplet_extra_water():
    url = "https://app.dewu.com/hacking-tree/v1/droplet-extra/receive"
    res = requests.post(url=url, headers=headers).json()
    if res['code'] == 200:
        totalDroplet = res["data"]["totalDroplet"]
        print(f'收瓶子水滴{totalDroplet}滴')


def droplet_extra_info():
    url = "https://app.dewu.com/hacking-tree/v1/droplet-extra/info"
    res = requests.get(url=url, headers=headers).json()
    # pprint(res)
    if res['code'] == 200:
        if res['data']['isComplete']:
            return 99


# 水瓶增加数
def droplet_extra_water_del():
    url = "https://app.dewu.com/hacking-tree/v1/tree/del"
    body = {}
    body = json.dumps(body).encode(encoding='utf-8')
    res = requests.post(url=url, data=body, headers=headers).json()
    # pprint(res)
    if res['code'] == 200:
        pass


# 收一次水滴生产
def reveive_one_water():
    body = {"classify": 1, "taskId": "4"}
    receive_task(body)


# 浇五次水收益
def reveive_five_water():
    body = {"classify": 1, "taskId": "1"}
    receive_task(body)


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
    dwtokens = os.environ["dwtoken"].split("\n")
    start_time = datetime.datetime.now().strftime('%H')
    for token in dwtokens:
        token = token.split("&")
        sk = token[0]
        shumeiId = token[1]
        x_auth_token = token[2]
        uid = token[3]
        cookieToken = token[4]
        header1 = {
            'SK': sk,
            'shumeiId': shumeiId,
            'x-auth-token': f'Bearer {x_auth_token}',
            'uid': uid,
            'cookieToken': cookieToken,
            'duToken': cookieToken,
            'Cookie': cookieToken
        }
        headers.update(header1)
        # # get_info()
        if start_time == "08":
            # # 1天领4次水滴
            receive_task_4water()
            # 领水滴投资
            invest_water()
            # # # 领水车水滴
            receive_water()
            reveive_one_water()
        if start_time == "10":
            droplet_extra_water()
        if start_time == "12":
            # # 1天领4次水滴
            receive_task_4water()
            # # # 领水车水滴
            receive_water()
        if start_time == "18":
            # # 1天领4次水滴
            receive_task_4water()
        if start_time == "22":
            # 1天领4次水滴
            receive_task_4water()
            get_list()
            # # 水滴投资
            watering()
            extra_task_reward()
            msg = get_info()
            webhook(msg, webhook_token)
