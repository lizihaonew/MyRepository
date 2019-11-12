#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : Li ZiHao
# @Time     : 2019/10/30 21:19
# @File     : opt_mysql.py

import pymysql


# ######## 配置信息 #############

host = 'rm-2ze3r058ks9ibbvnfqo.mysql.rds.aliyuncs.com'
username = 'wbs'
password = 'NTBnami201904!'
db = 'wbs-sec'

# ###############################


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

    def update_table(self, sql):
        res = cur.execute(sql)
        # print("update successful!!!")
        conn.commit()
        return res


if __name__ == '__main__':
    ops = Optsql()
    cursor = ops.conn_mysql()
    select_sql = 'SELECT * FROM `wbs_employee` WHERE mobile = "13666666661";'
    update_sql = "UPDATE `ns_order` SET trans_time = '2019-11-03 15:11:12' WHERE trans_time LIKE '2019-11-01%';"
    # res = ops.execute_select(cur, select_sql)
    # print(len(res))
    ops.update_table(update_sql)