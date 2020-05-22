import json
import os
import random


from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import shutil
from App.models import Grade, Student, Script, Data
from DjangoModels.settings import MEDIA_ROOT

base_path = r'D:\PythonFile\DjangoTests\DjangoModels\App\static\\'
response_data = {
    'message': 'success',
    'data': {}
}


def response(data):
    data = json.dumps(data, ensure_ascii=False)
    return HttpResponse(data, content_type="application/json,charset=utf-8")


def index(request):
    return HttpResponse('Hello Django')


def students(request):
    return HttpResponse('Get Students Success!!')


def student(request, g_id):
    students = Student.objects.filter(s_grade_id=g_id)
    return render(request, 'students.html', context=locals())


def grades(request):
    grades = Grade.objects.all()
    return render(request, 'grades.html', context=locals())


def get_date(request, day, month, year):
    return HttpResponse('Date: %s - %s - %s' %(year, month, day))


def hava_request(request):
    # print(request.path)
    # print(request.method)
    # print(request.GET)
    # print(request.POST)
    # hobby = request.GET.get('hobby')
    # print(hobby)
    # hobbies = request.GET.getlist('hobby')
    # print(hobbies)
    # print(request.META)
    # for key in request.META:
    #     print(key, request.META.get(key))
    OS = print(request.META.get('OS'))
    return HttpResponse('Request success!!')


def get_student(request):
    return render(request, 'student.html')


def create_student(request):
    name = request.POST.get('username')
    print(request.method)
    print(name)
    return HttpResponse(name)


def hello(request):
    response = HttpResponse()
    response.content = 'Hello world'
    # response.status_code = 404
    return response

# def hello(request):
#     return HttpResponse('Hello world!!')


def get_ticket(request):
    url = reverse('app:hello')
    if random.randrange(10) < 5:
        # return HttpResponseRedirect('/app/hello/')
        return HttpResponseRedirect(url)

    return HttpResponse('Get ticket success')


def hehe(request):
    data = {
        'name': 'Tom',
        'age': 20,
        'job': 'Teacher'
    }
    return HttpResponse(json.dumps(data))


def set_cookie(request):
    response = HttpResponse('Setting Cookies')
    response.set_cookie('username', 'Jack')

    return response


def get_cookie(request):

    username = request.COOKIES.get('username')

    return HttpResponse(username)


def login(request):

    return render(request, 'login.html')


def do_login(request):

    uname = request.POST.get('uname')
    response = HttpResponseRedirect(reverse('app:mine'))
    response.set_cookie('uname', uname)
    response.set_signed_cookie()

    return response


def mine(request):
    uname = request.COOKIES.get('uname')
    print(uname)
    if not uname:
        return HttpResponseRedirect(reverse('app:login'))
    return HttpResponse(uname)


def upload_file(request):
    if request.method == 'GET':
        return render(request, 'upload_file.html')
    elif request.method == 'POST':
        user_name = request.POST.get('username')
        icon = request.FILES.get('file')
        if icon:
            file_name = icon
            file_path = r'D:\PythonFile\DjangoTests\DjangoModels\App\static\upload\JmeterScript\%s' % file_name
            user_model = Script()
            user_model.u_name = user_name
            user_model.u_file_name = file_name
            user_model.u_file = file_path
            user_model.save()
            with open(file_path, 'wb') as save_file:
                for part in icon.chunks():
                    save_file.write(part)
                    save_file.flush()
            return HttpResponse('文件上传成功')


def jmeter_file(request):
    author = request.POST.get('author')
    file = request.FILES.get('script_file')
    file_name = file
    s_model = Script()
    s_model.s_author = author
    s_model.s_file_name = file_name
    s_model.s_file = file
    s_model.save()
    path = s_model.s_file.path
    return HttpResponse('%s上传成功！！%s'% (file_name, path))


def upload_files(request):
    if request.method == 'GET':
        return render(request, 'upload_files.html')
    elif request.method == 'POST':
        author = request.POST.get('author')
        script_file = request.FILES.get('script_file')
        script_file_name = str(script_file)
        upload_base_path = base_path + '\\upload\\'
        script_file_path = upload_base_path + 'JmeterScript\\' + script_file_name
        user_model = Script()
        user_model.s_name = author
        user_model.s_file_name = script_file_name
        user_model.s_file = script_file_path
        user_model.save()
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
            data_file_dirname = upload_base_path + 'JmeterData\\' + os.path.splitext(script_file_name)[0] + '\\'
            if not os.path.exists(data_file_dirname):
                os.makedirs(data_file_dirname)
            data_file_path = data_file_dirname + data_file_name
            data_model.d_file_name = data_file_name
            data_model.d_file = data_file_path
            data_model.d_script = user_model
            data_model.save()
            with open(data_file_path, 'wb') as fb:
                for chunk in file.chunks():
                    fb.write(chunk)
                    fb.flush()
        response_data['message'] = '上传成功'
        response_data['data'] = {'script_file': script_file_name, 'data_file': data_file_names}

        return HttpResponse(json.dumps(response_data, ensure_ascii=False),content_type="application/json,charset=utf-8")


def file_list(request):
    '''
        获取文件列表接口
        路径：/jmeter/filelist
        方法：GET
        入参：无
        '''
    script_list = Script.objects.all().order_by('-create_time')
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


def download_file(request):
    script_id = request.GET.get('script_id')
    s_model = Script.objects.get(id=script_id)
    s_file_name = s_model.s_file_name
    s_file_path = s_model.s_file
    download_path = os.path.join(base_path, 'download', s_file_name)
    print(download_path)
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    shutil.copy(download_path, s_file_path)

    return HttpResponse(s_file_name)