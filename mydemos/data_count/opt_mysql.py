#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : Li ZiHao
# @Time     : 2019/10/30 21:19
# @File     : opt_mysql.py

import pymysql

######### 配置信息 #############
host = 'rm-2ze1w9epp05wvc4j4po.mysql.rds.aliyuncs.com'
username = 'private'
password = '1qaz@WSX'
db = 'wbs_pri'
new_entId = '888'
################################


class Optsql:
    def conn_mysql(self):
        """
        创建数据库的链接对象，生成cursor对象
        """
        global conn
        conn = pymysql.Connect(
            host=host,
            port=3306,
            user=username,
            passwd=password,
            db=db,
            charset='utf8'
        )

        global cur
        cur = conn.cursor()
        return cur

    def object_close(self):
        cur.close()
        conn.close()

    # def execute_select(self, sql):
    #     cur = self.conn_mysql()
    #     cur.execute(sql)
    #     self.object_close(cur)
    #     return cur.fetchall()

    def execute_select(self, cur, sql):
        # cur = self.conn_mysql()
        cur.execute(sql)
        # self.object_close(cur)
        return cur.fetchall()

if __name__ == '__main__':
    ops = Optsql()
    res = ops.execute_select('SELECT * FROM `wbs_employee` WHERE mobile = "13666666661";')
    print(len(res))