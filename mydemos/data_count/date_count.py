#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : Li ZiHao
# @Time     : 2019/11/2 0:38
# @File     : date_count.py

import datetime
import time
from opt_mysql import Optsql


class DateCount(Optsql):
    def __init__(self, dept, date):
        self.dept = dept
        self.cur = self.conn_mysql()
        date_today = datetime.date.today()
        self.today = str(date_today)
        self.yesterday = str(date_today - datetime.timedelta(days=1))
        self.current_month = time.strftime('%Y-%m')
        if date == '0':
            self.date = self.today
        else:
            self.date = date

    def exchange_None(self,para):
        if para:
            return para
        else:
            return 0

    def dept_name_date(self):
        ''' 获取部门名称和日期 '''
        dept_name_sql = "SELECT NAME FROM `wbs_department` WHERE CODE = '{0}';".format(self.dept)
        dept_name = self.execute_select(self.cur,dept_name_sql)[0][0]
        the_datetime = str(self.date)
        return [dept_name, the_datetime]

    def invest_amount(self):
        '''当日投资总额 '''
        today_amount_sql = "SELECT SUM(trans_amount) FROM `ns_order` WHERE trans_time " \
                          "LIKE '{0}%' AND dept_code LIKE '{1}%';".format(self.date, self.dept)
        today_amount = self.exchange_None(self.execute_select(self.cur,today_amount_sql)[0][0])
        return str(today_amount)

    def invest_count(self):
        '''当日投资笔数'''
        today_count_sql = "SELECT COUNT(1) FROM `ns_order` WHERE trans_time " \
                          "LIKE '{0}%' AND dept_code LIKE '{1}%';".format(self.date, self.dept)
        today_count = self.exchange_None(self.execute_select(self.cur,today_count_sql)[0][0])
        return str(today_count)

    def today_performance_amount(self):
        '''当日投资业绩'''
        today_amount_sql = "SELECT SUM(performance_amount) FROM `ns_sop_order_snapshot` WHERE " \
                              "trans_time LIKE '{0}%' AND department_no LIKE '{1}%';".format(self.date, self.dept)
        today_performance_amount = self.exchange_None(self.execute_select(self.cur,today_amount_sql)[0][0])

        return str(today_performance_amount)

    def repayment_amount_today(self):
        '''当日还款总额'''
        repayed_amount_sql = "SELECT SUM(actual_exit_amount) FROM `wbs_received_payment` WHERE " \
                             "Convert(actual_exit_time,CHAR(20)) LIKE '{0}%' AND STATUS = 1 AND dept_code " \
                             "LIKE '{1}%';".format(self.date, self.dept)
        repayed_amount_today = self.exchange_None(self.execute_select(self.cur,repayed_amount_sql)[0][0])
        return str(repayed_amount_today)










def date_count_main(dept, date):
    dcm = DateCount(dept, date)
    dept_name, the_datetime = dcm.dept_name_date()
    today_amount = dcm.invest_amount()
    today_count = dcm.invest_count()
    today_performance_amount = dcm.today_performance_amount()
    repayed_amount_today = dcm.repayment_amount_today()




    comment = '销售日报，统计结果如下：' + '(部门：%s, 日期：%s)'%(dept_name, the_datetime) + '\n'\
        '当日投资总额：' + today_amount + '\n'\
        '当日投资笔数：' + today_count + '\n'\
        '当日投资业绩：' + today_performance_amount + '\n'\
        '当日还款总额：' + repayed_amount_today + '\n'\


    print(comment)


if __name__ == '__main__':
    date_count_main('SHNMCW0002', '0')
    # date_count_main('SHNMCW0002', '2019-11-01')