#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : Li ZiHao
# @Time     : 2019/11/2 0:32
# @File     : month_count.py

import datetime
import time
from opt_mysql import Optsql


class MonthCount(Optsql):
    def __init__(self, dept, date):
        self.dept = dept
        self.cur = self.conn_mysql()
        date_today = datetime.date.today()
        self.today = str(date_today)
        self.yesterday = str(date_today - datetime.timedelta(days=1))
        if date == '0':
            self.current_month = time.strftime('%Y-%m')
        else:
            self.current_month = date

        if self.current_month[-2:] == '01':
            self.last_month = str(eval(self.current_month[:4] + '-1')) + '-12'
        else:
            self.last_month = self.current_month[:4] + '-%s' % str(int(self.current_month[-2:])-1).zfill(2)

    def exchange_None(self, para):
        if para:
            return para
        else:
            return 0

    def dept_name_date(self):
        ''' 获取部门名称和日期 '''
        dept_name_sql = "SELECT NAME FROM `wbs_department` WHERE CODE = '{0}';".format(self.dept)
        dept_name = self.execute_select(self.cur,dept_name_sql)[0][0]
        the_month = str(self.current_month)
        return [dept_name, the_month]

    def current_month_invest_amount(self):
        '''当月投资总额 '''
        current_month_amount_sql = "SELECT SUM(trans_amount) FROM `ns_order` WHERE Convert(trans_time,CHAR(20)) " \
                          "LIKE '{0}%' AND dept_code LIKE '{1}%';".format(self.current_month, self.dept)
        current_month_amount = self.exchange_None(self.execute_select(self.cur, current_month_amount_sql)[0][0])
        return str(current_month_amount/10000)

    def last_month_invest_amount(self):
        '''上月投资总额 '''
        last_month_amount_sql = "SELECT SUM(trans_amount) FROM `ns_order` WHERE Convert(trans_time,CHAR(20)) " \
                          "LIKE '{0}%' AND dept_code LIKE '{1}%';".format(self.last_month, self.dept)
        last_month_amount = self.exchange_None(self.execute_select(self.cur, last_month_amount_sql)[0][0])
        return str(last_month_amount/10000)

    def invest_count(self):
        '''当月投资笔数'''
        current_month_count_sql = "SELECT COUNT(1) FROM `ns_order` WHERE Convert(trans_time,CHAR(20)) " \
                          "LIKE '{0}%' AND dept_code LIKE '{1}%';".format(self.current_month, self.dept)
        current_month_count = self.exchange_None(self.execute_select(self.cur, current_month_count_sql)[0][0])
        return str(current_month_count)

    def performance_amount(self):
        '''当月投资业绩、上月投资业绩'''
        current_month_amount_sql = "SELECT SUM(performance_amount) FROM `ns_sop_order_snapshot` WHERE " \
                              "Convert(trans_time,CHAR(20)) LIKE '{0}%' AND department_no LIKE '{1}%';".format(self.current_month, self.dept)
        last_month_amount_sql = "SELECT SUM(performance_amount) FROM `ns_sop_order_snapshot` WHERE " \
                                   "Convert(trans_time,CHAR(20)) LIKE '{0}%' AND department_no LIKE '{1}%';".format(self.last_month, self.dept)
        current_month_performance_amount = self.exchange_None(self.execute_select(self.cur, current_month_amount_sql)[0][0])
        last_month_performance_amount = self.exchange_None(self.execute_select(self.cur, last_month_amount_sql)[0][0])
        return [str(current_month_performance_amount/10000), str(last_month_performance_amount/10000)]

    def repayment_amount_current_month(self):
        '''当月还款总额'''
        repayed_amount_sql = "SELECT SUM(actual_exit_amount) FROM `wbs_received_payment` WHERE " \
                             "Convert(actual_exit_time,CHAR(20)) LIKE '{0}%' AND STATUS = 2 AND dept_code " \
                             "LIKE '{1}%';".format(self.current_month, self.dept)
        repayed_amount_current_month = self.exchange_None(self.execute_select(self.cur, repayed_amount_sql)[0][0])
        return str(repayed_amount_current_month/10000)

    def cashout_amount(self):
        ''' 当月提现总额 '''
        cashout_current_month_sql = "SELECT SUM(cashout_amount) FROM `ns_cashout_record` WHERE 1=1 AND STATUS=3 AND Convert(cashout_time,CHAR(20)) " \
                            "LIKE '{0}%' AND dept_code LIKE '{1}%';".format(self.current_month, self.dept)
        cashout_current_month = self.exchange_None(self.execute_select(self.cur, cashout_current_month_sql)[0][0])
        return str(cashout_current_month/10000)

    def recharge_amount_current_month(self):
        ''' 当月充值总额 '''
        recharge_current_month_sql = "SELECT SUM(recharge_amount) FROM `ns_recharge_record` WHERE 1=1 AND STATUS=3 AND Convert(recharge_time,CHAR(20)) " \
                            "LIKE '{0}%' AND dept_code LIKE '{1}%';".format(self.current_month, self.dept)
        recharge_current_month = self.exchange_None(self.execute_select(self.cur, recharge_current_month_sql)[0][0])
        return str(recharge_current_month/10000)

    def funds_amount(self):
        ''' 当月待收总额、当月沉淀总额 '''
        asset_funds_to_be_collected_sql = "SELECT SUM(a.funds_to_be_collected) FROM `wbs_asset_cus_account` a, " \
                                          "`wbs_customer` c WHERE c.`deptCode` LIKE '{0}%' AND Convert(a.update_time,CHAR(20))" \
                                          " LIKE '{1}%' AND a.`cus_id`=c.`id`;".format(self.dept, self.current_month)
        asset_precipitated_capital_sql = "SELECT SUM(a.precipitated_capital) FROM `wbs_asset_cus_account` a, " \
                                          "`wbs_customer` c WHERE c.`deptCode` LIKE '{0}%' AND Convert(a.update_time,CHAR(20))" \
                                          " LIKE '{1}%' AND a.`cus_id`=c.`id`;".format(self.dept, self.current_month)
        stock_funds_to_be_collected_sql = "SELECT SUM(funds_to_be_collected) FROM `wbs_stock_customer` WHERE dept_code" \
                                          " LIKE '{0}%' AND deleted=0 AND Convert(update_time,CHAR(20)) LIKE '{1}%';".format(self.dept, self.current_month)
        stock_precipitated_capital_sql = "SELECT SUM(precipitated_capital) FROM `wbs_stock_customer` WHERE dept_code" \
                                          " LIKE '{0}%' AND deleted=0 AND Convert(update_time,CHAR(20)) LIKE '{1}%';".format(self.dept, self.current_month)

        asset_funds_to_be_collected = self.exchange_None(self.execute_select(self.cur,asset_funds_to_be_collected_sql)[0][0])
        asset_precipitated_capital = self.exchange_None(self.execute_select(self.cur,asset_precipitated_capital_sql)[0][0])
        stock_funds_to_be_collected = self.exchange_None(self.execute_select(self.cur,stock_funds_to_be_collected_sql)[0][0])
        stock_precipitated_capital = self.exchange_None(self.execute_select(self.cur,stock_precipitated_capital_sql)[0][0])
        funds_to_be_collected = asset_funds_to_be_collected + stock_funds_to_be_collected
        precipitated_capital = asset_precipitated_capital + stock_precipitated_capital
        return [str(funds_to_be_collected/10000), str(precipitated_capital/10000)]

    def openaccount_amount(self):
        ''' 当月开户客户数 '''
        asset_openaccount_amount_current_month_sql = "SELECT COUNT(1) FROM `wbs_asset_cus_account` a, `wbs_customer` c WHERE" \
                                             " c.deptCode LIKE '{0}%' AND c.id=a.cus_id AND" \
                                             " Convert(platform_account_opening_time,CHAR(20)) LIKE '{1}%';".format(self.dept, self.current_month)
        stock_openaccount_amount_current_month_sql = "SELECT COUNT(1) FROM `wbs_stock_customer` WHERE 1=1 AND dept_code " \
                                             "LIKE '{1}%' AND deleted=0 AND Convert(platform_account_opening_time,CHAR(20))" \
                                             " LIKE '{0}%';".format(self.current_month, self.dept)
        asset_openaccount_amount_current_month = self.exchange_None(self.execute_select(self.cur, asset_openaccount_amount_current_month_sql)[0][0])
        stock_openaccount_amount_current_month = self.exchange_None(self.execute_select(self.cur, stock_openaccount_amount_current_month_sql)[0][0])
        openaccount_amount_current_month = asset_openaccount_amount_current_month + stock_openaccount_amount_current_month
        return str(openaccount_amount_current_month)

    def first_invest_match_count(self):
        ''' 当月首投达标客户数 '''
        ''' fimc = first_invest_match_count '''
        current_month_HY_fimc_sql = "SELECT COUNT(1) FROM `ns_order` WHERE Convert(trans_time,CHAR(20)) LIKE '{0}%'" \
                        " AND first_invest=1 AND dept_code LIKE '{1}%' AND asset_id=1 AND trans_amount>=3000;".format(self.current_month, self.dept)
        current_month_HJS_fimc_sql = "SELECT COUNT(1) FROM `ns_order` WHERE Convert(trans_time,CHAR(20)) LIKE '{0}%'" \
                        " AND first_invest=1 AND dept_code LIKE '{1}%' AND asset_id=2 AND trans_amount>=20000;".format(self.current_month, self.dept)
        current_month_HP_fimc_sql = "SELECT COUNT(1) FROM `ns_order` WHERE Convert(trans_time,CHAR(20)) LIKE '{0}%'" \
                        " AND first_invest=1 AND dept_code LIKE '{1}%' AND asset_id=3 AND trans_amount>=20000;".format(self.current_month, self.dept)
        current_month_HY_fimc = self.exchange_None(self.execute_select(self.cur, current_month_HY_fimc_sql)[0][0])
        current_month_HJS_fimc = self.exchange_None(self.execute_select(self.cur, current_month_HJS_fimc_sql)[0][0])
        current_month_HP_fimc = self.exchange_None(self.execute_select(self.cur, current_month_HP_fimc_sql)[0][0])
        current_month_fimc = current_month_HY_fimc + current_month_HJS_fimc + current_month_HP_fimc
        return str(current_month_fimc)

    def type_invest_amount(self):
        ''' 当月各产品类型投资总额 '''
        type_ids_sql = "SELECT DISTINCT product_type FROM `ns_order` WHERE Convert(trans_time,CHAR(20)) LIKE '{0}%';".format(self.current_month)
        type_ids_current_month = [id[0] for id in self.execute_select(self.cur, type_ids_sql)]
        result_product_type_invest = []
        for id in type_ids_current_month:
            product_type_name_sql = "SELECT product_type_name FROM `ns_product_type` WHERE id=%d;" % id
            invest_amount_current_month_sql = "SELECT SUM(trans_amount) FROM `ns_order` WHERE product_type={0} AND Convert(trans_time,CHAR(20)) LIKE" \
                                  " '{1}%' AND dept_code LIKE '{2}%';".format(id, self.current_month, self.dept)
            # print([product_type_name_sql,invest_amount_today_sql])
            product_type_name = self.execute_select(self.cur, product_type_name_sql)[0][0]
            product_type_invest_amount = self.exchange_None(self.execute_select(self.cur, invest_amount_current_month_sql)[0][0])
            if not product_type_invest_amount:
                continue
            result_product_type_invest.append((product_type_name+':%s' % str(id), '%.4f' % (product_type_invest_amount/10000)))
        return str(result_product_type_invest)

    def deadline_num_invest_amount(self):
        ''' 当日各期限产品投资总额 '''
        deadline_units_sql = "SELECT DISTINCT deadline_unit FROM `ns_order` WHERE Convert(trans_time,CHAR(20)) LIKE '{0}%';".format(self.current_month)
        deadline_nums_sql = "SELECT DISTINCT deadline_num FROM `ns_order` WHERE Convert(trans_time,CHAR(20)) LIKE '{0}%';".format(self.current_month)
        deadline_units_current_month = [id[0] for id in self.execute_select(self.cur, deadline_units_sql)]
        deadline_nums_current_month = [id[0] for id in self.execute_select(self.cur, deadline_nums_sql)]
        result_deadline_invest = []
        for unit in deadline_units_current_month:
            if unit == 1:
                unit_name = '天'
            elif unit == 2:
                unit_name = '月'
            else:
                unit_name = '年'
            for num in deadline_nums_current_month:
                invest_amount_current_month_sql = "SELECT SUM(trans_amount) FROM `ns_order` WHERE deadline_unit={0} AND Convert(trans_time,CHAR(20)) LIKE" \
                                          " '{1}%' AND deadline_num={3} AND dept_code LIKE '{2}%';".format(unit, self.current_month, self.dept, num)
                deadline_name = '{0}{1}'.format(str(num), unit_name)
                deadline_invest_amount = self.exchange_None(self.execute_select(self.cur, invest_amount_current_month_sql)[0][0])
                if not deadline_invest_amount:
                    continue
                result_deadline_invest.append(deadline_name + ': %.4f' % (deadline_invest_amount/10000))
        return str(result_deadline_invest)


def month_count_main(dept, date):
    mc = MonthCount(dept, date)
    dept_name, the_month = mc.dept_name_date()
    current_month_amount = mc.current_month_invest_amount()
    last_month_amount = mc.last_month_invest_amount()
    if last_month_amount == '0.0':
        investment_growth_rate = '0'
    else:
        investment_growth_rate = '%.4f%%' % ((float(current_month_amount)-float(last_month_amount))/float(last_month_amount)*100)
    current_month_count = mc.invest_count()
    current_month_performance_amount, last_month_performance_amount = mc.performance_amount()
    if last_month_performance_amount == '0.0':
        performance_growth_rate = '0'
    else:
        performance_growth_rate = '%.4f%%' % ((float(current_month_performance_amount)-float(last_month_performance_amount))/float(last_month_performance_amount)*100)
    repayed_amount_current_month = mc.repayment_amount_current_month()
    cashout_current_month = mc.cashout_amount()
    if repayed_amount_current_month != '0.0':
        cashout_proportion_current_month = str('%.4f%%' % eval(cashout_current_month+'/'+repayed_amount_current_month+'*100'))
    else:
        cashout_proportion_current_month = '0'
    recharge_current_month = mc.recharge_amount_current_month()
    if current_month_amount != '0.0':
        recharge_proportion_current_month = str('%.4f%%' % eval(recharge_current_month+'/'+current_month_amount+'*100'))
    else:
        recharge_proportion_current_month = '0'
    repay_investor_current_month = str(eval(current_month_amount + '-' + recharge_current_month))
    if current_month_amount != '0.0':
        repay_investor_proportion_current_month = str('%.4f%%' % eval(repay_investor_current_month+'/'+current_month_amount+'*100'))
    else:
        repay_investor_proportion_current_month = '0'
    net_amount_current_month = str(eval(recharge_current_month + '-' + cashout_current_month))
    funds_to_be_collected, precipitated_capital = mc.funds_amount()
    openaccount_amount_current_month = mc.openaccount_amount()
    current_month_fimc = mc.first_invest_match_count()
    result_product_type_invest = mc.type_invest_amount()
    result_deadline_invest = mc.deadline_num_invest_amount()

    comment = '销售日报，统计结果如下：' + '( 部门：%s, 搜索日期：%s )' % (dept_name, the_month) + '\n' \
        '当月投资总额：' + current_month_amount + '\n' \
        '上月投资总额：' + last_month_amount + '\n' \
        '投资总额环比增速：' + investment_growth_rate + '\n' \
        '当月投资笔数：' + current_month_count + '\n' \
        '当月投资业绩：' + current_month_performance_amount + '\n' \
        '上月投资业绩：' + last_month_performance_amount + '\n' \
        '投资业绩环比增速：' + performance_growth_rate + '\n' \
        '当月还款总额：' + repayed_amount_current_month + '\n' \
        '当月提现总额：' + cashout_current_month + '\n' \
        '当月提现占比：' + cashout_proportion_current_month + '\n' \
        '当月充值总额：' + recharge_current_month + '\n' \
        '当月充值投资占比：' + recharge_proportion_current_month + '\n' \
        '当月还款投资：' + repay_investor_current_month + '\n' \
        '当月还款投资占比：' + repay_investor_proportion_current_month + '\n' \
        '当月净资金流：' + net_amount_current_month + '\n' \
        '当月待收总额：' + funds_to_be_collected + '\n' \
        '当月沉淀总额：' + precipitated_capital + '\n' \
        '当月开户客户数：' + openaccount_amount_current_month + '\n' \
        '当月首投达标客户数：' + current_month_fimc + '\n' \
        '当月各产品类型投资总额：' + result_product_type_invest + '\n' \
        '当月各期限产品投资总额：' + result_deadline_invest + '\n' \

    print(comment)


if __name__ == '__main__':
    # month_count_main('SHNMCW0002', '0')
    month_count_main('SHNMCW0002', '2019-11')