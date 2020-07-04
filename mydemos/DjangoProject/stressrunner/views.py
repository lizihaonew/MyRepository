import json

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, FileResponse, JsonResponse
from django.views.decorators.http import require_POST, require_GET
from .models import ProjectRepo, EnvGroup

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
        "errMessage": ""
    }
    projects_all_set = ProjectRepo.objects.all()
    if projects_all_set.count() == 0:
        json_template["data"] = []
    else:
        project_data = []
        for project in projects_all_set:
            project_dict = {}
            project_dict["project_id"] = project.project_id
            project_dict["project_name"] = project.project_name
            project_dict["project_author"] = project.project_author
            project_dict["project_addr"] = project.project_addr
            project_dict["create_time"] = project.create_time.strftime('%Y-%m-%d %H:%M:%S')
            project_data.append(project_dict)

        json_template["data"] = project_data

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
    req_body = json.loads(request.body)
    req_data = req_body.values()
    if "" in req_data:
        json_template["errCode"] = 1
        json_template['errMessage'] = "必填字段不能为空"
        return JsonResponse(json_template, safe=False)
    keys = ("project_name", "project_author", "project_addr")
    project_name, project_author, project_addr = [req_body[k] for k in keys]
    project_model = ProjectRepo()
    project_model.project_name = project_name
    project_model.project_addr = project_addr
    project_model.project_author = project_author
    project_model.save()

    template = json_template
    json_template["errCode"] = 0
    template["errMessage"] = "新增成功"
    return JsonResponse(template, safe=False)


@require_POST
def project_update(request):
    """ 修改脚本库记录 """
    json_template = {
        "errCode": 0,
        "errMessage": ""
    }
    req_body = json.loads(request.body)
    req_data = list(req_body.values())
    if "" in req_data:
        json_template["errCode"] = 1
        json_template['errMessage'] = "必填字段不能为空"
        return JsonResponse(json_template, safe=False)

    keys = ("project_id", "project_name", "project_author", "project_addr")
    project_id, project_name, project_author, project_addr = [req_body[k] for k in keys]

    project_set = ProjectRepo.objects.filter(project_id=project_id)
    if not project_set:
        json_template["errCode"] = 1
        json_template['errMessage'] = "修改的内容不存在"
        return JsonResponse(json_template, safe=False)

    project_model = project_set.first()
    project_model.project_name = project_name
    project_model.project_author = project_author
    project_model.project_addr = project_addr
    project_model.save()

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
    project_id = request.GET.get('project_id')
    project_set = ProjectRepo.objects.filter(project_id=project_id)
    if not project_set:
        json_template["errCode"] = 1
        json_template['errMessage'] = "删除的内容不存在"
        return JsonResponse(json_template, safe=False)

    project_set.delete()
    json_template["errCode"] = 0
    json_template['errMessage'] = "删除成功"
    return JsonResponse(json_template, safe=False)


@require_GET
def env_list(request):
    """ 环境组列表 """
    json_template = {
        "errCode": 0,
        "errMessage": ""
    }
    set_status_map = {
        "0": "待部署",
        "1": "部署成功",
        "2": "部署失败",
        "3": "部署中"
    }
    test_status_map = {
        '0': u"待测试",
        '1': u"测试成功",
        '2': u"测试失败"
    }
    is_used_map = {
        '0': '空闲',
        '1': '占用'
    }
    env_all_set = EnvGroup.objects.all()
    if env_all_set.count() == 0:
        json_template["data"] = []
    else:
        env_data = []
        for env in env_all_set:
            env_dict = {}
            env_dict['id'] = env.env_id
            env_dict['env_name'] = env.env_name
            env_dict['author'] = env.owner
            env_dict['master'] = env.master_node
            env_dict['slave'] = env.slave_node
            env_dict['create_time'] = env.create_time.strftime('%Y-%m-%d %H:%M:%S')
            time_exist = lambda x: x.strftime('%Y-%m-%d %H:%M:%S') if x else None
            env_dict['test_time'] = time_exist(env.test_time)
            env_dict['set_status'] = set_status_map[env.set_status]
            env_dict['test_status'] = test_status_map[env.test_status]
            env_dict['is_used'] = is_used_map[env.is_used]
            env_data.append(env_dict)

        json_template['data'] = env_data[::-1]

    json_template['errMessage'] = '返回成功'
    return JsonResponse(json_template, safe=False)


@require_POST
def add_env(request):
    """ 新增环境组 """
    json_template = {
        "errCode": 0,
        "errMessage": ""
    }
    req_body = json.loads(request.body)
    must_data_keys = ['env_name', 'owner', 'master_node', 'user_name', 'user_password']
    req_data = [req_body[k] for k in must_data_keys]
    if "" in req_data:
        json_template["errCode"] = 1
        json_template['errMessage'] = "必填字段不能为空"
        return JsonResponse(json_template, safe=False)

    must_data_keys.append('slave_node')
    env_name, owner, master_node, user_name, user_password, slave_node = [req_body[k] for k in must_data_keys]
    env_model = EnvGroup.objects.create(
        env_name=env_name,
        owner=owner,
        master_node=master_node,
        slave_node=slave_node,
        user_name=user_name,
        user_password=user_password
    )
    env_model.save()

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
    env_id = request.GET.get('envId')

    env_set = EnvGroup.objects.filter(env_id=env_id)
    if not env_set:
        json_template["errCode"] = 1
        json_template['errMessage'] = "删除的内容不存在"
        return JsonResponse(json_template, safe=False)

    env_set.delete()
    json_template["errCode"] = 0
    json_template['errMessage'] = "删除成功"
    return JsonResponse(json_template, safe=False)







