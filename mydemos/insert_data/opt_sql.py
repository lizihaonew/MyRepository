#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : Li ZiHao
# @Time     : 2019/12/24 19:57
# @File     : opt_mysql.py


import pymysql


# #######################

host = 'rm-2ze1w9epp05wvc4j4po.mysql.rds.aliyuncs.com'
username = 'private'
password = '1qaz@WSX'
db = 'wbs_pri'

# #######################


class OptMysql(object):
    def __init__(self):
        conn = pymysql.Connect(
            host=host,
            port=3306,
            user=username,
            passwd=password,
            db=db,
            charset='utf8'
        )
        cur = conn.cursor()
        self.conn = conn
        self.cur = cur

    def object_close(self):
        self.cur.close()
        self.conn.close()

    def execute_select(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchall()

    def update_table(self, sql):
        res = self.cur.execute(sql)
        self.conn.commit()
        return res

    def insert_table(self, sql):
        self.conn.ping(reconnect=True)  # 若mysql连接失败就重连
        self.cur.execute(sql)
        self.conn.commit()


if __name__ == '__main__':
    ops = OptMysql()
    select_sql = "SELECT * FROM `ns_order` WHERE ent_id = 888 AND id = 1;"
    res = ops.execute_select(select_sql)[0]
    print(res)
