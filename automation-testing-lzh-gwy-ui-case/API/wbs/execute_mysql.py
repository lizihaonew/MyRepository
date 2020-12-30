#coding:utf-8

import MySQLdb
from API import config

class ExecuteMysql(object):
    '''
    用于执行mysql简单的增删改差的sql语句
    用法是导入该类，调用类中的方法，参数是需要执行的sql语句；
    '''

    def execute_add_sql(self, sql):
        '''
        增
        :param sql:
        :return: None
        '''
        self.sql = sql
        conn = MySQLdb.connect(
            host=config.host,
            port=config.port,
            user=config.user,
            passwd=config.passwd,
            db=config.db
        )
        cur = conn.cursor()
        cur.execute(self.sql)
        cur.close()
        conn.commit()
        conn.close()


    def execute_delete_sql(self, sql):
        '''
        删
        :param sql:
        :return: None
        '''
        self.sql = sql
        conn = MySQLdb.connect(
            host=config.host,
            port=config.port,
            user=config.user,
            passwd=config.passwd,
            db=config.db
        )
        cur = conn.cursor()
        cur.execute(self.sql)
        cur.close()
        conn.commit()
        conn.close()

    def execute_update_sql(self, sql):
        '''
        改
        :param sql:
        :return: None
        '''
        self.sql = sql
        conn = MySQLdb.connect(
            host=config.host,
            port=config.port,
            user=config.user,
            passwd=config.passwd,
            db=config.db
        )
        cur = conn.cursor()
        cur.execute(self.sql)
        cur.close()
        conn.commit()
        conn.close()

    def execute_select_sql(self, sql):
        '''
        查
        :param sql:
        :return: 查询结果的list
        '''
        self.sql = sql
        conn = MySQLdb.connect(
            host=config.host,
            port=config.port,
            user=config.user,
            passwd=config.passwd,
            db=config.db
        )
        result = []
        cur = conn.cursor()
        cur.execute(self.sql)
        for i in cur.fetchall():
            result.append(i)

        cur.close()
        conn.close()
        return result



if __name__ == '__main__':
    # ExecuteMysql().execute_delete_sql('delete from emp_transition where empId = "322"')

    result = ExecuteMysql().execute_select_sql('SELECT * FROM emp_transition;')
    print result