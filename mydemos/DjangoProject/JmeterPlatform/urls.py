# -*- coding: utf-8 -*-
# @Author  : Li Zihao
# @Time    : 2020/5/21 21:19
# @File    : urls.py

from django.contrib import admin
from django.urls import path

from JmeterPlatform import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('uploadfiles/', views.upload_files, name='uploadfiles'),
    path('filelist/', views.file_list, name='filelist'),
    path('downloadfile/', views.download_file, name='downloadfile'),
    path('deletefile/', views.delete_file, name='deletefile'),
]