#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : Li ZiHao
# @Time     : 2019/12/25 11:27
# @File     : recharge_cashout_insert.py

from opt_sql import OptMysql
from threading_build import go_thread
import random
import threading
import time

num_thread_per = 13100
tag = 'AUTOINSERT006'
lock = threading.Lock()


class RechargeCashoutInsert(OptMysql):

    def do_recharge_cashout_insert(self, num, num2):
        assert_id = random.choice(['1', '2', '3'])
        fa_id = random.choice(['2459', '2656', '2627'])
        fa_info = {
            '2459': ['新增员工005', '13666666665', 'SHNMCW000600010001'],
            '2656': ['新增员工001', '13999999991', 'SHNMCW00060001'],
            '2627': ['一级发财员工', '18711111111', 'SHNMZX0001']
        }
        detail_no = tag + num + num2
        cashout_insert_sql = "INSERT INTO `ns_cashout_record` (`asset_customer_id`, `detail_no`, `customer_name`, " \
                     "`customer_mobile`, `advisor_id`, `advisor_name`, `advisor_mobile`, `dept_code`, `asset_id`, " \
                     "`operate_platform`, `invest_platform`, `user_name`, `bank`, `cashout_amount`, `service_charge`, " \
                     "`arrive_amount`, `cashout_time`, `cashout_way`, `type`, `status`, `create_time`, `update_time`)" \
                     " VALUES('0000','{0}','江娜','13969875569','{1}','{2}','{3}','{4}','{5}','2','江西银行'," \
                     "'hyjf875569','农业银行','100.00','1.00','99.00','2019-12-25 09:55:16'," \
                     "'主动提现',NULL,'3','2019-11-01 19:43:02','2019-07-11 19:43:21')" \
                     ";".format(detail_no, fa_id, fa_info[fa_id][0], fa_info[fa_id][1], fa_info[fa_id][2], assert_id)

        recharge_insert_sql = "INSERT INTO `ns_recharge_record` (`asset_customer_id`, `detail_no`, `customer_name`, " \
                              "`customer_mobile`, `advisor_id`, `advisor_name`, `advisor_mobile`, `dept_code`, " \
                              "`asset_id`, `operate_platform`, `invest_platform`, `user_name`, `bank`, `recharge_amount`," \
                              " `service_charge`, `arrive_amount`, `recharge_time`, `type`, `status`, `create_time`, `update_time`) " \
                              "VALUES('0000','{0}','常平','18909877890','{1}','{2}'," \
                              "'{3}','{4}','{5}','1','江西银行','hyjf090909','农业银行','200.00'," \
                              "'0.00','200.00','2019-12-25 00:00:00','网上充值','3','2019-07-04 15:11:12','2019-07-04 16:00:21')" \
                              ";".format(detail_no, fa_id, fa_info[fa_id][0], fa_info[fa_id][1], fa_info[fa_id][2], assert_id)

        try:
            lock.acquire()
            self.insert_table(cashout_insert_sql)
            lock.release()

            lock.acquire()
            self.insert_table(recharge_insert_sql)
            lock.release()

        except Exception as e:
            print(e)
            print("cashout_insert_sql" + cashout_insert_sql)
            print("recharge_insert_sql" + recharge_insert_sql)
            raise NameError('SQL 执行错误！！！')

    def insert_loop(self, num):
        success_num = 0
        for index in range(num_thread_per):
            try:
                self.do_recharge_cashout_insert(str(num), str(index))
            except Exception as e:
                print(e)
                break
            else:
                success_num += 1
        print('线程%s完成，完成总数：%s' % (num, success_num))


def main():
    local_time = time.strftime('%y-%m-%d %H:%M:%S')
    print('开始时间：' + local_time)
    print('操作中》》》》》')
    rci = RechargeCashoutInsert()
    go_thread(rci.insert_loop)
    rci.object_close()
    print('结束时间：' + local_time)


if __name__ == '__main__':
    main()
