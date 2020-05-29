from django.shortcuts import render

import json
import os
import random

from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.shortcuts import render
from django.urls import reverse
import shutil
import zipfile
from DjangoProject.settings import MEDIA_ROOT
from JmeterPlatform import models
from JmeterPlatform.models import Data, Script

response_data = {
    'message': '',
    'data': {}
}


def response(data):
    data = json.dumps(data, ensure_ascii=False)
    return HttpResponse(data, content_type="application/json,charset=utf-8")


def upload_files(request):
    '''
    上传脚本文件接口
    路径：/jmeter/uploadfiles
    方法：POST
    入参：
    {
        "author": 作者名称,
        "script_file", Jmeter脚本文件,
        "data_files": 数据文件,
    }
    '''
    author = request.POST.get('author')
    script_file = request.FILES.get('script_file')
    script_file_name = str(script_file)
    upload_path = MEDIA_ROOT + 'upload\\'
    script_file_dirpath = upload_path + 'JmeterScript\\'
    if not os.path.exists(script_file_dirpath):
        os.makedirs(script_file_dirpath)
    script_file_path = script_file_dirpath + script_file_name
    if Script.objects.filter(s_file_name=script_file_name).exists():
        response_data['message'] = '上传失败，文件%s已经存在' % script_file_name
        response_data['data'] = {}
        return response(response_data)

    s_model = Script()
    s_model.s_author = author
    s_model.s_file_name = script_file_name
    s_model.s_file = script_file_path
    s_model.save()

    with open(script_file_path, 'wb') as fbs:
        for part in script_file.chunks():
            fbs.write(part)
            fbs.flush()

    data_files = request.FILES.getlist('data_files')
    data_file_names = []

    for file in data_files:
        data_file_name = str(file)
        data_file_names.append(data_file_name)
        data_model = Data()
        data_file_dirname = upload_path + 'JmeterData\\' + os.path.splitext(script_file_name)[0] + '\\'
        if not os.path.exists(data_file_dirname):
            os.makedirs(data_file_dirname)
        data_file_path = data_file_dirname + data_file_name
        data_model.d_file_name = data_file_name
        data_model.d_file = data_file_path
        data_model.d_script = s_model
        data_model.save()
        with open(data_file_path, 'wb') as fb:
            for chunk in file.chunks():
                fb.write(chunk)
                fb.flush()
    response_data['message'] = '操作成功'
    response_data['data'] = {'script_file': script_file_name, 'data_file': data_file_names}

    return response(response_data)


def file_list(request):
    '''
        获取文件列表接口
        路径：/jmeter/filelist
        方法：GET
        入参：无
        '''
    script_list = Script.objects.all().order_by('-create_time')
    print(script_list)
    files_ob = []
    for ob in script_list:
        script_author = ob.s_author
        script_name = ob.s_file_name
        create_time = ob.create_time.strftime('%Y-%m-%d %H:%M:%S')
        script_id = ob.id
        data_files_name_list = [d.d_file_name for d in ob.d_script.all()]
        file_ob = {
            'script_id': script_id,
            'script_author': script_author,
            'script_name': script_name,
            'create_time': create_time,
            'data_files': data_files_name_list
        }
        files_ob.append(file_ob)
    response_data['message'] = '操作成功'
    response_data['data'] = files_ob
    return response(response_data)


def download_file(request):
    '''
    下载接口，将脚本文件和数据文件打包下载
    路径：/jmeter/downloadfile
    方法：GET
    入参：script_id
    '''
    script_id = request.GET.get('script_id')
    s_model = Script.objects.get(id=script_id)
    s_file_name = s_model.s_file_name
    script_name = os.path.splitext(s_file_name)[0]
    s_file_path = s_model.s_file
    script_download_path = os.path.join(MEDIA_ROOT, 'download', script_name)
    d_file_path = os.path.join(MEDIA_ROOT, 'upload\\JmeterData', script_name)
    data_download_path = script_download_path + '\\data'
    d_model = s_model.d_script
    d_file_list = [d.d_file for d in d_model.all()]
    if not os.path.exists(script_download_path):
        os.makedirs(script_download_path, mode=0o777)
        os.makedirs(data_download_path, mode=0o777)
    shutil.copy(s_file_path, script_download_path)
    for file in d_file_list:
        shutil.copy(file, data_download_path)

    download_file_name = '.'.join([script_name, 'tar.gz'])
    download_file_path = os.path.join(MEDIA_ROOT, 'download', download_file_name)
    os.system('tar -cvf %s %s' % (download_file_name, script_download_path))
    # with open(download_file_path, 'w') as file:
    #     file.write('aaaa')
    if os.path.exists(download_file_path):
        shutil.rmtree(script_download_path)
        file = open(download_file_path, 'rb')
        response = FileResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="%s"' % download_file_name
        return response


def delete_file(request):
    '''
    删除脚本文件和相关的数据文件
    路径：/jmeter/deletefile
    方法：GET
    入参：script_id
    '''
    script_id = request.GET.get('script_id')
    s_model = Script.objects.get(pk=script_id)
    s_file_name = s_model.s_file_name
    s_file_path = s_model.s_file
    d_file_path = os.path.join(MEDIA_ROOT, 'upload\\JmeterData\\', os.path.splitext(s_file_name)[0])
    Data.objects.filter(d_script=script_id).delete()
    s_model.delete()
    os.remove(s_file_path)
    if os.path.exists(d_file_path):
        shutil.rmtree(d_file_path)

    response_data['message'] = '操作成功'
    response_data['data'] = "文件%s及其数据文件已经删除" % s_file_name

    return response(response_data)


def add_task(request):
    task_name = request.GET.get('task_name')
    response_data['message'] = '操作成功'
    response_data['data'] = task_name
    return response(response_data)



