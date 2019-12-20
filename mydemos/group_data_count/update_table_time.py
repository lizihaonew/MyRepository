#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : Li ZiHao
# @Time     : 2019/11/4 20:46
# @File     : update_table_time.py

import datetime
import time
from opt_group_mysql import Optsql


class UpdateTableTime(Optsql):
    def __init__(self, date, name):
        self.cur, self.conn = self.conn_mysql(name)
        if date == '0':
            date_today = datetime.date.today()
        else:
            year, month, day = date.split('-')
            date_today = datetime.date(int(year), int(month), int(day)) + datetime.timedelta(days=1)
        self.today = datetime.date.today()
        self.yesterday = datetime.date.today() - datetime.timedelta(days=1)
        self.date_yesterday = str(date_today - datetime.timedelta(days=1))
        self.two_days_ago = str(date_today - datetime.timedelta(days=2))
        self.current_month = time.strftime('%Y-%m')

    def update_table(self, sql):
        return super(UpdateTableTime, self).update_table(self.cur, self.conn, sql)

    def update_table_time(self):
        ns_order_today_sql = "UPDATE ns_order SET trans_time='{0} 00:00:00' WHERE trans_time LIKE " \
                             "'{1}%';".format(self.today, self.date_yesterday)
        ns_order_yesterday_sql = "UPDATE ns_order SET trans_time='{0} 00:00:00' WHERE trans_time LIKE " \
                                 "'{1}%';".format(self.yesterday, self.two_days_ago)
        ns_sop_order_snapshot_today_sql = "UPDATE ns_sop_order_snapshot_summary SET trans_time='{0} 00:00:00' WHERE trans_time" \
                                          " LIKE '{1}%';".format(self.today, self.date_yesterday)
        ns_sop_order_snapshot_yesterday_sql = "UPDATE ns_sop_order_snapshot_summary SET trans_time='{0} 00:00:00' WHERE " \
                                              "trans_time LIKE '{1}%';".format(self.yesterday, self.two_days_ago)
        actual_exit_time_today_sql = "UPDATE wbs_received_payment SET actual_exit_time='{0} 00:00:00' WHERE " \
                                     "actual_exit_time LIKE '{1}%';".format(self.today, self.date_yesterday)
        actual_exit_time_yesterday_sql = "UPDATE wbs_received_payment SET actual_exit_time='{0} 00:00:00' WHERE " \
                                         "actual_exit_time LIKE '{1}%';".format(self.yesterday, self.two_days_ago)
        expected_exit_time_today_sql = "UPDATE wbs_received_payment SET expected_exit_time='{0} 00:00:00' WHERE " \
                                       "expected_exit_time LIKE '{1}%';".format(self.today, self.date_yesterday)
        expected_exit_time_yesterday_sql = "UPDATE wbs_received_payment SET expected_exit_time='{0} 00:00:00' WHERE " \
                                           "expected_exit_time LIKE '{1}%';".format(self.yesterday, self.two_days_ago)
        cashout_time_today_sql = "UPDATE ns_cashout_record SET cashout_time='{0} 00:00:00' WHERE cashout_time " \
                                 "LIKE '{1}%';".format(self.today, self.date_yesterday)
        cashout_time_yesterday_sql = "UPDATE ns_cashout_record SET cashout_time='{0} 00:00:00' WHERE cashout_time " \
                                     "LIKE '{1}%';".format(self.yesterday, self.two_days_ago)
        recharge_time_today_sql = "UPDATE ns_recharge_record SET recharge_time='{0} 00:00:00' WHERE recharge_time " \
                                  "LIKE '{1}%';".format(self.today, self.date_yesterday)
        recharge_time_yesterday_sql = "UPDATE ns_recharge_record SET recharge_time='{0} 00:00:00' WHERE recharge_time" \
                                      " LIKE '{1}%';".format(self.yesterday, self.two_days_ago)
        stock_customer_today_sql = "UPDATE wbs_stock_customer SET platform_account_opening_time='{0} 00:00:00' " \
                                   "WHERE platform_account_opening_time LIKE '{1}%';".format(self.today, self.date_yesterday)
        stock_customer_yesterday_sql = "UPDATE wbs_stock_customer SET platform_account_opening_time='{0} 00:00:00'" \
                                       " WHERE platform_account_opening_time LIKE '{1}%'" \
                                       ";".format(self.yesterday, self.two_days_ago)
        stock_create_time_today_sql = "UPDATE wbs_stock_customer SET create_time='{0} 00:00:00' " \
                                   "WHERE create_time LIKE '{1}%';".format(self.today, self.date_yesterday)

        res = self.update_table(ns_order_today_sql)
        print('%s update successful!!!' % 'ns_order_today_sql' + '===' + str(res))
        res = self.update_table(ns_order_yesterday_sql)
        print('%s update successful!!!' % 'ns_order_yesterday_sql' + '===' + str(res))
        res = self.update_table(ns_sop_order_snapshot_today_sql)
        print('%s update successful!!!' % 'ns_sop_order_snapshot_today_sql' + '===' + str(res))
        res = self.update_table(ns_sop_order_snapshot_yesterday_sql)
        print('%s update successful!!!' % 'ns_sop_order_snapshot_yesterday_sql' + '===' + str(res))
        res = self.update_table(actual_exit_time_today_sql)
        print('%s update successful!!!' % 'actual_exit_time_today_sql' + '===' + str(res))
        res = self.update_table(actual_exit_time_yesterday_sql)
        print('%s update successful!!!' % 'actual_exit_time_yesterday_sql' + '===' + str(res))
        res = self.update_table(expected_exit_time_today_sql)
        print('%s update successful!!!' % 'expected_exit_time_today_sql' + '===' + str(res))
        res = self.update_table(expected_exit_time_yesterday_sql)
        print('%s update successful!!!' % 'expected_exit_time_yesterday_sql' + '===' + str(res))
        res = self.update_table(cashout_time_today_sql)
        print('%s update successful!!!' % 'cashout_time_today_sql' + '===' + str(res))
        res = self.update_table(cashout_time_yesterday_sql)
        print('%s update successful!!!' % 'cashout_time_yesterday_sql' + '===' + str(res))
        res = self.update_table(recharge_time_today_sql)
        print('%s update successful!!!' % 'recharge_time_today_sql' + '===' + str(res))
        res = self.update_table(recharge_time_yesterday_sql)
        print('%s update successful!!!' % 'recharge_time_yesterday_sql' + '===' + str(res))
        res = self.update_table(stock_customer_today_sql)
        print('%s update successful!!!' % 'stock_customer_today_sql' + '===' + str(res))
        res = self.update_table(stock_customer_yesterday_sql)
        print('%s update successful!!!' % 'stock_customer_yesterday_sql' + '===' + str(res))
        res = self.update_table(stock_create_time_today_sql)
        print('%s update successful!!!' % 'stock_create_time_today_sql' + '===' + str(res))

        self.object_close(self.cur, self.conn)


if __name__ == '__main__':
    print("请输入企业：nami、datang")
    company_name = input("请输入企业：")
    print("请输入修改的时间，当日时间输入0，其他输入格式如：2019-11-15")
    to_update_time = input("请输入: ")
    utt = UpdateTableTime(to_update_time, company_name)
    # utt = UpdateTableTime('2019-11-15')
    utt.update_table_time()



