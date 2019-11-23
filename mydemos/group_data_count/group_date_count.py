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

    def get_dept_date(self):
        the_date = self.date
        if self.dept == '0':
            the_dept = '查询整个公司'
        else:
            the_dept = self.execute_select(self.cur, "SELECT deptName FROM `data_statistics_day` WHERE deptCode='%s';" % self.dept)[0][0]
        return [the_date, the_dept]

    def invest_amount_today(self):
        ''' 当日投资总额 '''
        invest_amount_today_sql = "SELECT SUM(todayInvestAmount) FROM `data_statistics_day` WHERE entId='{0}' AND " \
                                  "DAY='{1}'{2};".format(self.entId, self.date, self.dept_sql)
        invest_amount_today = self.get_amount(invest_amount_today_sql)
        return invest_amount_today

    def invest_count_today(self):
        ''' 当日投资笔数 '''
        invest_count_today_sql = "SELECT SUM(todayInvestCount) FROM `data_statistics_day` WHERE entId='{0}' AND " \
                                 "DAY='{1}'{2};".format(self.entId, self.date, self.dept_sql)
        invest_count_today = self.get_amount(invest_count_today_sql)
        return invest_count_today

    def today_performance_amount(self):
        ''' 当日投资业绩 '''
        performance_amount_sql = "SELECT SUM(todayInvestPerformance) FROM `data_statistics_day` WHERE entId='{0}' AND " \
                                 "DAY='{1}'{2};".format(self.entId, self.date, self.dept_sql)
        today_performance_amount = self.get_amount(performance_amount_sql)
        return today_performance_amount

    def repayment_amount_today(self):
        ''' 当日还款总额 '''
        repayment_amount_sql = "SELECT SUM(todayReceivedPayment) FROM `data_statistics_day` WHERE entId='{0}' AND " \
                                 "DAY='{1}'{2};".format(self.entId, self.date, self.dept_sql)
        repayment_amount_today = self.get_amount(repayment_amount_sql)
        return repayment_amount_today

    def cashout_amount_today(self):
        ''' 当日提现总额 '''
        cashout_amount_sql = "SELECT SUM(todayCashout) FROM `data_statistics_day` WHERE entId='{0}' AND " \
                                 "DAY='{1}'{2};".format(self.entId, self.date, self.dept_sql)
        cashout_amount_today = self.get_amount(cashout_amount_sql)
        return cashout_amount_today

    def cashout_proportion_today(self):
        ''' 当日提现占比 '''
        cashout_proportion_sql = "SELECT SUM(todayCashoutProportion) FROM `data_statistics_day` WHERE entId='{0}' AND " \
                                 "DAY='{1}'{2};".format(self.entId, self.date, self.dept_sql)
        cashout_proportion_today = self.get_amount(cashout_proportion_sql)
        return cashout_proportion_today

    def recharge_amount_today(self):
        ''' 当日充值总额 '''
        recharge_amount_sql = "SELECT SUM(todayRecharge) FROM `data_statistics_day` WHERE entId='{0}' AND " \
                                 "DAY='{1}'{2};".format(self.entId, self.date, self.dept_sql)
        recharge_amount_today = self.get_amount(recharge_amount_sql)
        return recharge_amount_today

    def recharge_proportion_today(self):
        ''' 当日充值投资占比 '''
        recharge_proportion_sql = "SELECT SUM(todayRechargeInvestProportion) FROM `data_statistics_day` WHERE entId='{0}' AND " \
                                 "DAY='{1}'{2};".format(self.entId, self.date, self.dept_sql)
        recharge_proportion_today = self.get_amount(recharge_proportion_sql)
        return recharge_proportion_today

    def received_invest_today(self):
        ''' 当日还款投资 '''
        received_invest_sql = "SELECT SUM(todayReceivedInvest) FROM `data_statistics_day` WHERE entId='{0}' AND " \
                                 "DAY='{1}'{2};".format(self.entId, self.date, self.dept_sql)
        received_invest_today = self.get_amount(received_invest_sql)
        return received_invest_today

    def received_invest_proportion_today(self):
        ''' 当日还款投资占比 '''
        received_invest_proportion_sql = "SELECT SUM(todayReceivedInvestProportion) FROM `data_statistics_day` WHERE entId='{0}' AND " \
                                 "DAY='{1}'{2};".format(self.entId, self.date, self.dept_sql)
        received_invest_proportion_today = self.get_amount(received_invest_proportion_sql)
        return received_invest_proportion_today

    def net_capital_today(self):
        ''' 当日净资金流 '''
        net_capital_sql = "SELECT SUM(todayNetCapital) FROM `data_statistics_day` WHERE entId='{0}' AND " \
                                 "DAY='{1}'{2};".format(self.entId, self.date, self.dept_sql)
        net_capital_today = self.get_amount(net_capital_sql)
        return net_capital_today

    def funds_to_be_collected(self):
        ''' 当日待收总额 '''
        funds_to_be_collected_sql = "SELECT SUM(fundsToBeCollected) FROM `data_statistics_day` WHERE entId='{0}' AND " \
                                 "DAY='{1}'{2};".format(self.entId, self.date, self.dept_sql)
        funds_to_be_collected = self.get_amount(funds_to_be_collected_sql)
        return funds_to_be_collected

    def precipitated_capital(self):
        ''' 当日沉淀总额 '''
        precipitated_capital_sql = "SELECT SUM(precipitatedCapital) FROM `data_statistics_day` WHERE entId='{0}' AND " \
                                 "DAY='{1}'{2};".format(self.entId, self.date, self.dept_sql)
        precipitated_capital = self.get_amount(precipitated_capital_sql)
        return precipitated_capital

    def opening_account_count_today(self):
        ''' 当日开户客户数 '''
        opening_account_count_sql = "SELECT SUM(todayOpeningAccountCount) FROM `data_statistics_day` WHERE entId='{0}' AND " \
                                 "DAY='{1}'{2};".format(self.entId, self.date, self.dept_sql)
        opening_account_count_today = self.get_amount(opening_account_count_sql)
        return opening_account_count_today

    def first_invest_count_today(self):
        ''' 当日首投达标客户数 '''
        first_invest_count_sql = "SELECT SUM(todayFirstInvestCount) FROM `data_statistics_day` WHERE entId='{0}' AND " \
                                 "DAY='{1}'{2};".format(self.entId, self.date, self.dept_sql)
        first_invest_count_today = self.get_amount(first_invest_count_sql)
        return first_invest_count_today

    def product_type_invest_amount_today(self):
        ''' 当日各产品类型投资总额 '''
        product_type_invest_amount_sql = "SELECT SUM(todayProductTypeInvestAmount) FROM `data_statistics_day` WHERE entId='{0}' AND " \
                                 "DAY='{1}'{2};".format(self.entId, self.date, self.dept_sql)
        product_type_invest_amount_today = self.get_amount(product_type_invest_amount_sql)
        return product_type_invest_amount_today


def group_date_count_main(dept, date, name):
    gdcm = GroupDateCount(dept, date, name)
    company_name = gdcm.ent_name[name]
    the_date, the_dept = gdcm.get_dept_date()
    invest_amount_today = gdcm.invest_amount_today()
    invest_count_today = gdcm.invest_count_today()
    today_performance_amount = gdcm.today_performance_amount()
    repayment_amount_today = gdcm.repayment_amount_today()
    cashout_amount_today = gdcm.cashout_amount_today()
    cashout_proportion_today = gdcm.cashout_proportion_today()
    recharge_amount_today = gdcm.recharge_amount_today()
    recharge_proportion_today = gdcm.recharge_proportion_today()
    received_invest_today = gdcm.received_invest_today()
    received_invest_proportion_today = gdcm.received_invest_proportion_today()
    net_capital_today = gdcm.net_capital_today()
    funds_to_be_collected = gdcm.funds_to_be_collected()
    precipitated_capital = gdcm.precipitated_capital()
    opening_account_count_today = gdcm.opening_account_count_today()
    first_invest_count_today = gdcm.first_invest_count_today()
    product_type_invest_amount_today = gdcm.product_type_invest_amount_today()


    gdcm.object_close()

    comment = '集团数据统计，销售日报，统计结果如下：' + '( 公司名称：%s, 部门：%s, 日期：%s )'%(company_name, the_dept, the_date) + '\n'\
        '当日投资总额：' + invest_amount_today + '\n'\
        '当日投资笔数：' + invest_count_today + '\n'\
        '当日投资业绩：' + today_performance_amount + '\n'\
        '当日还款总额：' + repayment_amount_today + '\n'\
        '当日提现总额：' + cashout_amount_today + '\n'\
        '当日提现占比：' + cashout_proportion_today + '\n'\
        '当日充值总额：' + recharge_amount_today + '\n'\
        '当日充值投资占比：' + recharge_proportion_today + '\n'\
        '当日还款投资：' + received_invest_today + '\n'\
        '当日还款投资占比：' + received_invest_proportion_today + '\n'\
        '当日净资金流：' + net_capital_today + '\n'\
        '当日待收总额：' + funds_to_be_collected + '\n'\
        '当日沉淀总额：' + precipitated_capital + '\n'\
        '当日开户客户数：' + opening_account_count_today + '\n'\
        '当日首投达标客户数：' + first_invest_count_today + '\n'\
        '当日各产品类型投资总额：' + product_type_invest_amount_today + '\n'\

    print(comment)


if __name__ == '__main__':
    # group_date_count_main('0', '0', 'nami')
    # group_date_count_main('SHNMCW0002', '2019-11-20', 'nami')
    # group_date_count_main('SHNMCW0004', '2019-11-20', 'nami')
    group_date_count_main('0', '2019-11-20', 'nami')




