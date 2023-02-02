"""
cron: 10 0 * * *
new Env('高佣联盟提现');

"""

import json
import os
import requests


def get_money(number, userId, consumerId):
    url = "https://saas.hixiaoman.com/finance/farm/getFinanceInfo"
    headers = {
        'Host': 'saas.hixiaoman.com',
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; Pixel 4 Build/QD1A.190821.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36bxnative-1.5.3.15',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://saas.hixiaoman.com/tree_default.html?ADTAG=3095&appKey=fdsh-az-hdgj_tmddix&activityNo=NC-TREE-002&parentActNo=NC-TREE-002&subActivityNo=NC-TREE-002&strategyId=32&parentStrategyId=32&parentPeriodId=1588&parentActPlanId=1063&activityId=56&bossId=32&placeId=3095&activityType=6&putType=60000&as=2&skinId=92&themeId=530&flowId=0&flowActPlanId=0&activityPlanId=1063&flowActivityType=0&actPeriodId=1588&actTaskId=null&consumeType=1&userKey=600139975378852382&isShare=null&consumerId=7016469&vcs=0&wuBaNum=0&adSources=1_2',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cookie': f'userId=fdsh-az-hdgj_tmddix={userId}; consumerId=fdsh-az-hdgj_tmddix={consumerId};',

    }
    res = requests.get(url=url, headers=headers).json()
    if res['code'] == "0":
        money = res['data']['balance']
        print(f"第{number}个账号目前{money / 100}元")
        return money


def withdraw_money(number, userId, consumerId):
    url = "https://saas.hixiaoman.com/finance/activity/applyWithdraw?amount=100&busType=4"
    headers = {
        'Host': 'saas.hixiaoman.com',
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; Pixel 4 Build/QD1A.190821.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36bxnative-1.5.3.15',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://saas.hixiaoman.com/tree_default.html?ADTAG=3095&appKey=fdsh-az-hdgj_tmddix&activityNo=NC-TREE-002&parentActNo=NC-TREE-002&subActivityNo=NC-TREE-002&strategyId=32&parentStrategyId=32&parentPeriodId=1588&parentActPlanId=1063&activityId=56&bossId=32&placeId=3095&activityType=6&putType=60000&as=2&skinId=92&themeId=530&flowId=0&flowActPlanId=0&activityPlanId=1063&flowActivityType=0&actPeriodId=1588&actTaskId=null&consumeType=1&userKey=600139975378852382&isShare=null&consumerId=7016469&vcs=0&wuBaNum=0&adSources=1_2',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cookie': f'userId=fdsh-az-hdgj_tmddix={userId}; consumerId=fdsh-az-hdgj_tmddix={consumerId};',

    }
    res = requests.get(url=url, headers=headers).json()
    print(res)
    if res['code'] == "0":
        print(f"第{number}账号提现1元成功")
        return f"高佣联盟:第{number}账号提现1元成功"
    else:
        print(res['desc'])


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
    cookies = os.environ["fdshck"].split("@")
    webhook_token = os.environ["QYWX_KEY"]
    for i in range(len(cookies)):
        number = i + 1
        cookie = cookies[i].split("#")
        userId = cookie[0]
        consumerId = cookie[1]
        money = get_money(number, userId, consumerId)
        if money >= 100:
            msg = withdraw_money(number, userId, consumerId)
            webhook(msg, webhook_token)
