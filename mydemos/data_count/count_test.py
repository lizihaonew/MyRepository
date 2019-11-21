#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : Li ZiHao
# @Time     : 2019/11/2 0:39
# @File     : count_test.py

from date_count import date_count_main
from dept_count import dept_count_main
from employee_count import employee_count_main
from month_count import month_count_main

# #########################
# 配置count_type字段值
# bumen = 销售快报 - 按部门统计  SHNMCW0002  1
# yuangong = 销售快报 - 按员工统计   13666666661
# ribao = 销售日报  SHNMCW0002  2019-11-01
# yuebao = 销售月报 SHNMCW0002  2019-11

count_type = 'bumen'
# #########################


if count_type == 'bumen':
    print('现在操作的是 销售快报 - 按部门统计。')
    dept = input('请输入部门code：')
    print('请输入资产端id：0-全部资产端，1-汇盈金服，2-汇经社，3-恒普')
    asset = int(input('请输入资产端id：'))
    print('==================================>>>')
    if asset in (0, 1, 2, 3):
        dept_count_main(dept, asset)
    else:
        print('资产端id输入错误！！！')
elif count_type == 'yuangong':
    print('现在操作的是 销售快报 - 按员工统计。')
    employee_mobile = input('请输入员工手机号：')
    print('==================================>>>')
    employee_count_main(employee_mobile)
elif count_type == 'ribao':
    print('现在操作的是 销售日报。')
    dept = input('请输入部门code：')
    print('请输入需要搜索的日期：0-默认的今天，日期格式如：2019-11-01')
    date = input('请输入日期：')
    print('==================================>>>')
    date_count_main(dept, date)
elif count_type == 'yuebao':
    print('现在操作的是 销售月报。')
    dept = input('请输入部门code：')
    print('请输入需要搜索的日期：0-默认的今天，日期格式如：2019-11')
    date = input('请输入日期：')
    print('==================================>>>')
    month_count_main(dept, date)
else:
    print('count_type 字段输入错误')

