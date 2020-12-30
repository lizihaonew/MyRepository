# -*- coding: utf-8 -*-
# @Author  : Li Zihao
# @Time    : 2020/12/1 11:24
# @File    : get_ios_log.py


import threading
import datetime
import os
import time
from .libimobiledevice import get_devices, get_device_name, get_device_type, get_device_version, get_log, get_screenshot

KEYWORDS = ["ANR ", "NullPointerException", "CRASH", "Force Closed"]


def show_devices():
    devices = get_devices()
    print("已连接设备信息：")
    for device in devices:
        device_name = get_device_name(device)
        device_type = get_device_type(device)
        device_version = get_device_version(device)
        print("设备名称：%s, 类型：%s, 系统版本：%s, UID:%s" % (device_name, device_type, device_version, device))


# 监控关键字
def filter_keywords():
    devices = get_devices()
    print("开始监控关键字")
    for device in devices:
        t = threading.Thread(target=filter_keyword, args=(device,))
        t.start()
        print("设备%s关键字监控已开启" % str(device))


def filter_keyword(device):
    sub = get_log(device)
    with sub:
        for line in sub.stdout:
            print(line.decode("utf-8"))
            for key in KEYWORDS:
                if line.decode("utf-8").find(key) != -1:
                    path = get_log_path("screenshot")
                    text = line.decode("utf-8")
                    get_screenshot(device, path)
                    message = "设备：%s 检测到：%s\n%s屏幕截图路径：%s\n" % (str(device), str(key), text, path)
                    print(message)
    # send_message(message)  这里我没放上来，根据自己需要实现一个发送通知的方法就好了


def get_log_path(tag):
    year = datetime.datetime.now().strftime('%Y')
    month = datetime.datetime.now().strftime('%m')
    day = datetime.datetime.now().strftime('%d')
    path = os.path.join(tag, year, month, day)
    if not os.path.exists(path):
        os.makedirs(path)
    return path


if __name__ == '__main__':
    show_devices()
    time.sleep(3)
    filter_keywords()

