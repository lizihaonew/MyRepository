# -*- coding: utf-8 -*-
# @Author  : Li Zihao
# @Time    : 2020/7/9 19:12
# @File    : urls.py

from django.urls import path, include
from . import task_views

urlpatterns = [
    # path('js/', include('stress_agent.urls')),
    # path('setenv', task_views.set_env),
    # path('testenv', task_views.test_env),
]