# -*- coding: utf-8 -*-
# @Author  : Li Zihao
# @Time    : 2020/5/20 17:21
# @File    : urls.py

from django.urls import path, re_path
from App import views

urlpatterns = [
    path('indexhello/', views.index_hello),
    # re_path(r'^students', views.students),
    re_path(r'^student/$', views.get_student),
    re_path(r'^student/(\d+)/', views.student),
    re_path(r'^grades/$', views.grades),
    re_path(r'^getdate/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/', views.get_date),
    path('haverequest/', views.hava_request),
    path('docreatestudent', views.create_student, name='docreatestudent'),
    path('hello/', views.hello, name='hello'),
    path('getticket/', views.get_ticket),
    path('hehe/', views.hehe),
    path('setcookie/', views.set_cookie),
    path('getcookie/', views.get_cookie),
    path('login/', views.login, name='login'),
    path('dologin/', views.do_login, name='dologin'),
    path('mine/', views.mine, name='mine'),
    path('jmeterfile/', views.jmeter_file, name='jmeterfile'),
    path('uploadfile/', views.upload_file, name='uploadfile'),
    path('uploadfiles/', views.upload_files, name='uploadfiles'),
    path('filelist/', views.file_list, name='filelist'),
    re_path(r'downloadfile/', views.download_file, name='downloadfile'),
    re_path(r'getmodelfield/', views.getmodelfield, name='getmodelfield'),
    re_path(r'deletedata/', views.delete_data, name='deletedata'),
    path('index/', views.index)

]