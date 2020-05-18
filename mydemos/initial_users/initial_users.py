#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Li Zihao
# @Time    : 2020/4/24 11:23
# @File    : initial_users.py

'''
将测试环境中已经存在的用户的用户数据清空，使得该用户成为当当的新用户；
只是删除了用户数据，该用户的其他业务数据还会保留，比如步数赚钱的数据，但重新登录会生成新的custid；
脚本基于python3
依赖pymysql、pymssql
'''

import pymysql
import pymssql

######################
mysql45 = {
    'server': 'mysql',
    'host': '10.255.208.45',
    'port': 8888,
    'user': 'ddim',
    'password': '12348765',
    'db': 'mobile_activity'
}
mysql22 = {
    'server': 'mysql',
    'host': '10.255.255.22',
    'port': 3306,
    'user': 'writeuser',
    'password': 'ddbackend',
    'db': 'mobile'
}
mysql78 = {
    'server': 'mysql',
    'host': '10.255.254.78',
    'port': 3306,
    'user': 'writeuser',
    'password': 'ddbackend',
    'db': ''
}
sqlserver195 = {
    'server': 'sqlserver',
    'host': '10.255.254.195',
    'user': 'writeuser',
    'password': 'ddbackend',
    'db': 'customer'
}
######################


class OpSql(object):
    def __init__(self, param):
        if param['server'] == 'mysql':
            self.conn = pymysql.connect(
                host=param['host'],
                port=param['port'],
                user=param['user'],
                password=param['password'],
                database=param['db'],
                charset='utf8'
            )
        elif param['server'] == 'sqlserver':
            self.conn = pymssql.connect(
                host=param['host'],
                user=param['user'],
                password=param['password'],
                database=param['db'],
                charset='utf8'
            )
        self.cursor = self.conn.cursor()

    def op_select(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def op_insupddel(self, sql):
        res = self.cursor.execute(sql)
        self.conn.commit()
        if res:
            return res
        else:
            return '0'

    def op_close(self):
        self.cursor.close()
        self.conn.close()


def op_mysql45(custid):
    opsql = OpSql(mysql45)

    table_list = ['tb_stepearnmoney_step_detail',  'tb_stepearnmoney_step_change_cheese', \
                  'tb_stepearnmoney_task_detail', 'tb_stepearnmoney_user_info', 'tb_stepearnmoney_wx_step_count',\
                  'tb_stepearnmoney_user_message', 'tb_stepearnmoney_wake_help_log']
    table_list.append('tb_stepearnmoney_help_list_' + str(int(custid) % 10))
    for table in table_list:
        res = opsql.op_insupddel("DELETE FROM {0} WHERE cust_id = {1};".format(table, custid))
        print('45库，{0}表删除成功{1}条数据！！'.format(table, res))
    opsql.op_close()


def op_mysql22(custid):
    opsql = OpSql(mysql22)
    res = opsql.op_insupddel("DELETE FROM `mdd_sessions_common` WHERE cust_id = %s;" % custid)
    print('22库，mdd_sessions_common表删除成功%s条数据！！' % res)
    opsql.op_close()


def op_mysql78(custid):
    db = int(custid) % 16
    mysql78['db'] = 'customer_' + str(db)
    opsql = OpSql(mysql78)
    table_list = ['customer', 'customer_detail', 'customer_third', 'customer_third_wechat', \
                  'customer_third_wechat_openid', 'customer_third_qq_openid']
    for table in table_list:
        res = opsql.op_insupddel("DELETE FROM {0} WHERE cust_id = {1};".format(table, custid))
        print('78库，{0}表删除成功{1}条数据！！'.format(table, res))
    opsql.op_close()


def op_sqlserver195(custid):
    opsql = OpSql(sqlserver195)
    table_list = ['Customers', 'share_sign_link', 'share_sign_weixin', 'customers_wechat_plat', 'customer_third_qq_openid']
    for table in table_list:
        if table == 'customers_wechat_plat':
            sql = "select union_id from share_sign_weixin where custid=%s;" % custid
            union_id = opsql.op_select(sql)
            if union_id:
                res = opsql.op_insupddel("DELETE FROM {0} WHERE wx_union_id = {1};".format(table, union_id))
                print('195库，{0}表删除成功{1}条数据！！'.format(table, res))
        elif table == 'customer_third_qq_openid':
            res = opsql.op_insupddel("DELETE FROM {0} WHERE cust_id = {1};".format(table, custid))
            print('195库，{0}表删除成功{1}条数据！！'.format(table, res))
        else:
            sql = "DELETE FROM {0} WHERE custid = {1};".format(table, custid)
            res = opsql.op_insupddel(sql)
            print('195库，{0}表删除成功{1}条数据！！'.format(table, res))

    opsql.op_close()


def main(custid):
    op_mysql45(custid)
    op_mysql22(custid)
    op_mysql78(custid)
    op_sqlserver195(custid)


if __name__ == '__main__':
    # main('720006619')
    custid = input('请输入custid：')
    print('你的custid：'+custid)
    main(custid)
    print('操作完成！！')



