#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : Li ZiHao
# @Time     : 2019/12/25 18:18
# @File     : account_insert.py

from opt_sql import OptMysql
from threading_build import go_thread
import random
import threading
import time

lock = threading.Lock()


class AccountInsert(OptMysql):

    def do_account_insert(self, num, num2):
        assert_id = random.choice(['1', '2', '3'])
        fa_id = random.choice(['2459', '2656', '2627'])
        fa_info = {
            '2459': ['新增员工005', '13666666665', 'SHNMCW000600010001'],
            '2656': ['新增员工001', '13999999991', 'SHNMCW00060001'],
            '2627': ['一级发财员工', '18711111111', 'SHNMZX0001']
        }
        asset_cus_id = '102' + num + num2
        name = '小花'+ asset_cus_id
        user_name = 'AUTO' + asset_cus_id
        mobile = '102' + (num+num2).zfill(8)

        stock_insert_sql = "INSERT INTO `wbs_stock_customer` (`asset_cus_id`, `asset`, `user_name`, " \
                             "`precipitated_capital`, `funds_to_be_collected`, `account_info`, `name`, `mobile`, " \
                             "`fa_id`, `fa_no`, `ent_id`, `deleted`, `document_no_md5`, `update_time`, `create_time`," \
                             " `update_by`, `create_by`, `platform_registration_time`, `platform_account_opening_time`" \
                             ", `bank_of_deposit`, `bank_card_number`, `bank_reserved_phone_number`, `document_no`," \
                             " `fa_name`, `dept_code`, `fa_mobile`, `bind_asset_cus_id`, `exception_type`, `open_fa_id`" \
                             ", `open_fa_dept_code`) VALUES('{0}','{1}','{2}','100.00','20.00',NULL,'{3}','{4}','{5}','0112233','888','1'," \
                             "'87a3afd142f9b7e03c8b1119f3a7d6e8',NULL,NULL,NULL,NULL,'2019-03-04 15:44:50'," \
                             "'2019-12-25 15:46:44','农业银行','6228483858994110318','18133059269',NULL" \
                             ",'{6}','{7}','{8}',NULL,NULL,NULL,NULL)" \
                             ";".format(asset_cus_id, assert_id, user_name, name, mobile, fa_id, fa_info[fa_id][0], fa_info[fa_id][2], fa_info[fa_id][1])

        account_insert_sql = "INSERT INTO `wbs_asset_cus_account` (`asset_cus_id`, `asset`, `cus_id`, " \
                             "`related_account`, `user_name`, `precipitated_capital`, `funds_to_be_collected`, " \
                             "`platform_registration_time`, `platform_account_opening_time`, `account_bind_time`, " \
                             "`account_bind_platform`, `authorized`, `account_info`, `update_by`, `create_by`, " \
                             "`update_time`, `create_time`) VALUES('{0}','{1}','{2}',NULL,'{3}'," \
                             "'100.00','20.00','2019-03-04 15:44:50','2019-12-25 15:46:44',NULL,NULL,'0',NULL,NULL,NULL," \
                             "'2019-11-02 18:19:52','2019-08-08 18:19:52');".format(asset_cus_id, assert_id, ('1' + asset_cus_id), user_name)
        sql_dict = {
            "stock_insert_sql": stock_insert_sql,
            "account_insert_sql": account_insert_sql
        }

        try:
            lock.acquire()
            self.insert_table(stock_insert_sql)
            lock.release()

            lock.acquire()
            self.insert_table(account_insert_sql)
            lock.release()
        except Exception as e:
            print(e)
        return sql_dict

    def insert_loop(self, num):
        success_num = 0
        res = None
        for index in range(3):
            try:
                res = self.do_account_insert(str(num), str(index))
            except Exception as e:
                print(e)
                print(res)
                break
            else:
                success_num += 1
        print('线程%s完成，完成总数：%s' % (num, success_num))


def main():
    local_time = time.strftime('%y-%m-%d %H:%M:%S')
    print('开始时间：' + local_time)
    print('操作中》》》》》')
    ai = AccountInsert()
    go_thread(ai.insert_loop)
    ai.object_close()
    print('结束时间：' + local_time)


if __name__ == '__main__':
    main()



