# -*- coding: utf-8 -*-
# @Author  : Li Zihao
# @Time    : 2020/5/27 19:57
# @File    : task_view.py
import json

from django.http import HttpResponse

response_data = {
    'message': '',
    'data': {}
}


def response(data):
    data = json.dumps(data, ensure_ascii=False)
    return HttpResponse(data, content_type="application/json,charset=utf-8")


def add_task(request):
    task_name = request.GET.get('task_name')
    response_data['message'] = '操作成功'
    response_data['data'] = task_name
    return response(response_data)