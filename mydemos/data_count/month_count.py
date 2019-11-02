#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : Li ZiHao
# @Time     : 2019/11/2 0:32
# @File     : month_count.py

import datetime
import time
from opt_mysql import Optsql


class MonthCount(Optsql):
    def __init__(self, dept, asset=None):
        self.dept = dept
        self.asset = asset
        if asset:
            self.asset_sql = 'and asset_id = %s' % asset
        else:
            self.asset_sql = ''
        self.cur = self.conn_mysql()
        date_today = datetime.date.today()
        self.today = str(date_today)
        self.yesterday = str(date_today - datetime.timedelta(days=1))
        self.current_month = time.strftime('%Y-%m')

    def func(self):
        pass


def month_count_main():
    print('month_count_main')


if __name__ == '__main__':
    month_count_main()