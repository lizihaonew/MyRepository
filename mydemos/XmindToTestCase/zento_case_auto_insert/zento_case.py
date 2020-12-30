# -*- coding: utf-8 -*-
# @Author  : Li Zihao
# @Time    : 2020/9/2 22:06
# @File    : zento_case.py


import re
import requests
import time
from xmind2testcase.utils import get_xmind_testcase_list, get_absolute_path

"""
该脚本用于将xmind文件写的测试用例导入到禅道，不需要转成csv或者xlsx文件，直接插入到禅道库中
用法：
1.基于python3，依赖requests、xmind2testcase，使用pip3安装

"""

type_dict = {
        '功能测试': 'feature',
        '性能测试': 'performance',
        '配置相关': 'config',
        '安装部署': 'install',
        '安全相关': 'security',
        '接口测试': 'interface',
        '其他': 'other'
    }
stage_dict = {
    '单元测试阶段': 'unittest',
    '功能测试阶段': 'feature',
    '集成测试阶段': 'intergrate',
    '系统测试阶段': 'system',
    '冒烟测试阶段': 'smoke',
    '版本验证阶段': 'bvt'
}


def gen_a_testcase_row(testcase_dict):
    product_id, case_module, story_id = gen_case_module(testcase_dict['suite'])
    case_title = testcase_dict['name']
    case_precontion = testcase_dict['preconditions']
    case_step, case_expected_result = gen_case_step_and_expected_result(testcase_dict['steps'])
    case_keyword = ''
    case_priority = gen_case_priority(testcase_dict['importance'])
    case_type, case_stage = gen_case_type(testcase_dict['summary'])
    case_status = '正常'
    row = [product_id, case_module, story_id, case_title, case_precontion, case_step, case_expected_result, case_keyword, case_priority,
           case_type, case_stage, case_status]
    return row


def gen_case_module(module_name):
    if module_name:
        if '/' not in module_name:
            raise Exception('测试模块格式不对')
        res = module_name.split('/')
        product_id = res[0]
        module_name = '/' + res[1]
        if len(res) == 3:
            story_id = res[-1]
        else:
            story_id = ''
        module_name = module_name.replace('（', '(')
        module_name = module_name.replace('）', ')')
    else:
        raise Exception('测试模块格式不对')
    return [product_id, module_name, story_id]


def gen_case_step_and_expected_result(steps):
    case_step = ''
    case_expected_result = ''

    for step_dict in steps:
        case_step += str(step_dict['step_number']) + '. ' + step_dict['actions'].replace('\n', '').strip() + '\n'
        case_expected_result += str(step_dict['step_number']) + '. ' + \
                                step_dict['expectedresults'].replace('\n', '').strip() + '\n' \
            if step_dict.get('expectedresults', '') else ''

    return case_step, case_expected_result


def gen_case_priority(priority):
    mapping = {1: '1', 2: '2', 3: '3', 4: '4'}
    if priority in mapping.keys():
        return mapping[priority]
    else:
        return '2'


def gen_case_type(summary):
    if not summary:
        return ['功能测试', '功能测试阶段']
    count = summary.count('/')
    if count == 0:
        if summary not in list(type_dict.keys()):
            return ['功能测试', '功能测试阶段']
        else:
            return [summary, '功能测试阶段']
    elif count == 1:
        case_type, case_stage = summary.split('/')
        if case_type not in list(type_dict.keys()):
            if case_stage not in list(stage_dict.keys()):
                return ['功能测试', '功能测试阶段']
            else:
                return ['功能测试', case_stage]
        else:
            if case_stage not in list(stage_dict.keys()):
                return [case_type, '功能测试阶段']
            else:
                return [case_type, case_stage]
    else:
        return ['功能测试', '功能测试阶段']


def xmind_to_zentao_api_data(xmind_file):
    xmind_file = get_absolute_path(xmind_file)
    testcases = get_xmind_testcase_list(xmind_file)

    zentao_testcase_rows = []
    for testcase in testcases:
        row = gen_a_testcase_row(testcase)
        zentao_testcase_rows.append(row)

    data_list = []
    for row in zentao_testcase_rows:
        data_dict = dict()
        data_dict['product'] = row[0]
        data_dict['keywords'] = row[7]
        data_dict['title'] = row[3]
        data_dict['module'] = re.findall(r'#(\d+)', row[1])[0]
        data_dict['story'] = row[2]
        data_dict['pri'] = row[8]
        data_dict['type'] = type_dict[row[9]]
        data_dict['stage'] = stage_dict[row[10]]
        data_dict['precondition'] = row[4]
        data_dict['desc'] = row[5]
        data_dict['expect'] = row[6]
        data_dict['status'] = row[-1]
        data_list.append(data_dict)

    return data_list


def get_data(xmind_path):
    res = xmind_to_zentao_api_data(xmind_path)
    data_list = []
    for i in range(1, len(res) + 1):
        j = i - 1
        data_dict = dict()
        data_dict['product'] = res[j]['product']
        data_dict['keywords'] = res[j]['keywords']
        data_dict['title'] = res[j]['title']
        data_dict['module'] = res[j]['module']
        data_dict['story'] = res[j]['story']
        data_dict['pri'] = res[j]['pri']
        data_dict['type'] = res[j]['type']
        data_dict['stage[]'] = res[j]['stage']
        data_dict['color'] = ''
        data_dict['status'] = 'normal'
        data_dict['labels[]'] = ''
        data_dict['files[]'] = ''
        data_dict['precondition'] = res[j]['precondition']
        data_dict['status'] = res[j]['status']
        descs = res[j]['desc'].split('\n')[:-1]
        expect = res[j]['expect'].split('\n')[:-1]
        for n in range(1, len(descs) + 1):
            data_dict['stepType[%s]' % n] = 'item'
            data_dict['steps[%s]' % n] = descs[n - 1][3:]
            data_dict['expects[%s]' % n] = expect[n - 1][3:]

        data_list.append(data_dict)
    return data_list


def login_case(user, passw):
    login_url = 'http://chandao.dangdang.cn//index.php?m=user&f=login'
    data_dict = {
        'account': user,
        'password': passw,
        'passwordStrength': '1',
        'referer': '/',
        'verifyRand': '1984260971',
        'keepLogin': '1'
    }
    header = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    session = requests.Session()
    case_response = session.post(url=login_url, data=data_dict, headers=header)
    if 'f=login' in case_response.text or "登录失败" in case_response.text or "次尝试机会" in case_response.text:
        raise Exception('登录失败，请确认登录账号准确')
    else:
        cookies = session.cookies.get_dict()
        cookie_list = []
        for i in list(cookies.items()):
            cookie_list.append('%s=%s' % (i[0], i[1]))

        cookie = ';'.join(cookie_list)
        return [session, cookie]


def upload_case(xmind_path):
    api_datas = get_data(xmind_path)
    session, cookie = login_case(username, password)
    case_url = 'http://chandao.dangdang.cn/index.php?m=testcase&f=create&productID=0&branch=0&moduleID=0'

    fail_list = []
    start = 1
    for case in api_datas:
        case_response = session.post(url=case_url, data=case)
        res = case_response.text
        if "保存成功" not in res:
            fail_list.append(case['title'])
        else:
            print('完成：' + str(start))
            start += 1

    if fail_list:
        print('以下case添加不成功：\n  ' + str(fail_list))
    else:
        print('success')


if __name__ == '__main__':
    xmind_file_path = input('xmind文件路径：')
    username = input('禅道登录用户名：')
    password = input('禅道登录密码：')
    print('开始导入>>>')
    try:
        upload_case(xmind_file_path)
    except Exception as e:
        print(e)
    print('10秒后关闭窗口')
    time.sleep(10)


