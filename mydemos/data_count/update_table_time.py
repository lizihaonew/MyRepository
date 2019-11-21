#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : Li ZiHao
# @Time     : 2019/11/4 20:46
# @File     : update_table_time.py

import datetime
import time
from opt_mysql import Optsql


class UpdateTableTime(Optsql):
    def __init__(self, date):
        self.cur = self.conn_mysql()
        if date == '0':
            date_today = datetime.date.today()
            # self.yesterday = str(date_today - datetime.timedelta(days=1))
            # self.two_days_ago = str(date_today - datetime.timedelta(days=2))
        else:
            year, month, day = date.split('-')
            date_today = datetime.date(int(year), int(month), int(day)) + datetime.timedelta(days=1)
        self.today = datetime.date.today()
        self.yesterday = str(date_today - datetime.timedelta(days=1))
        self.two_days_ago = str(date_today - datetime.timedelta(days=2))
        self.current_month = time.strftime('%Y-%m')

    def update_table_time(self):
        ns_order_today_sql = "UPDATE ns_order SET trans_time='{0} 00:00:00' WHERE trans_time LIKE " \
                             "'{1}%';".format(self.today, self.yesterday)
        # print(ns_order_today_sql)
        ns_order_yesterday_sql = "UPDATE ns_order SET trans_time='{0} 00:00:00' WHERE trans_time LIKE " \
                                 "'{1}%';".format(self.yesterday, self.two_days_ago)
        ns_sop_order_snapshot_today_sql = "UPDATE ns_sop_order_snapshot SET trans_time='{0} 00:00:00' WHERE trans_time" \
                                          " LIKE '{1}%';".format(self.today, self.yesterday)
        ns_sop_order_snapshot_yesterday_sql = "UPDATE ns_sop_order_snapshot SET trans_time='{0} 00:00:00' WHERE " \
                                              "trans_time LIKE '{1}%';".format(self.yesterday, self.two_days_ago)
        actual_exit_time_today_sql = "UPDATE wbs_received_payment SET actual_exit_time='{0} 00:00:00' WHERE " \
                                     "actual_exit_time LIKE '{1}%';".format(self.today, self.yesterday)
        actual_exit_time_yesterday_sql = "UPDATE wbs_received_payment SET actual_exit_time='{0} 00:00:00' WHERE " \
                                         "actual_exit_time LIKE '{1}%';".format(self.yesterday, self.two_days_ago)
        expected_exit_time_today_sql = "UPDATE wbs_received_payment SET expected_exit_time='{0} 00:00:00' WHERE " \
                                       "expected_exit_time LIKE '{1}%';".format(self.today, self.yesterday)
        expected_exit_time_yesterday_sql = "UPDATE wbs_received_payment SET expected_exit_time='{0} 00:00:00' WHERE " \
                                           "expected_exit_time LIKE '{1}%';".format(self.yesterday, self.two_days_ago)
        cashout_time_today_sql = "UPDATE ns_cashout_record SET cashout_time='{0} 00:00:00' WHERE cashout_time " \
                                 "LIKE '{1}%';".format(self.today, self.yesterday)
        cashout_time_yesterday_sql = "UPDATE ns_cashout_record SET cashout_time='{0} 00:00:00' WHERE cashout_time " \
                                     "LIKE '{1}%';".format(self.yesterday, self.two_days_ago)
        recharge_time_today_sql = "UPDATE ns_recharge_record SET recharge_time='{0} 00:00:00' WHERE recharge_time " \
                                  "LIKE '{1}%';".format(self.today, self.yesterday)
        recharge_time_yesterday_sql = "UPDATE ns_recharge_record SET recharge_time='{0} 00:00:00' WHERE recharge_time" \
                                      " LIKE '{1}%';".format(self.yesterday, self.two_days_ago)
        account_opening_time_today_sql = "UPDATE wbs_asset_cus_account SET platform_account_opening_time=" \
                                         "'{0} 00:00:00' WHERE platform_account_opening_time LIKE " \
                                         "'{1}%';".format(self.today, self.yesterday)
        account_opening_time_yesterday_sql = "UPDATE wbs_asset_cus_account SET platform_account_opening_time=" \
                                             "'{0} 00:00:00' WHERE platform_account_opening_time LIKE " \
                                             "'{1}%';".format(self.yesterday, self.two_days_ago)
        stock_customer_today_sql = "UPDATE wbs_stock_customer SET platform_account_opening_time='{0} 00:00:00' " \
                                   "WHERE platform_account_opening_time LIKE '{1}%';".format(self.today, self.yesterday)
        stock_customer_yesterday_sql = "UPDATE wbs_stock_customer SET platform_account_opening_time='{0} 00:00:00'" \
                                       " WHERE platform_account_opening_time LIKE '{1}%'" \
                                       ";".format(self.yesterday, self.two_days_ago)
        stock_create_time_today_sql = "UPDATE wbs_stock_customer SET create_time='{0} 00:00:00' " \
                                   "WHERE create_time LIKE '{1}%';".format(self.today, self.yesterday)

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
        res = self.update_table(account_opening_time_today_sql)
        print('%s update successful!!!' % 'account_opening_time_today_sql' + '===' + str(res))
        res = self.update_table(account_opening_time_yesterday_sql)
        print('%s update successful!!!' % 'account_opening_time_yesterday_sql' + '===' + str(res))
        res = self.update_table(stock_customer_today_sql)
        print('%s update successful!!!' % 'stock_customer_today_sql' + '===' + str(res))
        res = self.update_table(stock_customer_yesterday_sql)
        print('%s update successful!!!' % 'stock_customer_yesterday_sql' + '===' + str(res))
        res = self.update_table(stock_create_time_today_sql)
        print('%s update successful!!!' % 'stock_create_time_today_sql' + '===' + str(res))


if __name__ == '__main__':
    utt = UpdateTableTime('0')
    # utt = UpdateTableTime('2019-11-15')
    utt.update_table_time()



