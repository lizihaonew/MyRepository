from datetime import datetime
import json
import os
import logging
import subprocess
import threading
from shlex import quote
import requests
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect, FileResponse, JsonResponse
from django.views.decorators.http import require_POST, require_GET
from DjangoProject.settings import JS_AGENT_HOST
from .models import ProjectRepo, EnvGroup, StressTask, Scenarios, InterfaceName
from .utils import ServerOpt, RecodeThread

logging.basicConfig(
    level=20,
    filename='test.log',
    format='%(levelname)-4s %(asctime)s - %(message)s'
)

json_template = {
    "errCode": 0,
    "errMessage": ""
}

err_template = {
    "errCode": 1,
    "errMessage": ""
}


@require_GET
def project_list(request):
    """ 返回脚本库列表 """
    json_template = {
        "errCode": 0,
        "errMessage": "返回成功"
    }
    try:
        page = request.GET.get('page')
        projects_all_set = ProjectRepo.objects.all()
        project_count = projects_all_set.count()
        if project_count == 0:
            json_template["total"] = 0
            json_template["data"] = []
            return JsonResponse(json_template, safe=False)

        json_template = {
            "errCode": 0,
            "errMessage": "返回成功",
            "total": project_count
        }
        paginator = Paginator(projects_all_set, 10)
        try:
            page_projects = paginator.page(page)
        except PageNotAnInteger:
            page_projects = paginator.page(1)
        except EmptyPage:
            page_projects = paginator.page(paginator.num_pages)

        project_data = []
        for project in page_projects:
            project_dict = {}
            project_dict["project_id"] = project.project_id
            project_dict["project_name"] = project.project_name
            project_dict["project_author"] = project.project_author
            project_dict["project_addr"] = project.project_addr
            project_dict["git_username"] = project.git_username
            project_dict["git_password"] = project.git_password
            project_dict["create_time"] = project.create_time.strftime('%Y-%m-%d %H:%M:%S')
            project_data.append(project_dict)

        json_template["data"] = project_data
    except Exception as e:
        json_template["errCode"] = 1
        json_template["errMessage"] = str(e)
        return JsonResponse(json_template, safe=False)

    json_template["errCode"] = 0
    json_template["errMessage"] = "返回成功"
    return JsonResponse(json_template, safe=False)


@require_POST
def project_add(request):
    """ 添加脚本库 """
    json_template = {
        "errCode": 0,
        "errMessage": ""
    }
    try:
        project_name = request.POST.get('project_name')
        project_author = request.POST.get('project_author')
        project_addr = request.POST.get('project_addr')
        git_username = request.POST.get('git_username')
        git_password = request.POST.get('git_password')

        if "" in [project_name, project_author, project_addr, git_username, git_password]:
            json_template["errCode"] = 1
            json_template['errMessage'] = "必填字段不能为空"
            return JsonResponse(json_template, safe=False)
        if not project_addr.startswith('http://') and not project_addr.startswith('https://'):
            json_template["errCode"] = 1
            json_template['errMessage'] = "git库地址错误，请填写http或https地址"
            return JsonResponse(json_template, safe=False)
        project_model = ProjectRepo()
        project_model.project_name = project_name
        project_model.project_addr = project_addr
        project_model.project_author = project_author
        project_model.git_username = git_username
        project_model.git_password = git_password
        project_model.save()
    except Exception as e:
        json_template["errCode"] = 1
        json_template['errMessage'] = str(e)
        return JsonResponse(json_template, safe=False)

    json_template["errCode"] = 0
    json_template["errMessage"] = "新增成功"
    return JsonResponse(json_template, safe=False)


@require_POST
def project_update(request):
    """ 修改脚本库记录 """
    json_template = {
        "errCode": 0,
        "errMessage": ""
    }
    try:
        project_id = request.POST.get('project_id')
        project_name = request.POST.get('project_name')
        project_author = request.POST.get('project_author')
        project_addr = request.POST.get('project_addr')
        git_username = request.POST.get('git_username')
        git_password = request.POST.get('git_password')
        if "" in [project_id, project_name, project_author, project_addr, git_username, git_password]:
            json_template["errCode"] = 1
            json_template['errMessage'] = "必填字段不能为空"
            return JsonResponse(json_template, safe=False)

        project_set = ProjectRepo.objects.filter(project_id=project_id)
        if not project_set:
            json_template["errCode"] = 1
            json_template['errMessage'] = "修改的内容不存在"
            return JsonResponse(json_template, safe=False)

        if not project_addr.startswith('http://') and not project_addr.startswith('https://'):
            json_template["errCode"] = 1
            json_template['errMessage'] = "git库地址错误，请填写http或https地址"
            return JsonResponse(json_template, safe=False)

        project_model = project_set.first()
        project_model.project_name = project_name
        project_model.project_author = project_author
        project_model.project_addr = project_addr
        project_model.git_username = git_username
        project_model.git_password = git_password
        project_model.save()
    except Exception as e:
        json_template["errCode"] = 1
        json_template['errMessage'] = str(e)
        return JsonResponse(json_template, safe=False)

    json_template["errCode"] = 0
    json_template['errMessage'] = "修改成功"
    return JsonResponse(json_template, safe=False)


@require_GET
def project_del(request):
    """ 删除脚本库 """
    json_template = {
        "errCode": 0,
        "errMessage": ""
    }
    try:
        project_id = request.GET.get('project_id')
        project_set = ProjectRepo.objects.filter(project_id=project_id)
        if not project_set:
            json_template["errCode"] = 1
            json_template['errMessage'] = "删除的内容不存在"
            return JsonResponse(json_template, safe=False)
        project_set.delete()
    except Exception as e:
        json_template["errCode"] = 1
        json_template['errMessage'] = str(e)
        return JsonResponse(json_template, safe=False)

    json_template["errCode"] = 0
    json_template['errMessage'] = "删除成功"
    return JsonResponse(json_template, safe=False)


@require_GET
def env_list(request):
    """ 环境组列表 """
    json_template = {
        "errCode": 0,
        "errMessage": "返回成功"
    }
    set_status_map = {
        "0": "待部署",
        "1": "部署成功",
        "2": "部署失败",
        "3": "部署中"
    }
    test_status_map = {
        '0': "待测试",
        '1': "测试成功",
        '2': "测试失败"
    }
    is_used_map = {
        '0': '空闲',
        '1': '占用'
    }
    try:
        page = request.GET.get('page')
        env_all_set = EnvGroup.objects.all().order_by('-create_time')
        env_count = env_all_set.count()
        if env_count == 0:
            json_template["total"] = 0
            json_template["data"] = []
            return JsonResponse(json_template, safe=False)

        json_template = {
            "errCode": 0,
            "errMessage": "返回成功",
            "total": env_count
        }
        paginator = Paginator(env_all_set, 10)
        try:
            page_projects = paginator.page(page)
        except PageNotAnInteger:
            page_projects = paginator.page(1)
        except EmptyPage:
            page_projects = paginator.page(paginator.num_pages)

        env_data = []
        for env in page_projects:
            env_dict = {}
            env_dict['env'] = env.env_id
            env_dict['env_name'] = env.env_name
            env_dict['owner'] = env.owner
            env_dict['master_node'] = env.master_node
            env_dict['slave_node'] = env.slave_node
            env_dict['create_time'] = env.create_time.strftime('%Y-%m-%d %H:%M:%S')
            time_exist = lambda x: x.strftime('%Y-%m-%d %H:%M:%S') if x else None
            env_dict['test_time'] = time_exist(env.test_time)
            env_dict['set_status_code'] = env.set_status
            env_dict['set_status'] = set_status_map[env.set_status]
            env_dict['test_status_code'] = env.test_status
            env_dict['test_status'] = test_status_map[env.test_status]
            env_dict['is_used_code'] = env.is_used
            env_dict['is_used'] = is_used_map[env.is_used]
            env_data.append(env_dict)

        json_template['data'] = env_data

        json_template["errCode"] = 0
        json_template['errMessage'] = '返回成功'
        return JsonResponse(json_template, safe=False)

    except Exception as e:
        json_template["errCode"] = 1
        json_template['errMessage'] = str(e)
        return JsonResponse(json_template, safe=False)


@require_POST
def add_env(request):
    """ 新增环境组 """
    json_template = {
        "errCode": 0,
        "errMessage": ""
    }
    try:
        env_name = request.POST.get('env_name')
        owner = request.POST.get('owner')
        master_node = request.POST.get('master_node')
        slave_node = request.POST.get('slave_node')
        user_name = request.POST.get('user_name')
        user_password = request.POST.get('user_password')

        if "" in [env_name, owner, master_node, user_name, user_password]:
            json_template["errCode"] = 1
            json_template['errMessage'] = "必填字段不能为空"
            return JsonResponse(json_template, safe=False)

        def isIpV4AddrLegal(ipStr):
            ip_split_list = ipStr.strip().split('.')
            if 4 != len(ip_split_list):
                return False
            for i in range(4):
                try:
                    ip_split_list[i] = int(ip_split_list[i])
                except:
                    print("IP invalid:" + ipStr)
                    return False
            for i in range(4):
                if ip_split_list[i] <= 255 and ip_split_list[i] >= 0:
                    pass
                else:
                    print("IP invalid:" + ipStr)
                    return False
            return True

        hosts = [master_node]
        if slave_node:
            hosts = slave_node.split(',') + hosts

        for host in hosts:
            if not isIpV4AddrLegal(host):
                json_template["errCode"] = 1
                json_template['errMessage'] = "ip地址格式不正确"
                return JsonResponse(json_template, safe=False)
        env_model = EnvGroup.objects.create(
            env_name=env_name,
            owner=owner,
            master_node=master_node,
            slave_node=slave_node,
            user_name=user_name,
            user_password=user_password
        )
        env_model.save()
    except Exception as e:
        json_template["errCode"] = 0
        json_template['errMessage'] = str(e)
        return JsonResponse(json_template, safe=False)

    json_template["errCode"] = 0
    json_template['errMessage'] = "新增成功"
    return JsonResponse(json_template, safe=False)


@require_GET
def del_env(request):
    """ 删除环境组 """
    json_template = {
        "errCode": 0,
        "errMessage": ""
    }
    try:
        env_id = request.GET.get('envId')

        env_set = EnvGroup.objects.filter(env_id=env_id)
        if not env_set:
            json_template["errCode"] = 1
            json_template['errMessage'] = "删除的内容不存在"
            return JsonResponse(json_template, safe=False)

        env_set.delete()
    except Exception as e:
        json_template["errCode"] = 1
        json_template['errMessage'] = str(e)
        return JsonResponse(json_template, safe=False)

    json_template["errCode"] = 0
    json_template['errMessage'] = "删除成功"
    return JsonResponse(json_template, safe=False)


@require_GET
def set_env(request):
    """ 部署环境 """
    json_template = {
        "errCode": 0,
        "errMessage": ""
    }
    try:
        env_id = request.GET.get('envId')
        env_set = EnvGroup.objects.filter(env_id=env_id)
        if not env_set:
            json_template["errCode"] = 1
            json_template['errMessage'] = "环境组不存在"
            return JsonResponse(json_template, safe=False)

        env_model = env_set.first()
        master_node = env_model.master_node
        slave_node = env_model.slave_node
        user_name = env_model.user_name
        user_password = env_model.user_password
        env_model.set_status = '3'
        env_model.save()
        url = JS_AGENT_HOST + '/js' + '/setenv'
        data_dict = {
            'master_node': master_node,
            'slave_node': slave_node,
            'user_name': user_name,
            'user_password': user_password
        }
        data = json.dumps(data_dict)
        header = {
            "Content-Type": "application/json"
        }
        print('>>> 数据校验查询完毕，准备调agent接口执行部署')
        try:
            response = requests.post(url=url, data=data, headers=header).json()
            set_status = response['set_status']
        except Exception:
            json_template["errCode"] = 1
            json_template['errMessage'] = "执行部署操作失败"
            return JsonResponse(json_template, safe=False)

        print('>>> 调用agent接口执行部署完成')
        env_model.set_status = set_status
        env_model.save()
    except Exception as e:
        json_template["errCode"] = 0
        json_template['errMessage'] = str(e)
        return JsonResponse(json_template, safe=False)

    json_template["errCode"] = response["errCode"]
    json_template['errMessage'] = response["errMessage"]
    return JsonResponse(json_template)


@require_GET
def test_env(request):
    """ 检测环境部署 """
    json_template = {
        "errCode": 0,
        "errMessage": ""
    }
    try:
        env_id = request.GET.get('envId')
        env_set = EnvGroup.objects.filter(env_id=env_id)
        if not env_set:
            json_template["errCode"] = 1
            json_template['errMessage'] = "环境组不存在"
            return JsonResponse(json_template, safe=False)

        env_model = env_set.first()
        master_node = env_model.master_node
        slave_node = env_model.slave_node
        user_name = env_model.user_name
        user_password = env_model.user_password
        env_model.test_time = datetime.now()
        url = JS_AGENT_HOST + '/js' + '/testenv'
        data_dict = {
            'master_node': master_node,
            'slave_node': slave_node,
            'user_name': user_name,
            'user_password': user_password
        }
        data = json.dumps(data_dict)
        try:
            response = requests.post(url=url, data=data).json()
            test_status = response['test_status']
        except Exception:
            json_template["errCode"] = 1
            json_template['errMessage'] = "执行检测操作失败"
            return JsonResponse(json_template, safe=False)
        env_model.test_status = test_status
        env_model.save()
    except Exception as e:
        json_template["errCode"] = 1
        json_template['errMessage'] = str(e)
        return JsonResponse(json_template, safe=False)

    json_template["errCode"] = response['errCode']
    json_template['errMessage'] = response['errMessage']
    return JsonResponse(json_template, safe=False)


@require_GET
def download_scripts(request):
    """ 拉取脚本文件 """
    json_template = {
        "errCode": 0,
        "errMessage": "",
        "data": {}
    }
    try:
        project_id = request.GET.get('project_id')
        project_set = ProjectRepo.objects.filter(project_id=project_id)
        if not project_set:
            json_template["errCode"] = 1
            json_template['errMessage'] = "请求的内容不存在"
            return JsonResponse(json_template, safe=False)

        project_model = project_set.first()
        project_id = project_model.project_id
        project_name = project_model.project_name
        project_addr = project_model.project_addr
        git_username = project_model.git_username
        git_password = project_model.git_password

        url = JS_AGENT_HOST + '/js' + '/downloadscripts'
        print(url)
        data_dict = {
            'project_id': project_id,
            'project_name': project_name,
            'project_addr': project_addr,
            'git_username': git_username,
            'git_password': git_password
        }
        data = json.dumps(data_dict)
        header = {
            'Connection': 'close',
            'user-agent': "Mozilla/5.0"
        }
        try:
            response = requests.post(url=url, data=data, headers=header).json()
        except Exception:
            json_template["errCode"] = 1
            json_template['errMessage'] = "执行拉取操作失败"
            return JsonResponse(json_template, safe=False)

        json_template["errCode"] = response['errCode']
        json_template['errMessage'] = response['errMessage']
        json_template['data'] = response['data']
        return JsonResponse(json_template, safe=False)

    except Exception as e:
        json_template["errCode"] = 1
        json_template['errMessage'] = str(e)
        return JsonResponse(json_template, safe=False)


@require_POST
def upload_host(request):
    """ 上传host文件 """
    json_template = {
        "errCode": 0,
        "errMessage": ""
    }
    try:
        envIds = json.loads(request.POST.get('envIds'))
        host_file = request.FILES.get('host_file')

        # host_file_path = '/var/host_file'             # 上传代码之前放开
        host_file_path = 'E:\\host_file'
        if os.path.exists(host_file_path):
            os.remove(host_file_path)
        f = open(host_file_path, 'w')
        f.close()
        with open(host_file_path, 'wb') as fbs:
            for part in host_file.chunks():
                fbs.write(part)
                fbs.flush()

        env_data = []
        for envId in envIds:
            env_set = EnvGroup.objects.filter(env_id=envId)
            if not env_set:
                json_template["errCode"] = 1
                json_template['errMessage'] = "环境组id: %d不存在" % envId
                return JsonResponse(json_template, safe=False)

            data = {}
            env_model = env_set.first()
            master_node = env_model.master_node
            slave_node = env_model.slave_node
            user_name = env_model.user_name
            user_password = env_model.user_password
            hosts = [master_node]
            if slave_node:
                hosts = hosts + slave_node.split(',')
            data['user_name'] = user_name
            data['user_password'] = user_password
            data['hosts'] = hosts
            env_data.append(data)

        # env_list = list(set(env_list))
        data = {
            "env_data": str(env_data)
        }
        url = JS_AGENT_HOST + '/js' + '/uploadhost'
        files = {'host_file': open(host_file_path, 'rb')}
        response = requests.post(url, data=data, files=files).json()

        json_template["errCode"] = response['errCode']
        json_template['errMessage'] = response['errMessage']
        return JsonResponse(json_template, safe=False)

    except Exception as e:
        json_template["errCode"] = 1
        json_template['errMessage'] = str(e)
        return JsonResponse(json_template, safe=False)


@require_POST
def task_add(request):
    """ 新建任务 """
    json_template = {
        "errCode": 0,
        "errMessage": "保存成功"
    }
    try:
        reqest_body = request.body.decode('utf-8')
        reqest_data = json.loads(reqest_body)

        task_name = reqest_data['task_name']
        task_content = reqest_data['task_content']
        task_owner = reqest_data['task_owner']
        git_name = reqest_data['git_name']
        git_addr = reqest_data['git_addr']
        duration = reqest_data['duration']
        next_run_time = reqest_data['next_run_time']
        scenarios = reqest_data['scenarios']
        if "" in [task_name, git_name, git_addr, duration, next_run_time, scenarios]:
            json_template["errCode"] = 1
            json_template['errMessage'] = "必填字段不能为空"
            return JsonResponse(json_template, safe=False)
        print('>>> 校验必填项完成')

        if not duration.isdigit():
            json_template["errCode"] = 1
            json_template['errMessage'] = "运行时长必须是正整数"
            return JsonResponse(json_template, safe=False)

        run_time = datetime.strptime(next_run_time, '%Y-%m-%d %H:%M:%S')
        now_time = datetime.now()

        if run_time < now_time:
            json_template["errCode"] = 1
            json_template['errMessage'] = "定时执行时间不能小于当前时间"
            return JsonResponse(json_template, safe=False)
        elif (run_time - now_time).seconds <= 120:
            json_template["errCode"] = 1
            json_template['errMessage'] = "定时执行时间不能在当前2分钟内"
            return JsonResponse(json_template, safe=False)
        try:
            task_model = StressTask.objects.create(
                    task_name=task_name,
                    task_content=task_content,
                    task_owner=task_owner,
                    git_name=git_name,
                    git_addr=git_addr,
                    duration=duration,
                    next_run_time=next_run_time,
                    hosts_path='0'
                )
        except Exception:
            json_template["errCode"] = 1
            json_template['errMessage'] = '任务数据保存失败'
            return JsonResponse(json_template, safe=False)

        for scenario in scenarios:
            thread_num = scenario['thread_num']
            rampup_time = scenario['rampup_time']
            if not thread_num.isdigit() or not rampup_time.isdigit:
                json_template["errCode"] = 1
                json_template['errMessage'] = "并发数和启动时间不能为空且必须是正整数"
                return JsonResponse(json_template, safe=False)
            env_model = EnvGroup.objects.filter(env_id=scenario['env']).first()
            try:
                scenario_model = Scenarios.objects.create(
                        scenario_file=scenario['scenario_file'],
                        scenario_path=scenario['scenario_path'],
                        is_throughput=scenario['is_throughput'],
                        thread_num=scenario['thread_num'],
                        rampup_time=scenario['rampup_time'],
                        env_name=scenario['env_name'],
                        master_node=scenario['master_node'],
                        slave_node=scenario['slave_node'],
                        env=env_model,
                        task=task_model
                    )
            except Exception:
                json_template["errCode"] = 1
                json_template['errMessage'] = '场景数据保存失败'
                return JsonResponse(json_template, safe=False)

            env_model.is_used = 1
            env_model.save()
            interfaces = scenario['interfaces']
            for interface in interfaces:
                try:
                    interface_model = InterfaceName.objects.create(
                        interface_name=interface['interface_name'],
                        interface_percent=interface['interface_percent'],
                        scenario=scenario_model
                    )

                    interface_model.save()
                except Exception as e:
                    print(e)
                    json_template["errCode"] = 1
                    json_template['errMessage'] = '接口占比数据保存失败'
                    return JsonResponse(json_template, safe=False)

            scenario_model.save()

        task_model.save()

        json_template["errCode"] = 0
        json_template['errMessage'] = "保存成功"
        return JsonResponse(json_template, safe=False)

    except Exception as e:
        json_template["errCode"] = 1
        json_template['errMessage'] = str(e)
        return JsonResponse(json_template, safe=False)


@require_POST
def analyze_script(request):
    """ 解析脚本文件 """
    json_template = {
        "errCode": 0,
        "errMessage": "返回成功"
    }
    try:
        request_body = request.body
        url = JS_AGENT_HOST + '/js' + '/analyzescript'
        header = {
            "Content-Type": "application/json"
        }
        response = requests.post(url, request_body, headers=header).json()

        json_template['errCode'] = response['errCode']
        json_template['errMessage'] = response['errMessage']
        json_template['data'] = response['data']
        return JsonResponse(json_template, safe=False)

    except Exception as e:
        json_template["errCode"] = 1
        json_template['errMessage'] = str(e)
        return JsonResponse(json_template, safe=False)


@require_POST
def sync_scripts(request):
    """ 同步脚本修改 """
    json_template = {
        "errCode": 0,
        "errMessage": ""
    }
    try:
        request_body = request.body
        request_data = json.loads(request_body.decode('utf-8'))

        data_dict = {}
        data_dict['project_id'] = request_data['project_id']
        data_dict['project_name'] = request_data['project_name']

        scenarios = []
        for scenario in request_data['scenarios']:
            dict_scenario = {}
            thread_num = scenario['thread_num']
            rampup_time = scenario['rampup_time']
            if not thread_num.isdigit() or not rampup_time.isdigit():
                json_template["errCode"] = 1
                json_template['errMessage'] = "场景中并发数和启动时间必须为正整数"
                return JsonResponse(json_template, safe=False)

            dict_scenario['scenario_path'] = scenario['scenario_path']
            dict_scenario['is_throughput'] = scenario['is_throughput']
            env = scenario['env']
            try:
                env_model = EnvGroup.objects.get(env_id=env)
            except Exception as e:
                print(e)
                json_template["errCode"] = 1
                json_template['errMessage'] = "选择的环境组不存在"
                return JsonResponse(json_template, safe=False)
            else:
                dict_scenario['master_node'] = env_model.master_node
                dict_scenario['user_name'] = env_model.user_name
                dict_scenario['user_password'] = env_model.user_password

            if scenario['is_throughput']:
                interfaces = scenario['interfaces']
                percents = [eval(interface['interface_percent']) for interface in interfaces]
                if sum(percents) <= 0 or sum(percents) > float(100):
                    json_template["errCode"] = 1
                    json_template['errMessage'] = "每个场景的接口占比之和不能小于0或大于100"
                    return JsonResponse(json_template, safe=False)
                dict_scenario['interfaces'] = scenario['interfaces']
            scenarios.append(dict_scenario)

        data_dict['scenarios'] = scenarios

        data = json.dumps(data_dict)
        url = JS_AGENT_HOST + '/js' + '/syncscripts'
        header = {
            "Content-Type": "application/json"
        }
        try:
            response = requests.post(url=url, data=data, headers=header).json()
        except Exception:
            json_template["errCode"] = 1
            json_template['errMessage'] = "执行同步操作失败"
            return JsonResponse(json_template, safe=False)

        json_template["errCode"] = response['errCode']
        json_template['errMessage'] = response['errMessage']
        return JsonResponse(json_template, safe=False)

    except Exception as e:
        json_template["errCode"] = 1
        json_template['errMessage'] = str(e)
        return JsonResponse(json_template, safe=False)


