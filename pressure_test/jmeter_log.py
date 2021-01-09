#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/4 22:49
# @Author : Li Zihao
# @Email : 1287626466@qq.com
# @File : jmeter_log.py

import os
import json
import re


def get_new_file(path):
    file_name = os.path.split(path)[1]
    file_size = os.path.getsize(path)
    print('%s文件大小：%s' % (file_name, file_size))
    if file_size > 104857600:
        file_size = 104857600
        print('文件大于50M，截取字节' + str(file_size))

    with open(file_path, encoding="utf-8") as fb:
        content = fb.read(file_size)

    new_file = os.path.join(os.path.split(file_path)[0], 'new_' + os.path.split(file_path)[1])
    print('新文件路径：' + new_file)
    with open(new_file, 'w') as fb1:
        fb1.write(content)

    new_file_size = os.path.getsize(new_file)
    print('新文件生成成功，大小：' + str(new_file_size))
    if new_file_size > 0:
        return new_file
    else:
        raise Exception("拷贝文件失败！！")


def anasy_file(key, path):
    print('开始解析文件')
    file_name = os.path.split(path)[1]
    server_name = file_name.split('.')[0]
    server_path = os.path.join(os.path.split(path)[0], server_name)
    print(server_path)
    if not os.path.exists(server_path):
        os.mkdir(server_path)

    with open(path, 'r') as fb:
        content_list = fb.readlines()

    api_list = []
    for line in content_list:
        try:
            line_dict = json.loads(line)
            url = line_dict[key]
            api_name = re.findall(r'/(\w+)\?', url)[0]
            api_file_path = os.path.join(server_path, api_name+'_'+file_name)
            if api_name not in api_list:
                api_list.append(api_name)

            f = open(api_file_path, 'a')
            f.write(url + '\n')
            f.close()
        except Exception as e:
            print(e)
            continue

    print('文件包含接口：' + str(api_list))


def get_10w_file(path):
    file_path, file_name = os.path.split(path)
    file_name_10w = '10w_' + file_name
    file_path_10w = os.path.join(file_path, file_name_10w)
    with open(path, 'r') as fbr:
        line_list = fbr.readlines()

    for i in range(100000):
        f = open(file_path_10w, 'a')
        f.write(line_list[i])
        f.close()

    print(file_path_10w)


if __name__ == '__main__':
    # filepath = r'E:\MyProject\6.大促压测\归档\mkg.log'
    # anasy_file('url', filepath)
    filepath = r'E:\MyProject\6.大促压测\归档\messageFetch\checkNum_messageFetch.log'
    get_10w_file(filepath)




