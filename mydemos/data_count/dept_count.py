#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : Li ZiHao
# @Time     : 2019/10/30 21:43
# @File     : dept_count.py

import datetime
from opt_mysql import Optsql


class DeptCount(Optsql):
    def __init__(self, dept, asset=None):
        self.dept = dept
        # self.asset = asset
        if asset:
            self.asset_sql = 'and asset_id = %s' % asset
        else:
            self.asset_sql = ''
        self.cur = self.conn_mysql()
        date_today = datetime.date.today()
        self.today = str(date_today)
        self.yesterday = str(date_today - datetime.timedelta(days=1))

    def invest_amount(self):
        '''本日投资总额、昨日投资总额'''
        # if self.asset:
        #     asset_sql = 'and asset_id = %s' % self.asset
        # else:
        #     asset_sql = ''
        today_count_sql = "SELECT SUM(trans_amount) FROM `ns_order` WHERE trans_time " \
                          "LIKE '{0}%' AND dept_code = '{1}' {2};".format(self.today, self.dept, self.asset_sql)

        yesterday_count_sql = "SELECT SUM(trans_amount) FROM `ns_order` WHERE trans_time LIKE '{0}%' " \
                              "AND dept_code = '{1}' {2};".format(self.yesterday, self.dept, self.asset_sql)
        res_today = self.execute_select(today_count_sql)[0][0]
        if res_today:
            today_count = res_today
        else:
            today_count = 0

        res_yesterday = self.execute_select(yesterday_count_sql)[0][0]
        if res_yesterday:
            yesterday_count = res_yesterday
        else:
            yesterday_count = 0

        return [str(today_count), str(yesterday_count)]




















def dept_count_main(dept, asset=None):
    result_dict = {}
    dc = DeptCount(dept, asset)
    today_count, yesterday_count=  dc.invest_amount()

    print('本日投资总额：' + today_count)
    print('昨日投资总额：' + yesterday_count)










if __name__ == '__main__':
    dept_count_main('SHNMCW0006', None)
    # dept_count_main('SHNMCW0006', 2)