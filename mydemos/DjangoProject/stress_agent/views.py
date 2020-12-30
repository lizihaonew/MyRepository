# -*- coding: utf-8 -*-
# @Author  : Li Zihao
# @Time    : 2020/7/9 19:15
# @File    : task_views.py


import os
import threading
import time
import json
import paramiko
import logging
import requests
from datetime import datetime, timedelta
import concurrent.futures as futures
from django.http import HttpResponse, JsonResponse
from apscheduler.schedulers.background import BackgroundScheduler
from django.views.decorators.http import require_POST, require_GET

from stress_agent.utils import RecodeThread, ServerOpt



@require_POST
def set_env(request):
    """ 部署环境 """
    json_template = {
        "errCode": 0,
        "errMessage": ""
    }
    body = json.loads(request.body)
    keys = ['master_node', 'slave_node', 'user_name', 'user_password']
    master_node, slave_node, user_name, user_password = [body[k] for k in keys]

    if slave_node:
        hosts = slave_node.split(',') + [master_node]
    else:
        hosts = [master_node]
    lock = threading.Lock()

    def set_jmeter(host):
        lock.acquire()
        try:
            server_opt = ServerOpt(host, user_name, user_password)
        except Exception:
            raise Exception('服务器%s登陆失败' % host)
        else:
            if 'jmeter.sh' in server_opt.exec_command('ifconfig;ls /var/autoplatform-jmeter/bin')['stdout']:
                print('服务器%s已经安装jmeter' % host)
                server_opt.ssh_close()
            else:
                jave_env_command = 'java -version'
                jave_env_reslut = server_opt.exec_command(jave_env_command)
                if not jave_env_reslut['stdout'] and 'version' not in jave_env_reslut['stderr']:
                    raise Exception('服务器%s未安装JDK环境' % host)
                else:
                    from_path = os.path.dirname(os.path.abspath(__file__)) + '\\autoplatform-jmeter.tar.gz'
                    to_path = '/var/autoplatform-jmeter.tar.gz'
                    try:
                        server_opt.put_files(from_path, to_path)
                    except Exception as e:
                        print(e)
                        raise Exception('服务器%s部署失败' % host)
                    if host == master_node:
                        command = 'cd /var;tar -zxvf %s;rm -f %s' % (to_path, to_path)
                    else:
                        sh_path = '/var/autoplatform-jmeter/start_slave_jmeter.sh'
                        command = 'cd /var;tar -zxvf %s;rm -f %s;chmod +x %s; bash %s' % (to_path, to_path, sh_path, sh_path)
                    try:
                        server_opt.exec_command(command)
                        server_opt.ssh_close()
                    except Exception:
                        pass
        lock.release()

    def go_thread(func):
        thread_obj = []
        for host in hosts:
            t = RecodeThread(func, host)
            thread_obj.append(t)
            t.start()

        for t in thread_obj:
            t.join()
            if t.exitcode != 0:
                raise Exception(t.exception)

    try:
        go_thread(set_jmeter)
    except Exception as e:
        json_template["errCode"] = 1
        json_template['errMessage'] = str(e)
        json_template['set_status'] = '2'
        return JsonResponse(json_template, safe=False)

    json_template["errCode"] = 0
    json_template['errMessage'] = "部署成功"
    json_template['set_status'] = "1"
    return JsonResponse(json_template, safe=False)


@require_POST
def test_env(request):
    """ 检测环境部署 """
    json_template = {
        "errCode": 0,
        "errMessage": ""
    }
    body = json.loads(request.body)
    keys = ['master_node', 'slave_node', 'user_name', 'user_password']
    master_node, slave_node, user_name, user_password = [body[k] for k in keys]

    try:
        master_server_opt = ServerOpt(master_node, user_name, user_password)

    except Exception:
        json_template["errCode"] = 1
        json_template['errMessage'] = "服务器%s登陆失败" % master_node
        json_template['test_status'] = '2'
        return JsonResponse(json_template)
    else:
        master_node_test_result = master_server_opt.exec_command('/var/autoplatform-jmeter/bin/jmeter -v')
        if 'Copyright' not in master_node_test_result['stdout']:
            master_server_opt.ssh_close()
            json_template["errCode"] = 1
            json_template['errMessage'] = "服务器%s测试失败" % master_node
            json_template['test_status'] = '2'
            return JsonResponse(json_template)

    def slave_test(host):
        try:
            slave_server_opt = ServerOpt(host, user_name, user_password)
        except Exception:
            raise Exception('服务器%s登陆失败' % host)
        else:
            command = 'ps -ef | grep jmeter'
            slave_test_result = slave_server_opt.exec_command(command)
            if 'jmeter-server' not in slave_test_result['stdout']:
                raise Exception('服务器%s测试失败' % host)

    def go_thread(func):
        thread_obj = []
        for host in slave_nodes:
            t = RecodeThread(func, host)
            thread_obj.append(t)
            t.start()

        for t in thread_obj:
            t.join()
            if t.exitcode != 0:
                raise Exception(t.exception)

    if slave_node:
        slave_nodes = slave_node.split(',')
        try:
            go_thread(slave_test)
        except Exception as e:
            json_template["errCode"] = 1
            json_template['errMessage'] = str(e)
            json_template['test_status'] = '2'
            return JsonResponse(json_template, safe=False)

    json_template["errCode"] = 0
    json_template['errMessage'] = "测试成功"
    json_template['test_status'] = "1"
    return JsonResponse(json_template, safe=False)





