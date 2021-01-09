# -*- coding: utf-8 -*-
# @Author  : Li Zihao
# @Time    : 2020/8/18 21:54
# @File    : modify_log.py

import os
import re


def sub_data(lines):
    new_lines = []
    for line in lines:
        if 'user_client=iphone' in line or 'user_client=android' in line:
            line = re.sub(r'client_version=[\d.]+', 'client_version=999.9.9', line)
        new_lines.append(line)
    return new_lines


def get_files(file_path):
    txt_files = []
    for path, folders, files in os.walk(file_path, topdown=True):
        for f in files:
            if f.endswith('.txt'):
                txt_path = os.path.join(os.path.abspath(path), f)
                txt_files.append(txt_path)
    return txt_files


def new_files(file):
    with open(file, 'r') as obr:
        lines = obr.readlines()

    file_path, file_name = os.path.split(file)

    txt_path = file_path + '\\txt_files'
    txt_new_lines = sub_data(lines)
    if not os.path.exists(txt_path):
        os.mkdir(txt_path)
    new_path = os.path.join(txt_path, file_name)
    with open(new_path, 'w') as obw:
        obw.writelines(txt_new_lines)

    dat_new_lines = ['req_url\n'] + sub_data(lines)
    dat_name = os.path.splitext(file_name)[0] + '.dat'
    dat_path = file_path + '\\dat_files'
    if not os.path.exists(dat_path):
        os.mkdir(dat_path)
    new_path = os.path.join(dat_path, dat_name)
    with open(new_path, 'w') as obw:
        obw.writelines(dat_new_lines)


# def new_txt_file(file):
#     with open(file, 'r') as obr:
#         lines = obr.readlines()
#
#     new_lines = sub_data(lines)
#     file_path, file_name = os.path.split(file)
#     # dat_name = os.path.splitext(file_name)[0] + '.dat'
#     txt_path = file_path + '\\txt_files'
#     if not os.path.exists(txt_path):
#         os.mkdir(txt_path)
#     new_path = os.path.join(txt_path, file_name)
#     with open(new_path, 'w') as obw:
#         obw.writelines(new_lines)


def main():
    folder_path = input('请输入目录路径：')
    txt_files = get_files(folder_path)
    for file in txt_files:
        new_files(file)
        # new_txt_file(file)


if __name__ == '__main__':
    main()


