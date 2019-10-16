#!/usr/bin/python2
# -*- coding: utf-8 -*-
# @Author   : Lizihao
# @Time     : 2019/4/14 12:21
# @File     : update_pod.py

"""
获取某个环境的镜像版本并更新到指定环境下
grep -r "image: registry.newbanker.cn:5000/newbanker/" ./
"""

import re
import os
import time

# ******** 配置信息 ******** #
project_version = "宁圣私有化项目dev环境"
namespace = "private-240"
base_path = "/data/k8s/private"
log_file = "/data/k8s/private/pods_update.log"
file_path = './11111.txt'
# ************************** #


def get_image_versions():
    with open(file_path, 'r') as fb:
        content = []
        for line in fb.readlines():
            line_version = re.findall(r':#{0}\s+image.+/newbanker/(.+:\d+)', line)
            if line_version:
                content.append(line_version[0])
    return content


def get_path(server_name):
    """
    通过镜像服务名，查找对应的deploy配置文件及其路径
    """
    for paths, floders, files in os.walk(base_path, topdown=False):
        if paths.endswith(server_name):
            for file in files:
                if "deploy" in file and file.endswith("yml") or file.endswith("yaml"):
                    return [paths, file]


def replease_image(yml_path, server_name, image_num):
    """
    更新deploy.yml文件中的镜像号；
    """
    with open(yml_path, 'r') as yml_obj:
        content = yml_obj.read()
        global version_old
        version_old = re.findall(r"^#{0}[\w/\s:.]+(%s:\d+)" % server_name, content, re.M)[0]
        print(">>> 老的版本号: " + version_old)
        global containers_name
        containers_name = re.findall(r"containers:\s+- name: ([\w-]+)", content)[0]

    with open(yml_path, 'w') as yml_obj:
        version_name = ":".join([server_name, image_num])
        content = content.replace(version_old, version_name)
        yml_obj.write(content)


def apply_deploy():
    """
    apply deploy文件
    """
    os.system("kubectl apply -f %s" % yml_file)
    print("******** 更新成功！！！********")


def record_log():
    """
    将相关参数记录到日志文件中
    """
    if os.path.exists(log_file):
        file_size = os.path.getsize(log_file)
        if file_size >= 10485760:
            os.remove(log_file)
            open(log_file, 'w')
    else:
        open(log_file, 'w')

    with open(log_file, 'r') as log_obj:
        content_older = log_obj.read()

    with open(log_file, 'w') as log_obj:
        op_time = time.strftime('%Y-%m-%d %H:%M:%S')
        content = '''

        项    目：{3}\n
        更新版本：{0}\n
        旧的版本：{1}\n
        更新时间：{2}\n

        ========================
        '''
        log_obj.write(content.format(version_name, version_old, op_time, project_version) + content_older)


def do_update(image_version):
    global version_name
    global yml_file
    while True:
        version_name = image_version
        if ":" not in version_name:
            print("输入格式不对，请重新输入")
            continue
        else:
            print(">>> 新的版本号：" + version_name)
            server_name, image_num = version_name.split(':')
            if not image_num.isdigit() or not server_name:
                print("服务名为空或冒号后面不是纯数字,请重新输入！！！")
                continue
            try:
                full_path, yml_file = get_path(server_name)
                yml_path = full_path + '/' + yml_file
                os.chdir(full_path)
            except Exception as exceptions:
                print("输入的服务没有匹配中，请确认并重新输入！！")
                continue
            else:
                break

    replease_image(yml_path, server_name, image_num)
    if version_old == version_name:
        print("待更新的版本，与原版本相同，不需要更新！！")
    else:
        apply_deploy()
        record_log()
        list_command = "kubectl get pods -n=%s | grep %s" % (namespace, containers_name)
        print(">>> 该命令查看启动状态：\n" + list_command)
        os.system(list_command)


def main_func():
    image_versions = get_image_versions()

    for image in image_versions:
        do_update(image)
        time.sleep(5)


if __name__ == '__main__':
    main_func()