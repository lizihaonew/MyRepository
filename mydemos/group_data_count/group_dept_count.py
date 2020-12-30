#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : Li ZiHao
# @Time     : 2019/11/28 21:03
# @File     : group_dept_count.py

import datetime
import time
from opt_group_mysql import Optsql


class GroupDeptCount(Optsql):
    def __init__(self, dept, asset, name):
        self.dept = dept
        self.asset = asset
        self.name = name
        if self.asset == 0:
            self.asset_sql = ''
        else:
            self.asset_sql = 'and assetId = %s' % str(self.asset)
        self.cur, self.conn = self.conn_mysql("shengmei")
        self.ent_cur, self.ent_conn = self.conn_mysql(self.name)
        date_today = datetime.date.today()
        self.today = str(date_today)
        self.yesterday = str(date_today - datetime.timedelta(days=1))
        self.current_month = time.strftime('%Y-%m')

    def exchange_None(self, para):
        if para:
            return para
        else:
            return 0

    def object_close(self):
        super(GroupDeptCount, self).object_close(self.cur, self.conn)

    def dept_asset_name(self):
        ''' 获取部门名称和资产端名称 '''
        if self.asset == 0:
            asset_name = '全部'
        elif self.asset == 1:
            asset_name = '汇盈金服'
        elif self.asset == 2:
            asset_name = '汇晶社'
        else:
            asset_name = '恒普金融'

        if self.dept == '0':
            dept_name = '公司快报'
        else:
            dept_name_sql = "SELECT NAME FROM `wbs_department` WHERE CODE = '{0}';".format(self.dept)
            dept_name = self.execute_select(self.cur,dept_name_sql)[0][0]
        ent_name = self.ent_name[self.name]
        return [dept_name, asset_name, ent_name]

    def company_count(self):
        if self.asset == 0:
            _asset_sql = " AND assetId IS NULL"
        else:
            _asset_sql = ' AND assetId = %s' % str(self.asset)
        sum_sql = "SELECT SUM(todayInvestAmount), SUM(yesterdayInvestAmount), SUM(yesterdayInvestPerformance), " \
                  "SUM(yesterdayInvestCount), SUM(todayInvestCount), SUM(currentMonthReceivedPayment), SUM(currentMonthUnreceivedPayment)," \
                  " SUM(currentMonthCashout), SUM(todayCashout), SUM(yesterdayCashout), SUM(currentMonthRecharge), SUM(todayRecharge), " \
                  "SUM(yesterdayRecharge), SUM(todayNetCapital), SUM(yesterdayNetCapital), SUM(fundsToBeCollected), SUM(precipitatedCapital), " \
                  "SUM(todayOpeningAccountCount), SUM(yesterdayOpeningAccountCount), SUM(currentMonthFirstInvestCount), " \
                  "SUM(todayFirstInvestCount) FROM `data_statistics` WHERE entId='{0}' AND deptLevel=1{1};".format(self.ent_id[self.name], _asset_sql)
        res = self.execute_select(self.cur, sum_sql)[0]
        todayInvestAmount = str(res[0])
        yesterdayInvestAmount = str(res[1])
        yesterdayInvestPerformance = str(res[2])
        yesterdayInvestCount = str(res[3])
        todayInvestCount = str(res[4])
        currentMonthReceivedPayment = str(res[5])
        currentMonthUnreceivedPayment = str(res[6])
        currentMonthCashout = str(res[7])
        todayCashout = str(res[8])
        yesterdayCashout = str(res[9])
        currentMonthRecharge = str(res[10])
        todayRecharge = str(res[11])
        yesterdayRecharge = str(res[12])
        todayNetCapital = str(res[13])
        yesterdayNetCapital = str(res[14])
        fundsToBeCollected = str(res[15])
        precipitatedCapital = str(res[16])
        todayOpeningAccountCount = str(res[17])
        yesterdayOpeningAccountCount = str(res[18])
        currentMonthFirstInvestCount = str(res[19])
        todayFirstInvestCount = str(res[20])

        if self.asset == 0:
            _asset_sql1 = ""
        else:
            _asset_sql1 = ' AND asset_id = %s' % str(self.asset)

        if self.asset == 0:
            exit_amount_today_sql = "SELECT SUM(actual_exit_amount) FROM `wbs_received_payment` WHERE Convert(actual_exit_time,CHAR(20)) " \
                                    "LIKE '{0}%' AND STATUS = 2;".format(self.today)
            exit_amount_yesterday_sql = "SELECT SUM(actual_exit_amount) FROM `wbs_received_payment` WHERE Convert(actual_exit_time,CHAR(20)) " \
                                        "LIKE '{0}%' AND STATUS = 2;".format(self.yesterday)
        else:
            exit_amount_today_sql = "SELECT SUM(actual_exit_amount) FROM `wbs_received_payment` WHERE Convert(actual_exit_time,CHAR(20)) " \
                                "LIKE '{0}%' AND STATUS = 2 AND order_no IN " \
                                "(SELECT order_no FROM `ns_order` WHERE 1=1 {2});".format(self.today, self.dept, _asset_sql1)
            exit_amount_yesterday_sql = "SELECT SUM(actual_exit_amount) FROM `wbs_received_payment` WHERE Convert(actual_exit_time,CHAR(20)) " \
                                "LIKE '{0}%' AND STATUS = 2 AND order_no IN " \
                                "(SELECT order_no FROM `ns_order` WHERE 1=1 {2});".format(self.yesterday, self.dept, _asset_sql1)
        exit_amount_today = self.exchange_None(self.execute_select(self.ent_cur, exit_amount_today_sql)[0][0])
        exit_amount_yesterday = self.exchange_None(self.execute_select(self.ent_cur, exit_amount_yesterday_sql)[0][0])
        if exit_amount_today == 0:
            todayCashoutProportion = '0'
        else:
            todayCashoutProportion = str('%.4f%%' % eval(todayCashout+'/'+str(exit_amount_today/10000) + '*100'))

        if exit_amount_yesterday == 0:
            yesterdayCashoutProportion = '0'
        else:
            yesterdayCashoutProportion = str('%.4f%%' % eval(yesterdayCashout+'/'+str(exit_amount_yesterday/10000) + '*100'))

        if todayInvestAmount == '0.0000':
            todayRechargeInvestProportion = '0'
        else:
            todayRechargeInvestProportion = str('%.4f%%' % eval(todayRecharge+'/'+todayInvestAmount + '*100'))

        todayReceivedInvest = str(eval(todayInvestAmount+'-'+todayRecharge))

        if todayInvestAmount == '0.0000':
            todayReceivedInvestProportion = '0'
        else:
            todayReceivedInvestProportion = str('%.4f%%' % eval(todayReceivedInvest+'/'+todayInvestAmount + '*100'))

        type_ids_sql = "SELECT DISTINCT product_type FROM `ns_order` WHERE trans_time LIKE '{0}%';".format(self.today)
        type_ids_today = [id[0] for id in self.execute_select(self.ent_cur, type_ids_sql)]
        todayProductTypeInvestAmount = []
        for id in type_ids_today:
            product_type_name_sql = "SELECT product_type_name FROM `ns_product_type` WHERE id=%d;" % id
            invest_amount_today_sql = "SELECT SUM(trans_amount) FROM `ns_order` WHERE product_type={0} AND trans_time LIKE" \
                                      " '{1}%'{3};".format(id, self.today, self.dept, _asset_sql1)
            product_type_name = self.execute_select(self.ent_cur, product_type_name_sql)[0][0]
            product_type_invest_amount = self.exchange_None(
                self.execute_select(self.ent_cur, invest_amount_today_sql)[0][0])
            if not product_type_invest_amount:
                continue
            todayProductTypeInvestAmount.append(
                (product_type_name + ':%s' % str(id), '%.4f' % (product_type_invest_amount / 10000)))

        deadline_units_sql = "SELECT DISTINCT deadline_unit FROM `ns_order` WHERE trans_time LIKE '{0}%';".format(self.today)
        deadline_nums_sql = "SELECT DISTINCT deadline_num FROM `ns_order` WHERE trans_time LIKE '{0}%';".format(self.today)
        deadline_units_today = [id[0] for id in self.execute_select(self.ent_cur, deadline_units_sql)]
        deadline_nums_today = [id[0] for id in self.execute_select(self.ent_cur, deadline_nums_sql)]
        if deadline_units_today and deadline_nums_today:
            todayDeadlineInvestAmount = []
            for unit in deadline_units_today:
                if unit == 1:
                    unit_name = '天'
                elif unit == 2:
                    unit_name = '月'
                else:
                    unit_name = '年'
                for num in deadline_nums_today:
                    invest_amount_today_sql = "SELECT SUM(trans_amount) FROM `ns_order` WHERE deadline_unit={0} AND trans_time LIKE" \
                                              " '{1}%' AND deadline_num={4}{3};".format(unit, self.today, self.dept, _asset_sql1, num)
                    deadline_name = '{0}{1}'.format(str(num), unit_name)
                    deadline_invest_amount = self.exchange_None(self.execute_select(self.ent_cur, invest_amount_today_sql)[0][0])
                    if not deadline_invest_amount:
                        continue
                    todayDeadlineInvestAmount.append(deadline_name + ': %.4f' % (deadline_invest_amount / 10000))
        else:
            todayDeadlineInvestAmount = []
        return [todayInvestAmount, yesterdayInvestAmount, yesterdayInvestPerformance, yesterdayInvestCount, todayInvestCount, currentMonthReceivedPayment, currentMonthUnreceivedPayment, currentMonthCashout, todayCashout, yesterdayCashout, todayCashoutProportion, yesterdayCashoutProportion, currentMonthRecharge, todayRecharge, yesterdayRecharge, todayRechargeInvestProportion, todayReceivedInvest, todayReceivedInvestProportion, todayNetCapital, yesterdayNetCapital, fundsToBeCollected, precipitatedCapital, todayOpeningAccountCount, yesterdayOpeningAccountCount, currentMonthFirstInvestCount, todayFirstInvestCount, str(todayProductTypeInvestAmount), str(todayDeadlineInvestAmount)]


def group_dept_count_main(dept, asset, name):
    gdcm = GroupDeptCount(dept, asset, name)
    dept_name, asset_name, ent_name = gdcm.dept_asset_name()
    if dept == '0':
        res = gdcm.company_count()
    todayInvestAmount, yesterdayInvestAmount, yesterdayInvestPerformance, yesterdayInvestCount, todayInvestCount, currentMonthReceivedPayment, currentMonthUnreceivedPayment, currentMonthCashout, todayCashout, yesterdayCashout, todayCashoutProportion, yesterdayCashoutProportion, currentMonthRecharge, todayRecharge, yesterdayRecharge, todayRechargeInvestProportion, todayReceivedInvest, todayReceivedInvestProportion, todayNetCapital, yesterdayNetCapital, fundsToBeCollected, precipitatedCapital, todayOpeningAccountCount, yesterdayOpeningAccountCount, currentMonthFirstInvestCount, todayFirstInvestCount, todayProductTypeInvestAmount, todayDeadlineInvestAmount = res
    gdcm.object_close()
    comment = '销售快报 - 按照部门统计，统计结果如下：' + '(公司：%s, 部门：%s, 资产端：%s)' % (ent_name, dept_name, asset_name) + '\n' \
            '当日投资总额：' + todayInvestAmount + '\n'\
            '昨日投资总额：' + yesterdayInvestAmount + '\n'\
            '昨日投资业绩：' + yesterdayInvestPerformance + '\n'\
            '昨日投资笔数：' + yesterdayInvestCount + '\n' \
            '本日投资笔数：' + todayInvestCount + '\n' \
            '本月累计已还款：' + currentMonthReceivedPayment + '\n'\
            '本月累计待还款：' + currentMonthUnreceivedPayment + '\n'\
            '本月累计提现：' + currentMonthCashout + '\n'\
            '本日累计提现：' + todayCashout + '\n'\
            '昨日累计提现：' + yesterdayCashout + '\n'\
            '本日提现占比：' + todayCashoutProportion + '\n'\
            '昨日提现占比：' + yesterdayCashoutProportion + '\n'\
            '本月累计充值：' + currentMonthRecharge + '\n'\
            '本日累计充值：' + todayRecharge + '\n'\
            '昨日累计充值：' + yesterdayRecharge + '\n'\
            '本日充值投资占比：' + todayRechargeInvestProportion + '\n'\
            '本日还款投资：' + todayReceivedInvest + '\n'\
            '本日还款投资占比：' + todayReceivedInvestProportion + '\n'\
            '本日净资金流：' + todayNetCapital + '\n'\
            '昨日净资金流：' + yesterdayNetCapital + '\n'\
            '客户待收总额：' + fundsToBeCollected + '\n'\
            '客户沉淀总额：' + precipitatedCapital + '\n'\
            '本日累计开户数：' + todayOpeningAccountCount + '\n'\
            '昨日累计开户数：' + yesterdayOpeningAccountCount + '\n' \
            '本日累计首投达标客户数：' + todayFirstInvestCount + '\n' \
            '本月累计首投达标客户数：' + currentMonthFirstInvestCount + '\n' \
            '本日各产品类型投资总额：' + todayProductTypeInvestAmount + '\n'\
            '当日各期限产品投资总额：' + todayDeadlineInvestAmount
    print(comment)


if __name__ == '__main__':
    # group_dept_count_main(部门, 资产端, 公司)
    group_dept_count_main('0', 0, 'nami')
