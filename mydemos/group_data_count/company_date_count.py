#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : Li ZiHao
# @Time     : 2019/11/2 0:38
# @File     : company_date_count.py

import datetime
import time
import opt_group_mysql
from opt_group_mysql import Optsql


class DateCount(Optsql):
    def __init__(self, dept, date, name):
        self.dept = dept
        self.name = name
        self.cur, self.conn = self.conn_mysql(name)
        self.sm_cur, self.sm_conn = self.conn_mysql("shengmei")
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

    def exchange_None(self, para):
        if para:
            return para
        else:
            return 0

    def object_close(self):
        super(DateCount, self).object_close(self.cur, self.conn)

    def object_sm_close(self):
        super(DateCount, self).object_close(self.sm_cur, self.sm_conn)

    def dept_name_date(self):
        ''' 获取部门名称和日期 '''
        dept_name_sql = "SELECT NAME FROM `wbs_department` WHERE CODE = '{0}';".format(self.dept)
        dept_name = self.execute_select(self.cur, dept_name_sql)[0][0]
        the_datetime = str(self.date)
        return [dept_name, the_datetime]

    def invest_amount(self):
        '''当日投资总额 '''
        today_amount_sql = "SELECT SUM(trans_amount) FROM `ns_order` WHERE trans_time " \
                          "LIKE '{0}%' AND dept_code LIKE '{1}%';".format(self.date, self.dept)
        today_amount = self.exchange_None(self.execute_select(self.cur, today_amount_sql)[0][0])
        return str(today_amount/10000)

    def invest_count(self):
        '''当日投资笔数'''
        today_count_sql = "SELECT COUNT(1) FROM `ns_order` WHERE trans_time " \
                          "LIKE '{0}%' AND dept_code LIKE '{1}%';".format(self.date, self.dept)
        today_count = self.exchange_None(self.execute_select(self.cur, today_count_sql)[0][0])
        return str(today_count)

    def today_performance_amount(self):
        '''当日投资业绩'''
        today_amount_sql = "SELECT SUM(performance_amount) FROM `ns_sop_order_snapshot_summary` WHERE " \
                              "trans_time LIKE '{0}%' AND department_no LIKE '{1}%';".format(self.date, self.dept)
        today_performance_amount = self.exchange_None(self.execute_select(self.cur, today_amount_sql)[0][0])
        return str(today_performance_amount/10000)

    def repayment_amount_today(self):
        '''当日还款总额'''
        repayed_amount_sql = "SELECT SUM(actual_exit_amount) FROM `wbs_received_payment` WHERE " \
                             "Convert(actual_exit_time,CHAR(20)) LIKE '{0}%' AND STATUS = 2 AND dept_code " \
                             "LIKE '{1}%';".format(self.date, self.dept)
        repayed_amount_today = self.exchange_None(self.execute_select(self.cur, repayed_amount_sql)[0][0])
        return str(repayed_amount_today/10000)

    def cashout_amount(self):
        ''' 当日提现总额 '''
        cashout_today_sql = "SELECT SUM(cashout_amount) FROM `ns_cashout_record` WHERE 1=1 AND STATUS=3 AND Convert(cashout_time,CHAR(20)) " \
                            "LIKE '{0}%' AND dept_code LIKE '{1}%';".format(self.date, self.dept)
        cashout_today = self.exchange_None(self.execute_select(self.cur, cashout_today_sql)[0][0])
        return str(cashout_today/10000)

    def recharge_amount_today(self):
        ''' 当日充值总额 '''
        recharge_today_sql = "SELECT SUM(recharge_amount) FROM `ns_recharge_record` WHERE 1=1 AND STATUS=3 AND Convert(recharge_time,CHAR(20)) " \
                            "LIKE '{0}%' AND dept_code LIKE '{1}%';".format(self.date, self.dept)
        recharge_today = self.exchange_None(self.execute_select(self.cur, recharge_today_sql)[0][0])
        return str(recharge_today/10000)

    def funds_amount(self):
        ''' 当日待收总额、当日沉淀总额 '''
        stock_funds_to_be_collected_sql = "SELECT fundsToBeCollected FROM `data_statistics_day` WHERE deptCode" \
                                          " LIKE '{0}%' AND day LIKE '{1}%' AND entId={2};".format(self.dept, self.date, self.ent_id[self.name])
        stock_precipitated_capital_sql = "SELECT precipitatedCapital FROM `data_statistics_day` WHERE deptCode" \
                                          " LIKE '{0}%' AND day LIKE '{1}%' AND entId={2};".format(self.dept, self.date, self.ent_id[self.name])
        stock_funds_to_be_collected = self.exchange_None(self.execute_select(self.sm_cur, stock_funds_to_be_collected_sql)[0][0])
        stock_precipitated_capital = self.exchange_None(self.execute_select(self.sm_cur, stock_precipitated_capital_sql)[0][0])
        return [str(stock_funds_to_be_collected), str(stock_precipitated_capital)]

    def openaccount_amount(self):
        ''' 当日开户客户数 '''
        stock_openaccount_amount_today_sql = "SELECT COUNT(1) FROM `wbs_stock_customer` WHERE 1=1 AND dept_code " \
                                             "LIKE '{1}%' AND platform_account_opening_time" \
                                             " LIKE '{0}%';".format(self.date, self.dept)
        stock_openaccount_amount_today = self.exchange_None(self.execute_select(self.cur, stock_openaccount_amount_today_sql)[0][0])
        return str(stock_openaccount_amount_today)

    def first_invest_match_count(self):
        ''' 当日首投达标客户数 '''
        ''' fimc = first_invest_match_count '''
        today_HY_fimc_sql = "SELECT COUNT(1) FROM `ns_order` WHERE Convert(trans_time,CHAR(20)) LIKE '{0}%'" \
                        " AND first_invest=1 AND dept_code LIKE '{1}%' AND asset_id=1 AND trans_amount>=3000;".format(self.date, self.dept)
        today_HJS_fimc_sql = "SELECT COUNT(1) FROM `ns_order` WHERE Convert(trans_time,CHAR(20)) LIKE '{0}%'" \
                        " AND first_invest=1 AND dept_code LIKE '{1}%' AND asset_id=2 AND trans_amount>=20000;".format(self.date, self.dept)
        today_HP_fimc_sql = "SELECT COUNT(1) FROM `ns_order` WHERE Convert(trans_time,CHAR(20)) LIKE '{0}%'" \
                        " AND first_invest=1 AND dept_code LIKE '{1}%' AND asset_id=3 AND trans_amount>=20000;".format(self.date, self.dept)
        today_HY_fimc = self.exchange_None(self.execute_select(self.cur, today_HY_fimc_sql)[0][0])
        today_HJS_fimc = self.exchange_None(self.execute_select(self.cur, today_HJS_fimc_sql)[0][0])
        today_HP_fimc = self.exchange_None(self.execute_select(self.cur, today_HP_fimc_sql)[0][0])
        today_fimc = today_HY_fimc + today_HJS_fimc + today_HP_fimc
        return str(today_fimc)

    def type_invest_amount(self):
        ''' 当日各产品类型投资总额 '''
        type_ids_sql = "SELECT DISTINCT product_type FROM `ns_order` WHERE trans_time LIKE '{0}%';".format(self.date)
        type_ids_today = [id[0] for id in self.execute_select(self.cur, type_ids_sql)]
        result_product_type_invest = []
        for id in type_ids_today:
            product_type_name_sql = "SELECT product_type_name FROM `ns_product_type` WHERE id=%d;" % id
            invest_amount_today_sql = "SELECT SUM(trans_amount) FROM `ns_order` WHERE product_type={0} AND trans_time LIKE" \
                                  " '{1}%' AND dept_code LIKE '{2}%';".format(id, self.date, self.dept)
            # print([product_type_name_sql,invest_amount_today_sql])
            product_type_name = self.execute_select(self.cur, product_type_name_sql)[0][0]
            product_type_invest_amount = self.exchange_None(self.execute_select(self.cur, invest_amount_today_sql)[0][0])
            if not product_type_invest_amount:
                continue
            result_product_type_invest.append((product_type_name+':%s' % str(id), '%.4f' % (product_type_invest_amount/10000)))
        return str(result_product_type_invest)

    def deadline_num_invest_amount(self):
        ''' 当日各期限产品投资总额 '''
        deadline_units_sql = "SELECT DISTINCT deadline_unit FROM `ns_order` WHERE trans_time LIKE '{0}%';".format(self.date)
        deadline_nums_sql = "SELECT DISTINCT deadline_num FROM `ns_order` WHERE trans_time LIKE '{0}%';".format(self.date)
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
                                          " '{1}%' AND deadline_num={3} AND dept_code LIKE '{2}%';".format(unit, self.date, self.dept, num)
                # print([product_type_name_sql,invest_amount_today_sql])
                deadline_name = '{0}{1}'.format(str(num), unit_name)
                deadline_invest_amount = self.exchange_None(self.execute_select(self.cur, invest_amount_today_sql)[0][0])
                if not deadline_invest_amount:
                    continue
                result_deadline_invest.append(deadline_name + ': %.4f' % (deadline_invest_amount/10000))
        return str(result_deadline_invest)


def date_count_main(dept, date, name):
    dcm = DateCount(dept, date, name)
    dept_name, the_datetime = dcm.dept_name_date()
    today_amount = dcm.invest_amount()
    today_count = dcm.invest_count()
    today_performance_amount = dcm.today_performance_amount()
    repayed_amount_today = dcm.repayment_amount_today()
    cashout_today = dcm.cashout_amount()
    if repayed_amount_today != '0.0':
        cashout_proportion_today = str('%.4f%%' % eval(cashout_today+'/'+repayed_amount_today+'*100'))
    else:
        cashout_proportion_today = '0'
    recharge_today = dcm.recharge_amount_today()
    if today_amount != '0.0':
        recharge_proportion_today = str('%.4f%%' % eval(recharge_today+'/'+today_amount+'*100'))
    else:
        recharge_proportion_today = '0'
    repay_investor_today = str(eval(today_amount + '-' + recharge_today))
    if today_amount != '0.0':
        repay_investor_proportion_today = str('%.4f%%' % eval(repay_investor_today+'/'+today_amount+'*100'))
    else:
        repay_investor_proportion_today = '0'
    net_amount_today = str(eval(recharge_today + '-' + cashout_today))
    funds_to_be_collected, precipitated_capital = dcm.funds_amount()
    openaccount_amount_today = dcm.openaccount_amount()
    today_fimc = dcm.first_invest_match_count()
    result_product_type_invest = dcm.type_invest_amount()
    result_deadline_invest = dcm.deadline_num_invest_amount()

    dcm.object_close()
    dcm.object_sm_close()

    comment = '销售日报，统计结果如下：' + '( 部门：%s, 日期：%s )'%(dept_name, the_datetime) + '\n'\
        '当日投资总额：' + today_amount + '\n'\
        '当日投资笔数：' + today_count + '\n'\
        '当日投资业绩：' + today_performance_amount + '\n'\
        '当日还款总额：' + repayed_amount_today + '\n'\
        '当日提现总额：' + cashout_today + '\n'\
        '当日提现占比：' + cashout_proportion_today + '\n'\
        '当日充值总额：' + recharge_today + '\n'\
        '当日充值投资占比：' + recharge_proportion_today + '\n'\
        '当日还款投资：' + repay_investor_today + '\n'\
        '当日还款投资占比：' + repay_investor_proportion_today + '\n'\
        '当日净资金流：' + net_amount_today + '\n'\
        '当日待收总额：' + funds_to_be_collected + '\n'\
        '当日沉淀总额：' + precipitated_capital + '\n'\
        '当日开户客户数：' + openaccount_amount_today + '\n'\
        '当日首投达标客户数：' + today_fimc + '\n'\
        '当日各产品类型投资总额：' + result_product_type_invest + '\n'\
        '当日各期限产品投资总额：' + result_deadline_invest

    print(comment)


if __name__ == '__main__':
    # date_count_main('SHNMCW0002', '0', 'nami')
    date_count_main('SHNMCW0013', '2019-12-03', 'nami')