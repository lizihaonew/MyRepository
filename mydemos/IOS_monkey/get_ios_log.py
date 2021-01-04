# -*- coding: utf-8 -*-
# @Author  : Li Zihao
# @Time    : 2020/12/1 11:24
# @File    : get_ios_log.py


import threading
from datetime import datetime
import os
import re
from libimobiledevice import *

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
            # print(line.decode("utf-8"))
            for key in KEYWORDS:
                if line.decode("utf-8").find(key) != -1:
                    path = get_log_path("screenshot")
                    text = line.decode("utf-8")
                    get_screenshot(device, path)
                    message = "设备：%s 检测到：%s\n%s屏幕截图路径：%s\n" % (str(device), str(key), text, path)
                    print(message)
    # send_message(message)  这里我没放上来，根据自己需要实现一个发送通知的方法就好了


def get_log_path(tag):
    year = datetime.now().strftime('%Y')
    month = datetime.now().strftime('%m')
    day = datetime.now().strftime('%d')
    path = os.path.join(tag, year, month, day)
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def get_log_file(device, time_str):
    now_time_str = datetime.strftime(time_str, '%Y%m%d%H%M%S')
    log_name = '.'.join((now_time_str, 'log'))
    log_path = os.path.join(BASE_PATH, 'logs')
    if not os.path.exists(log_path):
        os.mkdir(log_path)
    path = os.path.join(log_path, log_name)
    device_name = get_device_name(device)
    device_type = get_device_type(device)
    device_version = get_device_version(device)
    message = "设备名称：%s, 类型：%s, 系统版本：%s, UID:%s" % (device_name, device_type, device_version, device)
    with open(path, 'w') as f:
        f.write(message)
    command = "idevicesyslog -u %s >> %s &" % (device, path)
    res = os.system(command)
    print('IOS app log path: ' + path)
    return path


def analyse_log_file(udid, log_path):
    try:
        command = "ps -ef | grep 'idevicesyslog -u %s' | awk '{print $2}' | xargs kill -9" % udid
        os.popen(command)
    except Exception as e:
        pass

    with open(log_path, 'r') as fb:
        log_content = fb.read()

    res_dict = dict()
    for key in KEYWORDS:
        res_dict[key] = len(re.findall(r'%s' % key, log_content))
    return res_dict


if __name__ == '__main__':
    # show_devices()
    # time.sleep(3)
    # filter_keywords()
    udId = '871877d00ea5cf3f189a5eeeb1365babdbc9a3ad'
    logpath = '/Users/xujuan/Downloads/log.log'
    print(analyse_log_file(udId, logpath))



