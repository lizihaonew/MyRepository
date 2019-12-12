#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : Lizihao
# @Time     : 2018/11/7 22:52
# @File     : update_entId.py

"""
该脚本用于更新目标数据库中所有表的entId为指定的new_entId
当然有些表中没有这个字段，也有些表中是entId而有些表中是ent_id，这些都做了判断
后续如果还有别的entId的字段标识方式，就是设计表的开发人员脑袋有问题
使用前需要确保python3安装PyMySQL三方包，Python2安装MySQLdb，当然写法略有不同，本脚本以python3为准
修改变量数据，主要是数据库连接数据，还有需要替换成的entId
"""
# import MySQLdb
import pymysql

# ######## 测试环境纳觅租户库配置信息 #############
# host = 'rm-2ze3r058ks9ibbvnfqo.mysql.rds.aliyuncs.com'
# username = 'wbs'
# password = 'NTBnami201904!'
# db = 'wbs-sec'
# new_entId = '8001'
# ######## 测试环境大唐租户库配置信息 #############
host = 'rm-2zeqv910hn9004t41.mysql.rds.aliyuncs.com'
username = 'wbs'
password = 'NTB-datang201908'
db = 'wbs-test'
new_entId = '8002'
# ##################################################


def conn_mysql():
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

    cur = conn.cursor()
    return cur


def do_exchage(cur):
    """
    先获取到库中所有的表，遍历每张表查询每张表的至少一条数据，若表中没有数据则不需要更换ent_id
    若有返回数据，获取出表的所有字段，判断entId或者ent_id是否在其中，若存在执行update，记得需要commit
    """
    cur.execute('show tables;')
    tables = cur.fetchall()
    for obj in tables:
        table = obj[0]
        rows = cur.execute("select * from %s limit 0, 1;" % table)
        if rows:
            columns = [col[0] for col in cur.description]
            if "entId" in columns:
                res = cur.execute("update {0} set entId = {1};".format(table, new_entId))
                conn.commit()
                print(table + '\t' + str(res))
            elif "ent_id" in columns:
                res = cur.execute("update {0} set ent_id = {1};".format(table, new_entId))
                conn.commit()
                print(table + '\t' + str(res))


def object_close(cur):
    cur.close()
    conn.close()


def main():
    cur = conn_mysql()
    do_exchage(cur)
    object_close(cur)


if __name__ == '__main__':
    main()