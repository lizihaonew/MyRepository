#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : Li ZiHao
# @Time     : 2019/10/30 21:43
# @File     : dept_count.py

import datetime
import time
from opt_mysql import Optsql


class DeptCount(Optsql):
    def __init__(self, dept, asset):
        self.dept = dept
        self.asset = asset
        if asset == 0:
            self.asset_sql = '' % asset
        else:
            self.asset_sql = 'and asset_id = %s' % asset
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
        today_amount_sql = "SELECT SUM(trans_amount) FROM `ns_order` WHERE trans_time " \
                          "LIKE '{0}%' AND dept_code LIKE '{1}%' {2};".format(self.today, self.dept, self.asset_sql)

        yesterday_amount_sql = "SELECT SUM(trans_amount) FROM `ns_order` WHERE trans_time LIKE '{0}%' " \
                              "AND dept_code LIKE '{1}%' {2};".format(self.yesterday, self.dept, self.asset_sql)
        today_amount = self.exchange_None(self.execute_select(self.cur,today_amount_sql)[0][0])

        yesterday_amount = self.exchange_None(self.execute_select(self.cur,yesterday_amount_sql)[0][0])

        return [str(today_amount), str(yesterday_amount)]

    def yesterday_performance_amount(self):
        '''昨日投资业绩'''
        yesterday_amount_sql = "SELECT SUM(performance_amount) FROM `ns_sop_order_snapshot` WHERE " \
                              "trans_time LIKE '{0}%' AND department_no LIKE '{1}%' {2}" \
                              ";".format(self.yesterday, self.dept, self.asset_sql)
        yesterday_amount = self.exchange_None(self.execute_select(self.cur,yesterday_amount_sql)[0][0])

        return str(yesterday_amount)

    def invest_count(self):
        '''本日投资笔数、昨日投资笔数'''
        today_count_sql = "SELECT COUNT(1) FROM `ns_order` WHERE trans_time " \
                          "LIKE '{0}%' AND dept_code LIKE '{1}%' {2};".format(self.today, self.dept, self.asset_sql)
        yesterday_count_sql = "SELECT COUNT(1) FROM `ns_order` WHERE trans_time LIKE '{0}%' " \
                              "AND dept_code LIKE '{1}%' {2};".format(self.yesterday, self.dept, self.asset_sql)
        today_count = self.exchange_None(self.execute_select(self.cur,today_count_sql)[0][0])
        yesterday_count = self.exchange_None(self.execute_select(self.cur,yesterday_count_sql)[0][0])
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

        repayed_amount = self.exchange_None(self.execute_select(self.cur,repayed_amount_sql)[0][0])
        expected_amount = self.exchange_None(self.execute_select(self.cur,expected_amount_sql)[0][0])
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
        cashout_current_month = self.exchange_None(self.execute_select(self.cur,cashout_current_month_sql)[0][0])

        cashout_today = self.exchange_None(self.execute_select(self.cur,cashout_today_sql)[0][0])

        cashout_yesterday = self.exchange_None(self.execute_select(self.cur,cashout_yesterday_sql)[0][0])

        return [str(cashout_current_month), str(cashout_today), str(cashout_yesterday)]

    def exit_amount(self):
        ''' 当日实际回款总额、昨日实际回款总额 '''
        exit_amount_today_sql = "SELECT SUM(actual_exit_amount) FROM `wbs_received_payment` WHERE Convert(actual_exit_time,CHAR(20)) " \
                            "LIKE '{0}%' AND STATUS = 1 AND dept_code LIKE '{1}%' AND order_no IN " \
                            "(SELECT order_no FROM `ns_order` WHERE 1=1 {2});".format(self.today, self.dept, self.asset_sql)
        exit_amount_yesterday_sql = "SELECT SUM(actual_exit_amount) FROM `wbs_received_payment` WHERE Convert(actual_exit_time,CHAR(20)) " \
                            "LIKE '{0}%' AND STATUS = 1 AND dept_code LIKE '{1}%' AND order_no IN " \
                            "(SELECT order_no FROM `ns_order` WHERE 1=1 {2});".format(self.yesterday, self.dept, self.asset_sql)
        exit_amount_today = self.exchange_None(self.execute_select(self.cur,exit_amount_today_sql)[0][0])
        exit_amount_yesterday = self.exchange_None(self.execute_select(self.cur,exit_amount_yesterday_sql)[0][0])
        return [str(exit_amount_today), str(exit_amount_yesterday)]

    def recharge_amount(self):
        ''' 本月累计充值、本日累计充值、昨日累计充值 '''
        recharge_current_month_sql = "SELECT SUM(recharge_amount) FROM `ns_recharge_record` WHERE 1=1 AND Convert(recharge_time,CHAR(20)) " \
                                    "LIKE '{0}%' AND dept_code LIKE " \
                                    "'{1}%' {2}".format(self.current_month, self.dept, self.asset_sql)

        recharge_today_sql = "SELECT SUM(recharge_amount) FROM `ns_recharge_record` WHERE 1=1 AND Convert(recharge_time,CHAR(20)) " \
                            "LIKE '{0}%' AND dept_code LIKE " \
                            "'{1}%' {2}".format(self.today, self.dept, self.asset_sql)
        recharge_yesterday_sql = "SELECT SUM(recharge_amount) FROM `ns_recharge_record` WHERE 1=1 AND Convert(recharge_time,CHAR(20)) " \
                                "LIKE '{0}%' AND dept_code LIKE " \
                                "'{1}%' {2}".format(self.yesterday, self.dept, self.asset_sql)
        recharge_current_month = self.exchange_None(self.execute_select(self.cur,recharge_current_month_sql)[0][0])
        recharge_today = self.exchange_None(self.execute_select(self.cur,recharge_today_sql)[0][0])
        recharge_yesterday = self.exchange_None(self.execute_select(self.cur,recharge_yesterday_sql)[0][0])
        return [str(recharge_current_month), str(recharge_today), str(recharge_yesterday)]

    def funds_amount(self):
        ''' 客户待收总额、客户沉淀总额 '''
        if self.asset == 0:
            self.asset_sql = ''
        else:
            self.asset_sql = 'and asset = %s' % self.asset

        asset_funds_to_be_collected_sql = "SELECT SUM(funds_to_be_collected) FROM `wbs_asset_cus_account` WHERE 1=1 " \
                                          "AND cus_id IN (SELECT id FROM `wbs_customer` WHERE deptCode LIKE " \
                                          "'{0}%') {1};".format(self.dept, self.asset_sql)
        asset_precipitated_capital_sql = "SELECT SUM(precipitated_capital) FROM `wbs_asset_cus_account` WHERE 1=1 " \
                                          "AND cus_id IN (SELECT id FROM `wbs_customer` WHERE deptCode LIKE " \
                                          "'{0}%') {1};".format(self.dept, self.asset_sql)
        stock_funds_to_be_collected_sql = "SELECT SUM(funds_to_be_collected) FROM `wbs_stock_customer` WHERE 1=1 " \
                                         "AND dept_code LIKE '{0}%' AND deleted=0 {1};".format(self.dept, self.asset_sql)
        stock_precipitated_capital_sql = "SELECT SUM(precipitated_capital) FROM `wbs_stock_customer` WHERE 1=1 " \
                                         "AND dept_code LIKE '{0}%' AND deleted=0 {1};".format(self.dept, self.asset_sql)

        asset_funds_to_be_collected = self.exchange_None(self.execute_select(self.cur,asset_funds_to_be_collected_sql)[0][0])
        asset_precipitated_capital = self.exchange_None(self.execute_select(self.cur,asset_precipitated_capital_sql)[0][0])
        stock_funds_to_be_collected = self.exchange_None(self.execute_select(self.cur,stock_funds_to_be_collected_sql)[0][0])
        stock_precipitated_capital = self.exchange_None(self.execute_select(self.cur,stock_precipitated_capital_sql)[0][0])
        funds_to_be_collected = asset_funds_to_be_collected + stock_funds_to_be_collected
        precipitated_capital = asset_precipitated_capital + stock_precipitated_capital
        return [str(funds_to_be_collected), str(precipitated_capital)]

    def openaccount_amount(self):
        ''' 本日累计开户数、昨日累计开户数 '''
        if self.asset == 0:
            self.asset_sql = ''
        else:
            self.asset_sql = 'and asset = %s' % self.asset
        asset_openaccount_amount_today_sql = "SELECT COUNT(1) FROM `wbs_asset_cus_account` WHERE 1=1 AND cus_id " \
                                             "IN (SELECT id FROM `wbs_customer` WHERE deptCode LIKE '{1}%') " \
                                             "AND platform_account_opening_time LIKE '{0}%' " \
                                             "{2};".format(self.today, self.dept, self.asset_sql)
        asset_openaccount_amount_yesterday_sql = "SELECT COUNT(1) FROM `wbs_asset_cus_account` WHERE 1=1 AND cus_id " \
                                             "IN (SELECT id FROM `wbs_customer` WHERE deptCode LIKE '{1}%') " \
                                             "AND platform_account_opening_time LIKE '{0}%' " \
                                             "{2};".format(self.yesterday, self.dept, self.asset_sql)
        stock_openaccount_amount_today_sql = "SELECT COUNT(1) FROM `wbs_stock_customer` WHERE 1=1 AND dept_code " \
                                             "LIKE '{1}%' AND platform_account_opening_time LIKE '{0}%' " \
                                             "AND deleted=1 {2};".format(self.today, self.dept, self.asset_sql)
        stock_openaccount_amount_yesterday_sql = "SELECT COUNT(1) FROM `wbs_stock_customer` WHERE 1=1 AND dept_code " \
                                             "LIKE '{1}%' AND platform_account_opening_time LIKE '{0}%' " \
                                             "AND deleted=1 {2};".format(self.yesterday, self.dept, self.asset_sql)

        asset_openaccount_amount_today = self.exchange_None(self.execute_select(self.cur,asset_openaccount_amount_today_sql)[0][0])
        asset_openaccount_amount_yesterday = self.exchange_None(self.execute_select(self.cur,asset_openaccount_amount_yesterday_sql)[0][0])
        stock_openaccount_amount_today = self.exchange_None(self.execute_select(self.cur,stock_openaccount_amount_today_sql)[0][0])
        stock_openaccount_amount_yesterday = self.exchange_None(self.execute_select(self.cur,stock_openaccount_amount_yesterday_sql)[0][0])

        openaccount_amount_today = asset_openaccount_amount_today + stock_openaccount_amount_today
        openaccount_amount_yesterday = asset_openaccount_amount_yesterday + stock_openaccount_amount_yesterday

        return [str(openaccount_amount_today), str(openaccount_amount_yesterday)]

    def first_invest_match_count(self):
        ''' 本月累计首投达标客户数、本日累计首投达标客户数 '''
        ''' fimc = first_invest_match_count '''
        month_HY_fimc_sql = "SELECT COUNT(1) FROM (SELECT DISTINCT cus_id FROM `ns_order` WHERE Convert(trans_time,CHAR(20)) LIKE '{0}%'" \
                        " AND first_invest=1 AND dept_code LIKE '{1}%' AND asset_id=1 AND trans_amount>=3000) " \
                        "s;".format(self.current_month, self.dept)
        month_HJS_fimc_sql = "SELECT COUNT(1) FROM (SELECT DISTINCT cus_id FROM `ns_order` WHERE Convert(trans_time,CHAR(20)) LIKE '{0}%'" \
                        " AND first_invest=1 AND dept_code LIKE '{1}%' AND asset_id=2 AND trans_amount>=20000) " \
                        "s;".format(self.current_month, self.dept)
        month_HP_fimc_sql = "SELECT COUNT(1) FROM (SELECT DISTINCT cus_id FROM `ns_order` WHERE Convert(trans_time,CHAR(20)) LIKE '{0}%'" \
                        " AND first_invest=1 AND dept_code LIKE '{1}%' AND asset_id=3 AND trans_amount>=20000) " \
                        "s;".format(self.current_month, self.dept)

        today_HY_fimc_sql = "SELECT COUNT(1) FROM (SELECT DISTINCT cus_id FROM `ns_order` WHERE Convert(trans_time,CHAR(20)) LIKE '{0}%'" \
                        " AND first_invest=1 AND dept_code LIKE '{1}%' AND asset_id=1 AND trans_amount>=3000) " \
                        "s;".format(self.today, self.dept)
        today_HJS_fimc_sql = "SELECT COUNT(1) FROM (SELECT DISTINCT cus_id FROM `ns_order` WHERE Convert(trans_time,CHAR(20)) LIKE '{0}%'" \
                        " AND first_invest=1 AND dept_code LIKE '{1}%' AND asset_id=2 AND trans_amount>=20000) " \
                        "s;".format(self.today, self.dept)
        today_HP_fimc_sql = "SELECT COUNT(1) FROM (SELECT DISTINCT cus_id FROM `ns_order` WHERE Convert(trans_time,CHAR(20)) LIKE '{0}%'" \
                        " AND first_invest=1 AND dept_code LIKE '{1}%' AND asset_id=3 AND trans_amount>=20000) " \
                        "s;".format(self.today, self.dept)

        month_HY_fimc = self.exchange_None(self.execute_select(self.cur, month_HY_fimc_sql)[0][0])
        month_HJS_fimc = self.exchange_None(self.execute_select(self.cur, month_HJS_fimc_sql)[0][0])
        month_HP_fimc = self.exchange_None(self.execute_select(self.cur, month_HP_fimc_sql)[0][0])
        today_HY_fimc = self.exchange_None(self.execute_select(self.cur, today_HY_fimc_sql)[0][0])
        today_HJS_fimc = self.exchange_None(self.execute_select(self.cur, today_HJS_fimc_sql)[0][0])
        today_HP_fimc = self.exchange_None(self.execute_select(self.cur, today_HP_fimc_sql)[0][0])

        if self.asset == 1:
            month_fimc = month_HY_fimc
            today_fimc = today_HY_fimc
        elif self.asset == 2:
            month_fimc = month_HJS_fimc
            today_fimc = today_HJS_fimc
        elif self.asset == 3:
            month_fimc = month_HP_fimc
            today_fimc = today_HP_fimc
        else:
            month_fimc = month_HY_fimc + month_HJS_fimc + month_HP_fimc
            today_fimc = today_HY_fimc + today_HJS_fimc + today_HP_fimc

        return [str(month_fimc), str(today_fimc)]

    def type_invest_amount(self):
        ''' 本日各产品类型投资总额 '''
        type_ids_sql = "SELECT DISTINCT product_type FROM `ns_order` WHERE trans_time LIKE '{0}%';".format(self.today)
        type_ids_today = [id[0] for id in self.execute_select(self.cur, type_ids_sql)]
        result_product_type_invest = []
        for id in type_ids_today:
            product_type_name_sql = "SELECT product_type_name FROM `ns_product_type` WHERE id=%d;" % id
            invest_amount_today_sql = "SELECT SUM(trans_amount) FROM `ns_order` WHERE product_type={0} AND trans_time LIKE" \
                                  " '{1}%' AND dept_code LIKE '{2}%' " \
                                  "{3};".format(id, self.today, self.dept, self.asset_sql)
            # print([product_type_name_sql,invest_amount_today_sql])
            product_type_name = self.execute_select(self.cur, product_type_name_sql)[0][0]
            product_type_invest_amount = self.exchange_None(self.execute_select(self.cur, invest_amount_today_sql)[0][0])
            result_product_type_invest.append((product_type_name+':%s'%str(id), '%.2f'% product_type_invest_amount))
        return str(result_product_type_invest)

    def deadline_num_invest_amount(self):
        ''' 本日各期限产品投资总额 '''
        deadline_units_sql = "SELECT DISTINCT deadline_unit FROM `ns_order` WHERE trans_time LIKE '{0}%';".format(self.today)
        deadline_nums_sql = "SELECT DISTINCT deadline_num FROM `ns_order` WHERE trans_time LIKE '{0}%';".format(self.today)
        deadline_units_today = [id[0] for id in self.execute_select(self.cur, deadline_units_sql)]
        deadline_nums_today = [id[0] for id in self.execute_select(self.cur, deadline_nums_sql)]
        # print(deadline_units_today,deadline_nums_today)
        result_deadline_invest = []
        for unit in deadline_units_today:
            if unit == 1:
                unit_name = '天'
            elif unit == 2:
                unit_name = '月'
            else:
                unit_name = '年'
            for num in deadline_nums_today:
                invest_amount_today_sql = "SELECT SUM(trans_amount) FROM `ns_order` WHERE deadline_unit={0} AND trans_time LIKE" \
                                          " '{1}%' AND deadline_unit={4} AND dept_code LIKE '{2}%' " \
                                          "{3};".format(unit, self.today, self.dept, self.asset_sql, num)
                # print([product_type_name_sql,invest_amount_today_sql])
                deadline_name = '{0}{1}'.format(str(num), unit_name)
                deadline_invest_amount = self.exchange_None(self.execute_select(self.cur, invest_amount_today_sql)[0][0])
                result_deadline_invest.append(deadline_name + ': %.2f' % deadline_invest_amount)
        return str(result_deadline_invest)


def dept_count_main(dept, asset):
    dc = DeptCount(dept, asset)
    today_amount, yesterday_amount =  dc.invest_amount()
    yesterday_performance_amount = dc.yesterday_performance_amount()
    today_count, yesterday_count = dc.invest_count()
    current_month_actual_exit_amount, current_month_expected_exit_amount = dc.repayment_amount()
    cashout_current_month,cashout_today,cashout_yesterday = dc.cashout_amount()
    exit_amount_today,exit_amount_yesterday = dc.exit_amount()
    if exit_amount_today != '0':
        cashout_proportion_today = str('%.2f%%' % eval(cashout_today+'/'+exit_amount_today))
    else:
        cashout_proportion_today = '0'

    if exit_amount_yesterday != '0':
        cashout_proportion_yesterday = str('%.2f%%' % eval(cashout_yesterday+'/'+exit_amount_yesterday))
    else:
        cashout_proportion_yesterday = '0'
    recharge_current_month,recharge_today,recharge_yesterday = dc.recharge_amount()
    if today_amount != '0':
        recharge_proportion_today = str('%.2f%%' % eval(recharge_today+'/'+today_amount))
    else:
        recharge_proportion_today = '0'
    repay_investor_today = str(eval(today_amount+'-'+recharge_today))
    if today_amount != '0':
        repay_investor_proportion_today = str('%.2f%%' % eval(repay_investor_today+'/'+today_amount))
    else:
        repay_investor_proportion_today = '0'
    net_amount_today = str(eval(recharge_today+'-'+cashout_today))
    net_amount_yesterday = str(eval(recharge_yesterday+'-'+cashout_yesterday))
    funds_to_be_collected,precipitated_capital = dc.funds_amount()
    openaccount_amount_today,openaccount_amount_yesterday = dc.openaccount_amount()
    month_fimc,today_fimc = dc.first_invest_match_count()
    result_product_type_invest = dc.type_invest_amount()
    result_deadline_invest = dc.deadline_num_invest_amount()

    dc.object_close()
    # print('销售快报 - 按照部门统计，统计结果如下：')
    # print('本日投资总额：' + today_amount)
    # print('昨日投资总额：' + yesterday_amount)
    # print('昨日投资业绩：' + yesterday_performance_amount)
    # print('本日投资笔数：' + today_count)
    # print('昨日投资笔数：' + yesterday_count)
    # print('本月累计已还款：' + current_month_actual_exit_amount)
    # print('本月累计待还款：' + current_month_expected_exit_amount)
    # print('本月累计提现：' + cashout_current_month)
    # print('本日累计提现：' + cashout_today)
    # print('昨日累计提现：' + cashout_yesterday)
    # print('本日提现占比：' + cashout_proportion_today)
    # print('昨日提现占比：' + cashout_proportion_yesterday)
    # print('本月累计充值：' + recharge_current_month)
    # print('本日累计充值：' + recharge_today)
    # print('昨日累计充值：' + recharge_yesterday)
    # print('本日充值投资占比：' + recharge_proportion_today)
    # print('本日还款投资：' + repay_investor_today)
    # print('本日还款投资占比：' + repay_investor_proportion_today)
    # print('本日净资金流：' + net_amount_today)
    # print('昨日净资金流：' + net_amount_yesterday)
    # print('客户待收总额：' + funds_to_be_collected)
    # print('客户沉淀总额：' + precipitated_capital)
    # print('本日累计开户数：' + openaccount_amount_today)
    # print('昨日累计开户数：' + openaccount_amount_yesterday)
    # print('本月累计首投达标客户数：' + month_fimc)
    # print('本日累计首投达标客户数：' + today_fimc)
    # print('本日各产品类型投资总额：' + result_product_type_invest)
    # print('本日各期限产品投资总额：' + result_deadline_invest)

    comment = '销售快报 - 按照部门统计，统计结果如下：' + '\n'\
        '本日投资总额：' + today_amount + '\n'\
        '昨日投资总额：' + yesterday_amount + '\n'\
        '昨日投资业绩：' + yesterday_performance_amount + '\n'\
        '本日投资笔数：' + today_count + '\n'\
        '昨日投资笔数：' + yesterday_count + '\n'\
        '本月累计已还款：' + current_month_actual_exit_amount + '\n'\
        '本月累计待还款：' + current_month_expected_exit_amount + '\n'\
        '本月累计提现：' + cashout_current_month + '\n'\
        '本日累计提现：' + cashout_today + '\n'\
        '昨日累计提现：' + cashout_yesterday + '\n'\
        '本日提现占比：' + cashout_proportion_today + '\n'\
        '昨日提现占比：' + cashout_proportion_yesterday + '\n'\
        '本月累计充值：' + recharge_current_month + '\n'\
        '本日累计充值：' + recharge_today + '\n'\
        '昨日累计充值：' + recharge_yesterday + '\n'\
        '本日充值投资占比：' + recharge_proportion_today + '\n'\
        '本日还款投资：' + repay_investor_today + '\n'\
        '本日还款投资占比：' + repay_investor_proportion_today + '\n'\
        '本日净资金流：' + net_amount_today + '\n'\
        '昨日净资金流：' + net_amount_yesterday + '\n'\
        '客户待收总额：' + funds_to_be_collected + '\n'\
        '客户沉淀总额：' + precipitated_capital + '\n'\
        '本日累计开户数：' + openaccount_amount_today + '\n'\
        '昨日累计开户数：' + openaccount_amount_yesterday + '\n'\
        '本月累计首投达标客户数：' + month_fimc + '\n'\
        '本日累计首投达标客户数：' + today_fimc + '\n'\
        '本日各产品类型投资总额：' + result_product_type_invest + '\n'\
        '本日各期限产品投资总额：' + result_deadline_invest
    print(comment)


if __name__ == '__main__':
    # dept_count_main('SHNMCW0002'，0)
    dept_count_main('SHNMCW0002', 3)


