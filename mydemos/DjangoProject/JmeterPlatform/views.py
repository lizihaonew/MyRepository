from django.shortcuts import render

import json
import os
import random

from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import shutil
from JmeterPlatform.models import Data, Script

static_base_path = r'E:\PythonFiles\DjangoProject\static\\'
response_data = {
    'message': 'success',
    'data': {}
}


def response(data):
    data = json.dumps(data, ensure_ascii=False)
    return HttpResponse(data, content_type="application/json,charset=utf-8")


# def upload_files(request):
#     '''
#     上传脚本文件接口
#     路径：/jmeter/uploadfiles
#     方法：POST
#     入参：
#     {
#         "username": 作者名称,
#         "script_file", Jmeter脚本文件,
#         "data_files": 数据文件,
#     }
#     '''
#     if request.method == 'POST':
#         author = request.POST.get('author')
#         script_file = request.FILES.get('script_file')
#         script_file_name = str(script_file)
#         upload_path = static_base_path + '\\upload\\'
#         script_file_dirpath = upload_path + 'JmeterScript\\'
#         if not os.path.exists(script_file_dirpath):
#             os.makedirs(script_file_dirpath)
#         script_file_path = script_file_dirpath + script_file_name
#         print(Script.objects.get(s_file_name=script_file_name))
#         if Script.objects.exists(s_file_name=script_file_name):
#             s_model = Script.objects.get(s_file_name=script_file_name)
#         else:
#             s_model = Script()
#         s_model.s_author = author
#         s_model.s_file_name = script_file_name
#         s_model.s_file = script_file_path
#         s_model.save()
#         with open(script_file_path, 'wb') as fbs:
#             for part in script_file.chunks():
#                 fbs.write(part)
#                 fbs.flush()
#
#         data_files = request.FILES.getlist('data_files')
#         data_file_names = []
#
#         for file in data_files:
#             data_file_name = str(file)
#             data_file_names.append(data_file_name)
#             data_model = Data()
#             data_file_dirname = upload_path + 'JmeterData\\' + os.path.splitext(script_file_name)[0] + '\\'
#             if not os.path.exists(data_file_dirname):
#                 os.makedirs(data_file_dirname)
#             data_file_path = data_file_dirname + data_file_name
#             data_model.d_file_name = data_file_name
#             data_model.d_file = data_file_path
#             data_model.d_script = s_model
#             data_model.save()
#             with open(data_file_path, 'wb') as fb:
#                 for chunk in file.chunks():
#                     fb.write(chunk)
#                     fb.flush()
#         response_data['data'] = {'script_file': script_file_name, 'data_file': data_file_names}
#
#         return HttpResponse(json.dumps(response_data, ensure_ascii=False), content_type="application/json,charset=utf-8")


def file_list(request):
    '''
        获取文件列表接口
        路径：/jmeter/filelist
        方法：GET
        入参：无
        '''
    script_list = Script.objects.order_by('-create_time')
    files_ob = []
    for ob in script_list:
        script_author = ob.s_author
        script_name = ob.s_file_name
        create_time = ob.create_time.strftime('%Y-%m-%d %H:%M:%S')
        script_id = ob.id
        data_files_name_list =[d.d_file_name for d in ob.data_set.all()]
        file_ob = {
            'script_id': script_id,
            'script_author': script_author,
            'script_name': script_name,
            'create_time': create_time,
            'data_files': data_files_name_list
        }
        files_ob.append(file_ob)
    response_data['data'] = files_ob
    return response(response_data)


def upload_files(request):
    '''
    上传脚本文件接口
    路径：/jmeter/uploadfiles
    方法：POST
    入参：
    {
        "username": 作者名称,
        "script_file", Jmeter脚本文件,
        "data_files": 数据文件,
    }
    '''
    if request.method == 'POST':
        author = request.POST.get('author')
        script_file = request.FILES.get('script_file')
        script_file_name = os.path.splitext(str(script_file))[0]

        s_model = Script()
        s_model.s_author = author
        s_model.s_file_name = script_file_name
        s_model.s_file = script_file
        s_model.save()

        data_files = request.FILES.getlist('data_files')
        data_file_names = []

        for file in data_files:
            data_file_name = os.path.splitext(str(file))[0]
            data_file_names.append(data_file_name)
            data_model = Data()
            # data_file_dirname = upload_path + 'JmeterData\\' + os.path.splitext(script_file_name)[0] + '\\'
            # if not os.path.exists(data_file_dirname):
            #     os.makedirs(data_file_dirname)
            # data_file_path = data_file_dirname + data_file_name
            data_model.d_file_name = data_file_name
            data_model.d_file = file
            data_model.d_script = s_model
            data_model.save()
            # with open(data_file_path, 'wb') as fb:
            #     for chunk in file.chunks():
            #         fb.write(chunk)
            #         fb.flush()
        response_data['data'] = {'script_file': script_file_name, 'data_file': data_file_names}

        return HttpResponse(json.dumps(response_data, ensure_ascii=False), content_type="application/json,charset=utf-8")

