#!/usr/bin/python2
# -*- coding: utf-8 -*-
# @Author   : Lizihao
# @Time     : 2019/4/14 12:21
# @File     : update_pod.py

"""
该脚本主要用于在服务器更新微服务镜像版本号，并可自动apply deploy.yml文件。
用法：
1. 在使用前，以项目级修改配置信息
2. 配置信息中，base_path为各服务公共目录的最深一层，log_file为日志文件
3. 使用前必须保证各个服务deploy文件的上一层目录名与镜像服务名一致
    如:  /data/…/wbs-web/deploy.yml  ==>  wbs-web:1234567890
4. 将该脚本复制到服务器中使用

"""

import re
import os, time


# ******** 配置信息 ******** #
project_version = "宁圣私有化项目 1.0"
namespace = "ningsheng"
base_path = "/data/k8s/ningsheng"
log_file = "/data/k8s/ningsheng/pods_update.log"

# ************************** #


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
        print ">>> 老的版本号: " + version_old
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
    print "******** 更新成功！！！********"


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


def do_update():
    print ">>> 请输入镜像版本号，例：nsprivate-web:2019040901"
    global version_name
    global yml_file
    while True:
        version_name = raw_input(">>> 请输入：")
        if ":" not in version_name:
            print "输入格式不对，请重新输入"
            continue
        else:
            print ">>> 新的版本号：" + version_name
            server_name, image_num = version_name.split(':')
            if not image_num.isdigit() or not server_name:
                print "服务名为空或冒号后面不是纯数字,请重新输入！！！"
                continue
            try:
                full_path, yml_file = get_path(server_name)
                yml_path = full_path + '/' + yml_file
                os.chdir(full_path)
            except Exception as exceptions:
                print "输入的服务没有匹配中，请确认并重新输入！！"
                continue
            else:
                break

    replease_image(yml_path, server_name, image_num)
    if version_old == version_name:
        print "待更新的版本，与原版本相同，不需要更新！！"
    else:
        apply_deploy()
        record_log()
        list_command = "kubectl get pods -n=%s | grep %s" % (namespace, containers_name)
        print ">>> 该命令查看启动状态：\n" + list_command
        os.system(list_command)


if __name__ == "__main__":
    do_update()

"""
# 单元测试case集
wbs-cms:12424314124
open-api:123424241
wbs-web:213421421
marketing-admin:12421424212
marketing-api:34142142
marketing-center:12421412412
wbs_web:213421421
123214wbs-web:213421421
open-api:wqe
:12321212
open-api:
输入为空
"""