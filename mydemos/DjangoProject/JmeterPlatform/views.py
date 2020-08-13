from django.shortcuts import render

import json
import os
import random

from django.http import HttpResponse, HttpResponseRedirect, FileResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse
import shutil
import zipfile
from DjangoProject.settings import MEDIA_ROOT
from JmeterPlatform import models
from JmeterPlatform.models import Data, Script, Person, PersonInfo, Author, Book, Child, Colors

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


def json_response(request):
    data = {
        'errCode': 200,
        'errMessage': 'ok',
        'data': {
            'users': [
                {
                    'name': 'Tom',
                    'age': 20
                },
                {
                    'name': 'Jerry',
                    'age': 18
                }
            ]
        }
    }
    res = JsonResponse(data=data)
    res.status_code = 404
    return res


# def my_script(request):
    # # 普通查询方式
    # person_set = Person.objects.all().first()
    # info_set = PersonInfo.objects.filter(person=person_set)
    # print('person_set', person_set.name)
    # print('info_set', info_set[0].birth)
    #
    # # 关联查询，正查，即先查主表，通过主表数据关联从表数据
    # person_set2 = Person.objects.all().first()
    # personInfo = person_set2.personinfo     # personinfo是PersonInfo模型类的小写
    # print(personInfo.birth)
    #
    # # 关联查询，反查，即先查从表，通过从表数据关联出主表数据
    # info_set3 = PersonInfo.objects.filter(tel='13000000001').first()
    # person_set3 = info_set3.person
    # print(person_set3.name)
    #
    # person_obj4 = Person.objects.create(
    #     name='person4',
    #     age=20
    # )
    # person_obj4.save()
    # info_obj4 = PersonInfo.objects.create(
    #     sex=1,
    #     birth='2020-10-11',
    #     tel='13000000004',
    #     person=person_obj4
    # )
    # info_obj4.save()
    # print(info_obj4.tel)

    # person_obj5 = Person.objects.all().first()
    # info_obj5 = person_obj5.personinfo
    # print(info_obj5.tel)
    #
    # person_obj6 = Person.objects.all().last()
    # info_obj6 = person_obj6.info
    # print(info_obj6.tel)
    # return HttpResponse('ok')


# def my_script(request):
#     author_obj = Author.objects.create(
#         name='author1',
#         age=20
#     )
#     author_obj.save()
#
#     for i in range(3):
#         book_obj = Book.objects.create(
#             book_name='book_%s' % str(i),
#             page=i * 20,
#             author=author_obj
#         )
#         book_obj.save()
#
#     # 正向查询
#     author_obj = Author.objects.all().first()
#     book_set = author_obj.book.all()
#     for book_obj in book_set:
#         print(book_obj.book_name)
#
#     # 反向查询
#     book_obj2 = Book.objects.first()
#     author_obj2 = book_obj2.author
#     print(author_obj2.name)
#
#     return HttpResponse('ok')


def my_script(request):
    # 写法1：
    child_obj = models.Child.objects.get(name="小明")  # 写法：子表对象.子表多对多字段.过滤条件(all()/filter())
    print(child_obj.favor.all())
    # 写法2，反向从母表入手：
    print(models.Colors.objects.filter(child__name="小明"))  # 母表对象.filter(子表表名小写__子表字段名="过滤条件")

    return HttpResponse('ok')





