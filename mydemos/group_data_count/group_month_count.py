#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : Li ZiHao
# @Time     : 2019/11/23 16:36
# @File     : group_month_count.py

import datetime
import time
from opt_group_mysql import Optsql


class GroupMonthCount(Optsql):
    def __init__(self, dept, date, name):
        self.dept = dept
        self.name = name
        self.cur, self.conn = self.conn_mysql("shengmei")
        self.ent_cur, self.ent_conn = self.conn_mysql(self.name)
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

        if dept == '0':
            self.dept_sql = ""
        else:
            self.dept_sql = " AND deptCode like '%s'" % dept

    def exchange_None(self, para):
        if para:
            return para
        else:
            return 0

    def object_close(self):
        super(GroupMonthCount, self).object_close(self.cur, self.conn)

    def get_dept_date(self):
        the_date = self.current_month
        if self.dept == '0':
            the_dept = '查询整个公司'
        else:
            the_dept = self.execute_select(self.cur, "SELECT deptName FROM `data_statistics_day` WHERE deptCode='%s';" % self.dept)[0][0]
        ent_name = self.ent_name[self.name]
        return [the_date, the_dept, ent_name]

    def company_count(self):
        company_count_sql = "SELECT SUM(currentMonthNetCapital), SUM(currentMonthInvestAmount), SUM(lastMonthInvestAmount), SUM(currentMonthInvestCount)," \
                            " SUM(currentMonthInvestPerformance), SUM(lastMonthInvestPerformance), SUM(currentMonthReceivedPayment), " \
                            "SUM(currentMonthCashout), SUM(currentMonthRecharge), SUM(currentMonthReceivedInvest), SUM(fundsToBeCollected), " \
                            "SUM(precipitatedCapital), SUM(currentMonthOpeningAccountCount), SUM(currentMonthFirstInvestCount) " \
                            "FROM data_statistics_month WHERE  MONTH = '{0}' AND entId = {1} AND deptLevel=1;".format(self.current_month, self.ent_id[self.name])
        # print(company_count_sql)
        company_count_res = self.execute_select(self.cur, company_count_sql)[0]
        # print([value for value in company_count_res])
        currentMonthNetCapital, currentMonthInvestAmount, lastMonthInvestAmount, currentMonthInvestCount, currentMonthInvestPerformance, lastMonthInvestPerformance, currentMonthReceivedPayment, currentMonthCashout, currentMonthRecharge, currentMonthReceivedInvest, fundsToBeCollected, precipitatedCapital, currentMonthOpeningAccountCount, currentMonthFirstInvestCount = [str(value) for value in company_count_res]
        # print(int(lastMonthInvestAmount))
        if lastMonthInvestAmount == '0.0000':
            investAmountLinkRelativeRatio = '0'
        else:
            investAmountLinkRelativeRatio = str('%.4f%%' % eval("({0}-{1})/{1}*100".format(currentMonthInvestAmount, lastMonthInvestAmount)))

        if lastMonthInvestPerformance == '0.0000':
            investPerformanceLinkRelativeRatio = '0'
        else:
            investPerformanceLinkRelativeRatio = str('%.4f%%' % eval("({0}-{1})/{1}*100".format(currentMonthInvestPerformance, lastMonthInvestPerformance)))

        if currentMonthReceivedPayment == '0.0000':
            currentMonthCashoutProportion = '0'
        else:
            currentMonthCashoutProportion = str('%.4f%%' % eval("({0}/{1})*100".format(currentMonthCashout, currentMonthReceivedPayment)))
        # print(currentMonthCashoutProportion)

        if currentMonthInvestAmount == '0.0000':
            currentMonthRechargeInvestProportion = '0'
        else:
            currentMonthRechargeInvestProportion = str('%.4f%%' % eval("({0}/{1})*100".format(currentMonthRecharge, currentMonthInvestAmount)))
        # print(currentMonthRechargeInvestProportion)

        if currentMonthInvestAmount == '0.0000':
            currentMonthReceivedInvestProportion = '0'
        else:
            currentMonthReceivedInvestProportion = str('%.4f%%' % eval("({0}/{1})*100".format(currentMonthReceivedInvest, currentMonthInvestAmount)))
        # print(currentMonthReceivedInvestProportion)

        type_ids_sql = "SELECT DISTINCT product_type FROM `ns_order` WHERE Convert(trans_time,CHAR(20)) LIKE '{0}%';".format(self.current_month)
        type_ids_current_month = [id[0] for id in self.execute_select(self.ent_cur, type_ids_sql)]
        currentMonthProductTypeInvestAmount = []
        for id in type_ids_current_month:
            product_type_name_sql = "SELECT product_type_name FROM `ns_product_type` WHERE id=%d;" % id
            invest_amount_current_month_sql = "SELECT SUM(trans_amount) FROM `ns_order` WHERE product_type={0} AND Convert(trans_time,CHAR(20)) LIKE" \
                                              " '{1}%';".format(id, self.current_month)
            # print([product_type_name_sql,invest_amount_today_sql])
            product_type_name = self.execute_select(self.ent_cur, product_type_name_sql)[0][0]
            product_type_invest_amount = self.exchange_None(self.execute_select(self.ent_cur, invest_amount_current_month_sql)[0][0])
            if not product_type_invest_amount:
                continue
            currentMonthProductTypeInvestAmount.append((product_type_name + ':%s' % str(id), '%.4f' % (product_type_invest_amount / 10000)))

        deadline_units_sql = "SELECT DISTINCT deadline_unit FROM `ns_order` WHERE Convert(trans_time,CHAR(20)) LIKE '{0}%';".format(self.current_month)
        deadline_nums_sql = "SELECT DISTINCT deadline_num FROM `ns_order` WHERE Convert(trans_time,CHAR(20)) LIKE '{0}%';".format( self.current_month)
        deadline_units_current_month = [id[0] for id in self.execute_select(self.ent_cur, deadline_units_sql)]
        deadline_nums_current_month = [id[0] for id in self.execute_select(self.ent_cur, deadline_nums_sql)]
        currentMonthDeadlineInvestAmount = []
        for unit in deadline_units_current_month:
            if unit == 1:
                unit_name = '天'
            elif unit == 2:
                unit_name = '月'
            else:
                unit_name = '年'
            for num in deadline_nums_current_month:
                invest_amount_current_month_sql = "SELECT SUM(trans_amount) FROM `ns_order` WHERE deadline_unit={0} AND Convert(trans_time,CHAR(20)) LIKE" \
                                                  " '{1}%' AND deadline_num={2};".format(unit, self.current_month, num)
                deadline_name = '{0}{1}'.format(str(num), unit_name)
                deadline_invest_amount = self.exchange_None(self.execute_select(self.ent_cur, invest_amount_current_month_sql)[0][0])
                if not deadline_invest_amount:
                    continue
                currentMonthDeadlineInvestAmount.append(deadline_name + ': %.4f' % (deadline_invest_amount / 10000))

        return [currentMonthInvestAmount, lastMonthInvestAmount, investAmountLinkRelativeRatio, currentMonthInvestCount, currentMonthInvestPerformance, lastMonthInvestPerformance, investPerformanceLinkRelativeRatio, currentMonthReceivedPayment, currentMonthCashout, currentMonthCashoutProportion, currentMonthRecharge, currentMonthRechargeInvestProportion, currentMonthReceivedInvest, currentMonthReceivedInvestProportion, currentMonthNetCapital, fundsToBeCollected, precipitatedCapital, currentMonthOpeningAccountCount, currentMonthFirstInvestCount, str(currentMonthProductTypeInvestAmount), str(currentMonthDeadlineInvestAmount)]


def group_month_count_main(dept, date, name):
    gmcm = GroupMonthCount(dept, date, name)
    the_date, the_dept, ent_name = gmcm.get_dept_date()
    if dept == '0':
        res = gmcm.company_count()
    currentMonthInvestAmount, lastMonthInvestAmount, investAmountLinkRelativeRatio, currentMonthInvestCount, currentMonthInvestPerformance, lastMonthInvestPerformance, investPerformanceLinkRelativeRatio, currentMonthReceivedPayment, currentMonthCashout, currentMonthCashoutProportion, currentMonthRecharge, currentMonthRechargeInvestProportion, currentMonthReceivedInvest, currentMonthReceivedInvestProportion, currentMonthNetCapital, fundsToBeCollected, precipitatedCapital, currentMonthOpeningAccountCount, currentMonthFirstInvestCount, currentMonthProductTypeInvestAmount, currentMonthDeadlineInvestAmount = res
    gmcm.object_close()
    comment = '销售月报，统计结果如下：' + '( 公司：%s, 部门：%s, 搜索日期：%s )' % (ent_name, the_dept, the_date) + '\n' \
        '当月投资总额：' + currentMonthInvestAmount + '\n' \
        '上月投资总额：' + lastMonthInvestAmount + '\n' \
        '投资总额环比增速：' + investAmountLinkRelativeRatio + '\n' \
        '当月投资笔数：' + currentMonthInvestCount + '\n' \
        '当月投资业绩：' + currentMonthInvestPerformance + '\n' \
        '上月投资业绩：' + lastMonthInvestPerformance + '\n' \
        '投资业绩环比增速：' + investPerformanceLinkRelativeRatio + '\n' \
        '当月还款总额：' + currentMonthReceivedPayment + '\n' \
        '当月提现总额：' + currentMonthCashout + '\n' \
        '当月提现占比：' + currentMonthCashoutProportion + '\n' \
        '当月充值总额：' + currentMonthRecharge + '\n' \
        '当月充值投资占比：' + currentMonthRechargeInvestProportion + '\n' \
        '当月还款投资：' + currentMonthReceivedInvest + '\n' \
        '当月还款投资占比：' + currentMonthReceivedInvestProportion + '\n' \
        '当月净资金流：' + currentMonthNetCapital + '\n' \
        '当月待收总额：' + fundsToBeCollected + '\n' \
        '当月沉淀总额：' + precipitatedCapital + '\n' \
        '当月开户客户数：' + currentMonthOpeningAccountCount + '\n' \
        '当月首投达标客户数：' + currentMonthFirstInvestCount + '\n' \
        '当月各产品类型投资总额：' + currentMonthProductTypeInvestAmount + '\n' \
        '当月各期限产品投资总额：' + currentMonthDeadlineInvestAmount

    print(comment)


if __name__ == '__main__':
    # group_month_count_main(部门, 日期, 公司)
    # group_month_count_main('0', '2019-12', 'nami')
    group_month_count_main('0', '2019-12', 'datang')
