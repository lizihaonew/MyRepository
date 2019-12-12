#!/usr/bin/python2
# -*- coding: utf-8 -*-
# @Author   : Li ZiHao
# @Time     : 2019/9/19 11:22
# @File     : base_demo.py

import requests
import json


class RunMain:
    # def __init__(self):
    #     pass

    def get_method(self,url,data):
        result = requests.get(url=url, data=data).json()
        return json.dumps(result, indent=2, sort_keys=True)

    def post_method(self,url,data):
        result = requests.post(url=url, data=data).json()
        return json.dumps(result, indent=2, sort_keys=True)

    def run_main(self,url,method,data):
        if method == 'GET' or method == 'get':
            res = self.get_method(url, data)
        elif method == 'POST' or method == 'post':
            res = self.post_method(url, data)
        return json.loads(res)


if __name__ == '__main__':
    url = 'http://www.imooc.com/m/web/shizhanapi/loadmorepingjia.html'
    data = {
        'cart': 'www'
    }
    run = RunMain()
    resp = run.run_main(url, 'GET', data)
    # print(resp)
    # {'code': 200,
    #  'data': {'data': [], 'errorCode': 1006, 'errorDesc': 'token error', 'status': 1, 'timestamp': 1568867068064}}