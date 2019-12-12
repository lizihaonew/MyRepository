#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : Li ZiHao
# @Time     : 2019/10/30 21:19
# @File     : opt_group_mysql.py

import pymysql
import config


class Optsql:
    ent_id = config.ent_id
    ent_name = config.ent_name

    def conn_mysql(self, name):
        """
        创建数据库的链接对象，生成cursor对象
        """
        if name == 'shengmei':
            params = config.shengmei
        elif name == 'nami':
            params = config.nami
        elif name == 'datang':
            params = config.datang
        else:
            params = config.qianle

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
        return [cur, conn]

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
