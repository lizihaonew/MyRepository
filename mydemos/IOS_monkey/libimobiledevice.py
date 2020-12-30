# -*- coding: utf-8 -*-
# @Author  : Li Zihao
# @Time    : 2020/12/1 11:22
# @File    : libimobiledevice.py


import subprocess
import os

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


# 安装应用  app名称中不能有空格
def install_app():
    app = os.path.join(BASE_PATH, "xxx.ipa")
    command = "ideviceinstaller -u fd655f67024bcadd9c64d49df00dfeb9e41d34cb -i %s" % app
    res = os.popen(command).read()


# 卸载应用
def uninstall_app():
    bundleID = "cn.xxxxxx.ios"
    command = "ideviceinstaller -u fd655f67024bcadd9c64d49df00dfeb9e41d34cb -U %s" % bundleID
    res = os.popen(command).read()


