#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : Li ZiHao
# @Time     : 2019/10/30 21:19
# @File     : opt_mysql.py

import pymysql


# ######## 开发环境圣玫租户库配置信息 #############
shengmei = {
    'host': 'rm-2ze1w9epp05wvc4j4po.mysql.rds.aliyuncs.com',
    'username': 'wbs_shengmei',
    'password': 'wbs_shengmei@123',
    'db': 'wbs_shengmei'
}

# ######## 测试环境纳觅租户库配置信息 #############
nami = {
    'host': 'rm-2ze3r058ks9ibbvnfqo.mysql.rds.aliyuncs.com',
    'username': 'wbs',
    'password': 'NTBnami201904!',
    'db': 'wbs-sec'
}

# ######## 测试环境大唐租户库配置信息 #############
datang = {
    'host': 'rm-2ze3r058ks9ibbvnfqo11.mysql.rds.aliyuncs.com',
    'username': 'wbs',
    'password': 'NTBnami201904!',
    'db': 'wbs-sec'
}

# ######## 测试环境大唐租户库配置信息 #############
qianle = {
    'host': 'rm-2ze3r058ks9ibbvnfqo11.mysql.rds.aliyuncs.com',
    'username': 'wbs',
    'password': 'NTBnami201904!',
    'db': 'wbs-sec'
}

# ######## 测试环境大唐租户库配置信息 #############
shanshang = {
    'host': 'rm-2ze3r058ks9ibbvnfqo11.mysql.rds.aliyuncs.com',
    'username': 'wbs',
    'password': 'NTBnami201904!',
    'db': 'wbs-sec'
}

# ##################################################


class Optsql:

    def conn_mysql(self, name):
        """
        创建数据库的链接对象，生成cursor对象
        """
        if name == 'shengmei':
            params = shengmei
        elif name == 'nami':
            params = nami
        elif name == 'datang':
            params = datang
        elif name == 'shanshang':
            params = shanshang
        else:
            params = qianle

        host, username, password, db = [params['host'], params['username'], params['password'], params['db']]

        conn = pymysql.Connect(
            host=host,
            port=3306,
            user=username,
            passwd=password,
            db=db,
            charset='utf8'
        )
        cur = conn.cursor()
        return cur

    def object_close(self, cur, conn):
        cur.close()
        conn.close()

    def execute_select(self, cur, sql):
        cur.execute(sql)
        return cur.fetchall()

    def update_table(self, cur, conn, sql):
        res = cur.execute(sql)
        conn.commit()
        return res


if __name__ == '__main__':
    ops = Optsql()
    # cursor = ops.conn_sm_mysql()
    # select_sql = "SELECT fundsToBeCollected,precipitatedCapital FROM `data_statistics_day` WHERE DAY='2019-11-20' " \
    #              "AND deptCode='SHNMCW0001';"
    # res = ops.execute_select(cursor, select_sql)[0]
    # print(type(res[0]/10000))
    ops.conn_mysql('shengmei')
