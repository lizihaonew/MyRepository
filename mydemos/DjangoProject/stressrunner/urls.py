# -*- coding: utf-8 -*-
# @Author  : Li Zihao
# @Time    : 2020/7/4 15:36
# @File    : urls.py


from django.urls import path, include

from stressrunner import views

urlpatterns = [
    path('projectlist', views.project_list),
    path('projectadd', views.project_add),
    path('projectupdate', views.project_update),
    path('projectdel', views.project_del),
    path('envlist', views.env_list),
    path('addenv', views.add_env),
    path('delenv', views.del_env),
    path('setenv', views.set_env),
    path('testenv', views.test_env),
    path('downloadscripts', views.download_scripts),
    path('uploadhost', views.upload_host),
    path('taskadd', views.task_add),
    path('analyzescript', views.analyze_script),
    path('syncscripts', views.sync_scripts),
]