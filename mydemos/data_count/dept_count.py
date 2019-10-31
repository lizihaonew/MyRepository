#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : Li ZiHao
# @Time     : 2019/10/30 21:43
# @File     : dept_count.py

import datetime
import time
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
        self.current_month = time.strftime('%Y-%m')

    def exchange_None(self,para):
        if para:
            return para
        else:
            return 0

    def invest_amount(self):
        '''本日投资总额、昨日投资总额'''
        # if self.asset:
        #     asset_sql = 'and asset_id = %s' % self.asset
        # else:
        #     asset_sql = ''
        today_amount_sql = "SELECT SUM(trans_amount) FROM `ns_order` WHERE trans_time " \
                          "LIKE '{0}%' AND dept_code LIKE '{1}%' {2};".format(self.today, self.dept, self.asset_sql)

        yesterday_amount_sql = "SELECT SUM(trans_amount) FROM `ns_order` WHERE trans_time LIKE '{0}%' " \
                              "AND dept_code LIKE '{1}%' {2};".format(self.yesterday, self.dept, self.asset_sql)
        res_today = self.execute_select(today_amount_sql)[0][0]
        today_amount = self.exchange_None(res_today)

        res_yesterday = self.execute_select(yesterday_amount_sql)[0][0]
        yesterday_amount = self.exchange_None(res_yesterday)

        return [str(today_amount), str(yesterday_amount)]

    def yesterday_performance_amount(self):
        '''昨日投资业绩'''
        yesterday_amount_sql = "SELECT SUM(performance_amount) FROM `ns_sop_order_snapshot` WHERE " \
                              "trans_time LIKE '{0}%' AND department_no LIKE '{1}%' {2}" \
                              ";".format(self.yesterday, self.dept, self.asset_sql)
        res_yesterday = self.execute_select(yesterday_amount_sql)[0][0]
        yesterday_amount = self.exchange_None(res_yesterday)

        return str(yesterday_amount)

    def invest_count(self):
        '''本日投资笔数、昨日投资笔数'''
        today_count_sql = "SELECT COUNT(1) FROM `ns_order` WHERE trans_time " \
                          "LIKE '{0}%' AND dept_code LIKE '{1}%' {2};".format(self.today, self.dept, self.asset_sql)
        yesterday_count_sql = "SELECT COUNT(1) FROM `ns_order` WHERE trans_time LIKE '{0}%' " \
                              "AND dept_code LIKE '{1}%' {2};".format(self.yesterday, self.dept, self.asset_sql)
        res_today = self.execute_select(today_count_sql)[0][0]
        today_count = self.exchange_None(res_today)
        res_yesterday = self.execute_select(yesterday_count_sql)[0][0]
        yesterday_count = self.exchange_None(res_yesterday)
        return [str(today_count), str(yesterday_count)]

    def repayment_amount(self):
        '''本月累计已还款、本月累计待还款'''
        repayed_amount_sql = "SELECT SUM(actual_exit_amount) FROM `wbs_received_payment` WHERE Convert(actual_exit_time,CHAR(20)) " \
                            "LIKE '{0}%' AND STATUS = 1 AND dept_code LIKE '{1}%' AND order_no " \
                            "IN (SELECT order_no FROM `ns_order` WHERE 1=1 " \
                            "{2});".format(self.current_month, self.dept, self.asset_sql)
        expected_amount_sql = "SELECT SUM(expected_exit_amount) FROM `wbs_received_payment` WHERE Convert(expected_exit_time,CHAR(20)) " \
                            "LIKE '{0}%' AND STATUS = 2 AND dept_code LIKE '{1}%' AND order_no " \
                            "IN (SELECT order_no FROM `ns_order` WHERE 1=1 " \
                            "{2});".format(self.current_month, self.dept, self.asset_sql)

        res_repayed = self.execute_select(repayed_amount_sql)[0][0]
        repayed_amount = self.exchange_None(res_repayed)
        res_expected = self.execute_select(expected_amount_sql)[0][0]
        expected_amount = self.exchange_None(res_expected)
        return [str(repayed_amount), str(expected_amount)]

    def cashout_amount(self):
        ''' 本月累计提现、本日累计提现、昨日累计提现 '''
        cashout_current_month_sql = "SELECT SUM(cashout_amount) FROM `ns_cashout_record` WHERE 1=1 AND Convert(cashout_time,CHAR(20)) " \
                                    "LIKE '{0}%' AND dept_code LIKE " \
                                    "'{1}%' {2}".format(self.current_month, self.dept, self.asset_sql)

        cashout_today_sql = "SELECT SUM(cashout_amount) FROM `ns_cashout_record` WHERE 1=1 AND Convert(cashout_time,CHAR(20)) " \
                                    "LIKE '{0}%' AND dept_code LIKE " \
                                    "'{1}%' {2}".format(self.today, self.dept, self.asset_sql)
        cashout_yesterday_sql = "SELECT SUM(cashout_amount) FROM `ns_cashout_record` WHERE 1=1 AND Convert(cashout_time,CHAR(20)) " \
                                    "LIKE '{0}%' AND dept_code LIKE " \
                                    "'{1}%' {2}".format(self.yesterday, self.dept, self.asset_sql)
        res_current_month = self.execute_select(cashout_current_month_sql)[0][0]
        cashout_current_month = self.exchange_None(res_current_month)

        res_today = self.execute_select(cashout_today_sql)[0][0]
        cashout_today = self.exchange_None(res_today)

        res_yesterday = self.execute_select(cashout_yesterday_sql)[0][0]
        cashout_yesterday = self.exchange_None(res_yesterday)

        return [str(cashout_current_month), str(cashout_today), str(cashout_yesterday)]

# SELECT SUM(actual_exit_amount) FROM `wbs_received_payment` WHERE actual_exit_time LIKE '2019-11-01%' AND STATUS = 1 AND dept_code LIKE 'SHNMCW0001%' AND order_no IN (SELECT order_no FROM `ns_order` WHERE 1=1 );
    def exit_amount(self):
        ''' 当日实际回款总额、昨日实际回款总额 '''
        exit_amount_today = "SELECT SUM(actual_exit_amount) FROM `wbs_received_payment` WHERE Convert(actual_exit_time,CHAR(20)) " \
                            "LIKE '{0}%' AND STATUS = 1 AND dept_code LIKE '{1}%' AND order_no IN " \
                            "(SELECT order_no FROM `ns_order` WHERE 1=1 {2});".format(self.today, self.dept, self.asset_sql)
        exit_amount_yesterday = "SELECT SUM(actual_exit_amount) FROM `wbs_received_payment` WHERE Convert(actual_exit_time,CHAR(20)) " \
                            "LIKE '{0}%' AND STATUS = 1 AND dept_code LIKE '{1}%' AND order_no IN " \
                            "(SELECT order_no FROM `ns_order` WHERE 1=1 {2});".format(self.yesterday, self.dept, self.asset_sql)
        # res_today = self.execute_select(exit_amount_today)[0][0]
        repayed_amount = self.exchange_None(self.execute_select(exit_amount_today)[0][0])
        # res_yesterday = self.execute_select(exit_amount_yesterday)[0][0]
        repayed_amount = self.exchange_None(self.execute_select(exit_amount_yesterday)[0][0])














def dept_count_main(dept, asset=None):
    result_dict = {}
    dc = DeptCount(dept, asset)
    # today_amount, yesterday_amount =  dc.invest_amount()
    # yesterday_performance_amount = dc.yesterday_performance_amount()
    # today_count, yesterday_count = dc.invest_count()
    # current_month_actual_exit_amount, current_month_expected_exit_amount = dc.repayment_amount()
    cashout_current_month,cashout_today,cashout_yesterday = dc.cashout_amount()

    # print('本日投资总额：' + today_amount)
    # print('昨日投资总额：' + yesterday_amount)
    # print('昨日投资业绩：' + yesterday_performance_amount)
    # print('本日投资笔数：' + today_count)
    # print('昨日投资笔数：' + yesterday_count)
    # print('本月累计已还款：' + current_month_actual_exit_amount)
    # print('本月累计待还款：' + current_month_expected_exit_amount)
    print('本月累计提现：' + cashout_current_month)
    print('本日累计提现：' + cashout_today)
    print('昨日累计提现：' + cashout_yesterday)













if __name__ == '__main__':
    # dept_count_main('SHNMCW0001')
    dept_count_main('SHNMCW0001', 1)