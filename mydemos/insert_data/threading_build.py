#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : Li ZiHao
# @Time     : 2019/12/26 14:14
# @File     : threading_build.py

import threading


def go_thread(func):
    thread_obj = []
    for i in range(10):
        t = threading.Thread(target=func, args=(i, ))
        thread_obj.append(t)
        t.start()

    for t in thread_obj:
        t.join()

