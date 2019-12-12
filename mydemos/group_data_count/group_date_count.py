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
        self.ent_cur, self.ent_conn = self.conn_mysql(self.name)
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

    def exchange_None(self, para):
        if para:
            return para
        else:
            return 0

    def object_close(self):
        super(GroupDateCount, self).object_close(self.cur, self.conn)

    def get_dept_date(self):
        the_date = self.date
        if self.dept == '0':
            the_dept = '查询整个公司'
        else:
            the_dept = self.execute_select(self.cur, "SELECT deptName FROM `data_statistics_day` WHERE deptCode='%s';" % self.dept)[0][0]
        return [the_date, the_dept]

    def company_count(self):
        company_count_sql = "SELECT SUM(todayInvestAmount), SUM(todayInvestCount), SUM(todayInvestPerformance), SUM(todayReceivedPayment)," \
                            " SUM(todayCashout), SUM(todayRecharge), SUM(todayReceivedInvest), SUM(todayNetCapital), SUM(fundsToBeCollected)," \
                            " SUM(precipitatedCapital), SUM(todayOpeningAccountCount), SUM(todayFirstInvestCount) FROM `data_statistics_day` " \
                            "WHERE  DAY = '{0}' AND entId = {1} AND deptLevel=1;".format(self.date, self.ent_id[self.name])
        company_count_res = self.execute_select(self.cur, company_count_sql)[0]
        todayInvestAmount, todayInvestCount, todayInvestPerformance, todayReceivedPayment, todayCashout, todayRecharge, todayReceivedInvest, todayNetCapital, fundsToBeCollected, precipitatedCapital, todayOpeningAccountCount, todayFirstInvestCount = [str(value) for value in company_count_res]
        # print([str(value) for value in company_count_res])

        if todayReceivedPayment == '0.0000':
            todayCashoutProportion = '0'
        else:
            todayCashoutProportion = str('%.2f%%' % eval("({0}/{1})*100".format(todayCashout, todayReceivedPayment)))

        if todayInvestAmount == '0.0000':
            todayRechargeInvestProportion = '0'
        else:
            todayRechargeInvestProportion = str('%.2f%%' % eval("({0}/{1})*100".format(todayRecharge, todayInvestAmount)))

        if todayInvestAmount == '0.0000':
            todayReceivedInvestProportion = '0'
        else:
            todayReceivedInvestProportion = str('%.2f%%' % eval("({0}/{1})*100".format(todayReceivedInvest, todayInvestAmount)))

        type_ids_sql = "SELECT DISTINCT product_type FROM `ns_order` WHERE trans_time LIKE '{0}%';".format(self.date)
        type_ids_today = [id[0] for id in self.execute_select(self.ent_cur, type_ids_sql)]
        todayProductTypeInvestAmount = []
        for id in type_ids_today:
            product_type_name_sql = "SELECT product_type_name FROM `ns_product_type` WHERE id=%d;" % id
            invest_amount_today_sql = "SELECT SUM(trans_amount) FROM `ns_order` WHERE product_type={0} AND trans_time LIKE" \
                                      " '{1}%';".format(id, self.date, self.dept)
            # print([product_type_name_sql,invest_amount_today_sql])
            product_type_name = self.execute_select(self.ent_cur, product_type_name_sql)[0][0]
            product_type_invest_amount = self.exchange_None(self.execute_select(self.ent_cur, invest_amount_today_sql)[0][0])
            if not product_type_invest_amount:
                continue
            todayProductTypeInvestAmount.append((product_type_name + ':', '%.4f' % (product_type_invest_amount / 10000)))

        deadline_units_sql = "SELECT DISTINCT deadline_unit FROM `ns_order` WHERE trans_time LIKE '{0}%';".format(self.date)
        deadline_nums_sql = "SELECT DISTINCT deadline_num FROM `ns_order` WHERE trans_time LIKE '{0}%';".format(self.date)
        deadline_units_today = [id[0] for id in self.execute_select(self.ent_cur, deadline_units_sql)]
        deadline_nums_today = [id[0] for id in self.execute_select(self.ent_cur, deadline_nums_sql)]
        # print(deadline_units_today,deadline_nums_today)
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
                                          " '{1}%' AND deadline_num={3};".format(unit, self.date, self.dept, num)
                deadline_name = '{0}{1}'.format(str(num), unit_name)
                deadline_invest_amount = self.exchange_None(self.execute_select(self.ent_cur, invest_amount_today_sql)[0][0])
                if not deadline_invest_amount:
                    continue
                todayDeadlineInvestAmount.append(deadline_name + ': %.4f' % (deadline_invest_amount / 10000))

        return [todayInvestAmount, todayInvestCount, todayInvestPerformance, todayReceivedPayment, todayCashout, todayCashoutProportion, todayRecharge, todayReceivedInvest, todayRechargeInvestProportion, todayReceivedInvestProportion, todayNetCapital, fundsToBeCollected, precipitatedCapital, todayOpeningAccountCount, todayFirstInvestCount, str(todayProductTypeInvestAmount), str(todayDeadlineInvestAmount)]


def group_date_count_main(dept, date, name):
    gdcm = GroupDateCount(dept, date, name)
    company_name = gdcm.ent_name[name]
    the_date, the_dept = gdcm.get_dept_date()
    company_count_res = gdcm.company_count()
    todayInvestAmount, todayInvestCount, todayInvestPerformance, todayReceivedPayment, todayCashout, todayCashoutProportion, todayRecharge, todayReceivedInvest, todayRechargeInvestProportion, todayReceivedInvestProportion, todayNetCapital, fundsToBeCollected, precipitatedCapital, todayOpeningAccountCount, todayFirstInvestCount, todayProductTypeInvestAmount, todayDeadlineInvestAmount = company_count_res

    gdcm.object_close()

    comment = '集团数据统计，销售日报，统计结果如下：' + '( 公司名称：%s, 部门：%s, 日期：%s )'%(company_name, the_dept, the_date) + '\n'\
        '当日投资总额：' + todayInvestAmount + '\n'\
        '当日投资笔数：' + todayInvestCount + '\n'\
        '当日投资业绩：' + todayInvestPerformance + '\n'\
        '当日还款总额：' + todayReceivedPayment + '\n'\
        '当日提现总额：' + todayCashout + '\n'\
        '当日提现占比：' + todayCashoutProportion + '\n'\
        '当日充值总额：' + todayRecharge + '\n'\
        '当日充值投资占比：' + todayRechargeInvestProportion + '\n'\
        '当日还款投资：' + todayReceivedInvest + '\n'\
        '当日还款投资占比：' + todayReceivedInvestProportion + '\n'\
        '当日净资金流：' + todayNetCapital + '\n'\
        '当日待收总额：' + fundsToBeCollected + '\n'\
        '当日沉淀总额：' + precipitatedCapital + '\n'\
        '当日开户客户数：' + todayOpeningAccountCount + '\n'\
        '当日首投达标客户数：' + todayFirstInvestCount + '\n'\
        '当日各产品类型投资总额：' + todayProductTypeInvestAmount + '\n' \
        '当月各期限产品投资总额：' + todayDeadlineInvestAmount

    print(comment)


if __name__ == '__main__':
    # group_date_count_main(部门, 日期, 公司)
    group_date_count_main('0', '2019-12-04', 'nami')
    # group_date_count_main('0', '2019-12-03', 'datang')





