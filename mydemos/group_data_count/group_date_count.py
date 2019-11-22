#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : Li ZiHao
# @Time     : 2019/11/22 22:48
# @File     : group_date_count.py

import datetime
import time
import opt_group_mysql
from opt_group_mysql import Optsql


class GroupDateCount(Optsql):
    def __init__(self, dept, date, name):
        self.dept = dept
        self.name = name
        self.entId = self.ent_id[self.name]
        self.cur, self.conn = self.conn_mysql("shengmei")
        date_today = datetime.date.today()
        default_date = date_today - datetime.timedelta(days=1)
        self.current_month = time.strftime('%Y-%m')
        if date == '0':
            self.date = default_date
            self.yesterday = str(self.date - datetime.timedelta(days=1))
        else:
            self.date = date
            year, month, day = self.date.split('-')
            self.yesterday = str(datetime.date(int(year), int(month), int(day)) - datetime.timedelta(days=1))

        if dept == '0':
            self.dept_sql = ""
        else:
            self.dept_sql = " AND deptCode like '%s'" % dept

    def get_amount(self, sql):
        res = super(GroupDateCount, self).execute_select(self.cur, sql)[0][0]
        if res:
            return str(res)
        else:
            return '0'

    def object_close(self):
        super(GroupDateCount, self).object_close(self.cur, self.conn)

    def get_name_date(self):
        ent_name = self.ent_name

    def invest_amount_today(self):
        ''' 当日投资总额 '''
        invest_amount_today_sql = "SELECT SUM(todayInvestAmount) FROM `data_statistics_day` WHERE entId='{0}' AND " \
                                  "DAY='{1}'{2};".format(self.entId, self.date, self.dept_sql)
        invest_amount_today = self.get_amount(invest_amount_today_sql)
        return invest_amount_today

    # def invest_count_today(self):





def group_date_count_main(dept, date, name):
    gdcm = GroupDateCount(dept, date, name)
    company_name = gdcm.ent_name[name]
    invest_amount_today = gdcm.invest_amount_today()


    gdcm.object_close()

    comment = '销售日报，统计结果如下：' + '( 公司名称：%s, 部门：%s, 日期：%s )'%(company_name, dept, date) + '\n'\
        '当日投资总额：' + invest_amount_today + '\n'

    print(comment)


if __name__ == '__main__':
    group_date_count_main('0', '0', 'nami')
    # group_date_count_main('0', '2019-11-20', 'nami')




