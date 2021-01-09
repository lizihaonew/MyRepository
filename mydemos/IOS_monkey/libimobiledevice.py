# -*- coding: utf-8 -*-
# @Author  : Li Zihao
# @Time    : 2020/12/1 11:22
# @File    : libimobiledevice.py


import subprocess
import os
from datetime import datetime

BASE_PATH = os.path.dirname(os.path.abspath(__file__))


# 获取所有已连接设备UUID
def get_devices():                          
    command = "idevice_id -l"
    res = os.popen(command).read()
    devices = list(filter(None, res.split("\n")))
    return devices


# 获取设备名称
def get_device_name(device):
    command = "ideviceinfo -u %s -k DeviceName" % device
    res = os.popen(command).read()
    return res.replace("\n", "")


# 获取设备类型
def get_device_type(device):
    command = "ideviceinfo -u %s -k ProductType" % device
    res = os.popen(command).read()
    return res.replace("\n", "")


# 获取设备系统版本
def get_device_version(device):
    command = "ideviceinfo -u %s -k ProductVersion" % device
    res = os.popen(command).read()
    return res.replace("\n", "")


# 截图 截图会放在当前目录下，所以先切换到需要放置截图的目录下
def get_screenshot(device, path):
    command = "idevicescreenshot -u %s" % device
    os.chdir(path)
    os.system(command)


# 实时输出IOS系统日志过滤指定APP
def get_log(device):
    # command = "idevicesyslog -u {device} | grep {app}".format(device=device, app=APP_NAME)
    # 输出所有日志不过滤
    command = "idevicesyslog -u %s" % device
    sub = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return sub


def get_installed_app(device):
    command = 'ideviceinstaller -u %s -l' % device
    res = os.popen(command).read()
    # return res.replace("\n", "")
    return res.split('\n')

# 安装应用  app名称中不能有空格
def install_app(udid):
    app = os.path.join(BASE_PATH, "xxx.ipa")
    command = "ideviceinstaller -u %s -i %s" % (udid, app)
    res = os.popen(command).read()


# 卸载应用bundleID = cn.xxxxxx.ios
def uninstall_app(udid, bundleID):
    # bundleID = ""
    command = "ideviceinstaller -u %s -U %s" % (udid, bundleID)
    res = os.popen(command).read()


if __name__ == '__main__':
    # result = get_devices()
    # print(result)
    udid = '871877d00ea5cf3f189a5eeeb1365babdbc9a3ad'
    # time_str = datetime.now()
    # get_log_file(udid, time_str)
    print(get_installed_app(udid))
