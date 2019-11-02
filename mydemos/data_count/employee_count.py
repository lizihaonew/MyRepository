#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : Li ZiHao
# @Time     : 2019/11/2 0:30
# @File     : employee_count.py

import datetime
import time
from opt_mysql import Optsql


class EmployeeCount(Optsql):
    def __init__(self, mobile):
        self.mobile = mobile
        self.cur = self.conn_mysql()
        date_today = datetime.date.today()
        self.today = str(date_today)
        self.yesterday = str(date_today - datetime.timedelta(days=1))
        self.current_month = time.strftime('%Y-%m')
        self.fa_id = str(self.execute_select(self.cur, "SELECT id FROM `wbs_employee` WHERE mobile='{0}' AND dismissionDate IS NULL;".format(self.mobile))[0][0])

    def exchange_None(self,para):
        if para:
            return para
        else:
            return 0

    def employee_information(self):
        ''' 员工姓名、手机号、部门 '''
        employee_mobile = self.mobile
        employee_information_sql = "SELECT e.name,d.name FROM `wbs_employee` e, `wbs_department` d WHERE " \
                                   "e.mobile = '{0}' AND e.dismissionDate IS NULL AND e.`deptCode`=d.code;".format(self.mobile)
        employee_name, employee_dept = self.execute_select(self.cur, employee_information_sql)[0]
        return [employee_name, employee_mobile, employee_dept]

    def invest_amount(self):
        '''本日投资总额、昨日投资总额'''
        today_amount_sql = "SELECT SUM(trans_amount) FROM `ns_order` WHERE fa_id='{0}' AND trans_time LIKE '{1}%';".format(self.fa_id, self.today)

        yesterday_amount_sql = "SELECT SUM(trans_amount) FROM `ns_order` WHERE fa_id='{0}' AND trans_time LIKE '{1}%';".format(self.fa_id, self.yesterday)
        today_amount = self.exchange_None(self.execute_select(self.cur, today_amount_sql)[0][0])
        yesterday_amount = self.exchange_None(self.execute_select(self.cur, yesterday_amount_sql)[0][0])
        return [str(today_amount), str(yesterday_amount)]

    def yesterday_performance_amount(self):
        '''昨日投资业绩'''
        yesterday_amount_sql = "SELECT sum(performance_amount) FROM ns_sop_order_snapshot WHERE advisor_id={0} AND " \
                               "trans_time LIKE '{1}%';".format(self.fa_id,self.yesterday)
        yesterday_performance_amount = self.exchange_None(self.execute_select(self.cur,yesterday_amount_sql)[0][0])

        return str(yesterday_performance_amount)

    def invest_count(self):
        '''本日投资笔数、昨日投资笔数'''
        today_count_sql = "SELECT COUNT(1) FROM ns_order WHERE trans_time LIKE '{0}%' AND fa_id={1};".format(self.today, self.fa_id)
        yesterday_count_sql = "SELECT COUNT(1) FROM ns_order WHERE trans_time LIKE '{0}%' AND fa_id={1};".format(self.yesterday, self.fa_id)
        today_count = self.exchange_None(self.execute_select(self.cur,today_count_sql)[0][0])
        yesterday_count = self.exchange_None(self.execute_select(self.cur,yesterday_count_sql)[0][0])
        return [str(today_count), str(yesterday_count)]

    def funds_amount(self):
        ''' 客户待收总额、客户沉淀总额 '''
        asset_funds_to_be_collected_sql = "SELECT SUM(a.funds_to_be_collected) FROM wbs_asset_cus_account a, " \
                                          "wbs_customer c WHERE c.faId={0} AND a.cus_id=c.id;".format(self.fa_id)
        asset_precipitated_capital_sql = "SELECT SUM(a.precipitated_capital) FROM wbs_asset_cus_account a, " \
                                          "wbs_customer c WHERE c.faId={0} AND a.cus_id=c.id;".format(self.fa_id)
        stock_funds_to_be_collected_sql = "SELECT SUM(funds_to_be_collected) FROM wbs_stock_customer WHERE fa_id={0} " \
                                          "AND deleted=0;".format(self.fa_id)
        stock_precipitated_capital_sql = "SELECT SUM(precipitated_capital) FROM wbs_stock_customer WHERE fa_id={0} " \
                                          "AND deleted=0;".format(self.fa_id)

        asset_funds_to_be_collected = self.exchange_None(self.execute_select(self.cur,asset_funds_to_be_collected_sql)[0][0])
        asset_precipitated_capital = self.exchange_None(self.execute_select(self.cur,asset_precipitated_capital_sql)[0][0])
        stock_funds_to_be_collected = self.exchange_None(self.execute_select(self.cur,stock_funds_to_be_collected_sql)[0][0])
        stock_precipitated_capital = self.exchange_None(self.execute_select(self.cur,stock_precipitated_capital_sql)[0][0])
        funds_to_be_collected = asset_funds_to_be_collected + stock_funds_to_be_collected
        precipitated_capital = asset_precipitated_capital + stock_precipitated_capital
        return [str(funds_to_be_collected), str(precipitated_capital)]

    def openaccount_amount(self):
        ''' 本日累计开户数、昨日累计开户数 '''
        asset_openaccount_amount_today_sql = "SELECT COUNT(1) FROM wbs_asset_cus_account a, wbs_customer c WHERE " \
                                             "c.faId={0} AND a.cus_id=c.id AND platform_account_opening_time LIKE " \
                                             "'{1}%';".format(self.fa_id, self.today)
        asset_openaccount_amount_yesterday_sql = "SELECT COUNT(1) FROM wbs_asset_cus_account a, wbs_customer c WHERE " \
                                             "c.faId={0} AND a.cus_id=c.id AND platform_account_opening_time LIKE " \
                                             "'{1}%';".format(self.fa_id, self.yesterday)
        stock_openaccount_amount_today_sql = "SELECT COUNT(1) FROM wbs_stock_customer WHERE fa_id={0} AND deleted=0 " \
                                             "AND platform_account_opening_time LIKE '{1}%';".format(self.fa_id, self.today)
        stock_openaccount_amount_yesterday_sql = "SELECT COUNT(1) FROM wbs_stock_customer WHERE fa_id={0} AND deleted=0 " \
                                             "AND platform_account_opening_time LIKE '{1}%';".format(self.fa_id, self.yesterday)

        asset_openaccount_amount_today = self.exchange_None(self.execute_select(self.cur,asset_openaccount_amount_today_sql)[0][0])
        asset_openaccount_amount_yesterday = self.exchange_None(self.execute_select(self.cur,asset_openaccount_amount_yesterday_sql)[0][0])
        stock_openaccount_amount_today = self.exchange_None(self.execute_select(self.cur,stock_openaccount_amount_today_sql)[0][0])
        stock_openaccount_amount_yesterday = self.exchange_None(self.execute_select(self.cur,stock_openaccount_amount_yesterday_sql)[0][0])
        openaccount_amount_today = asset_openaccount_amount_today + stock_openaccount_amount_today
        openaccount_amount_yesterday = asset_openaccount_amount_yesterday + stock_openaccount_amount_yesterday

        return [str(openaccount_amount_today), str(openaccount_amount_yesterday)]

    def first_invest_match_count(self):
        ''' 本月首投达标客户数 '''
        ''' fimc = first_invest_match_count '''
        month_HY_fimc_sql = "SELECT COUNT(1) FROM (SELECT DISTINCT cus_id FROM `ns_order` WHERE fa_id={0} AND " \
                            "Convert(trans_time,CHAR(20)) LIKE '{1}%' AND first_invest=1 AND trans_amount>=3000 AND " \
                            "asset_id=1) a;".format(self.fa_id, self.current_month)
        month_HJS_fimc_sql = "SELECT COUNT(1) FROM (SELECT DISTINCT cus_id FROM `ns_order` WHERE fa_id={0} AND " \
                            "Convert(trans_time,CHAR(20)) LIKE '{1}%' AND first_invest=1 AND trans_amount>=20000 AND " \
                            "asset_id=2) a;".format(self.fa_id, self.current_month)
        month_HP_fimc_sql = "SELECT COUNT(1) FROM (SELECT DISTINCT cus_id FROM `ns_order` WHERE fa_id={0} AND " \
                            "Convert(trans_time,CHAR(20)) LIKE '{1}%' AND first_invest=1 AND trans_amount>=20000 AND " \
                            "asset_id=3) a;".format(self.fa_id, self.current_month)

        month_HY_fimc = self.exchange_None(self.execute_select(self.cur, month_HY_fimc_sql)[0][0])
        month_HJS_fimc = self.exchange_None(self.execute_select(self.cur, month_HJS_fimc_sql)[0][0])
        month_HP_fimc = self.exchange_None(self.execute_select(self.cur, month_HP_fimc_sql)[0][0])
        month_fimc = month_HY_fimc + month_HJS_fimc + month_HP_fimc

        return str(month_fimc)


def employee_count_main(mobile):
    ec = EmployeeCount(mobile)
    employee_name, employee_mobile, employee_dept = ec.employee_information()
    today_amount, yesterday_amount = ec.invest_amount()
    yesterday_performance_amount = ec.yesterday_performance_amount()
    today_count, yesterday_count = ec.invest_count()
    funds_to_be_collected, precipitated_capital = ec.funds_amount()
    openaccount_amount_today, openaccount_amount_yesterday = ec.openaccount_amount()
    month_fimc = ec.first_invest_match_count()


    comment = '销售快报 - 按照员工统计，统计结果如下：' + '( 员工：%s, 手机号：%s，部门：%s )' % (employee_name, employee_mobile, employee_dept) + '\n' \
        '本日投资总额：' + today_amount + '\n' \
        '昨日投资总额：' + yesterday_amount + '\n' \
        '昨日投资业绩：' + yesterday_performance_amount + '\n' \
        '本日投资笔数：' + today_count + '\n' \
        '昨日投资笔数：' + yesterday_count + '\n' \
        '客户待收总额：' + funds_to_be_collected + '\n' \
        '客户沉淀总额：' + precipitated_capital + '\n' \
        '本日累计开户数：' + openaccount_amount_today + '\n' \
        '昨日累计开户数：' + openaccount_amount_yesterday + '\n' \
        '本月首投达标客户数：' + month_fimc

    print(comment)


if __name__ == '__main__':
    employee_count_main('13666666661')