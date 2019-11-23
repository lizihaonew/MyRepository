#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : Li ZiHao
# @Time     : 2019/11/23 16:36
# @File     : group_month_count.py

import datetime
import time
from opt_group_mysql import Optsql


class GroupMonthCount(Optsql):
    def __init__(self, dept, date, name):
        self.dept = dept
        self.name = name
        self.cur, self.conn = self.conn_mysql("shengmei")
        date_today = datetime.date.today()
        self.today = str(date_today)
        self.yesterday = str(date_today - datetime.timedelta(days=1))
        if date == '0':
            self.current_month = time.strftime('%Y-%m')
        else:
            self.current_month = date

        if self.current_month[-2:] == '01':
            self.last_month = str(eval(self.current_month[:4] + '-1')) + '-12'
        else:
            self.last_month = self.current_month[:4] + '-%s' % str(int(self.current_month[-2:])-1).zfill(2)

        if dept == '0':
            self.dept_sql = ""
        else:
            self.dept_sql = " AND deptCode like '%s'" % dept

    def get_amount(self, sql):
        res = super(GroupMonthCount, self).execute_select(self.cur, sql)[0][0]
        if res:
            return str(res)
        else:
            return '0'

    def object_close(self):
        super(GroupMonthCount, self).object_close(self.cur, self.conn)

    def get_dept_date(self):
        the_date = self.date
        if self.dept == '0':
            the_dept = '查询整个公司'
        else:
            the_dept = self.execute_select(self.cur, "SELECT deptName FROM `data_statistics_day` WHERE deptCode='%s';" % self.dept)[0][0]
        return [the_date, the_dept]