#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : Li ZiHao
# @Time     : 2019/12/24 20:12
# @File     : order_payment_insert.py

from opt_sql import OptMysql
from threading_build import go_thread
import random
import threading
import time

num_thread_per = 8000
tag = 'AUTOINSERT3119'
lock = threading.Lock()


class OrderPaymentInsert(OptMysql):

    def do_order_payment_insert(self, num, num2):
        assert_id = random.choice(['1', '2', '3'])
        fa_id = random.choice(['2459', '2656', '2627'])
        fa_info = {
            '2459': ['新增员工008', '13666666668', 'SHNMCW0003'],
            '2656': ['新增员工001', '13999999991', 'SHNMCW00060001'],
            '2627': ['一级发财员工', '18711111111', 'SHNMZX0001']
        }
        order_no = tag + num + num2
        order_insert_sql = "INSERT INTO `ns_order` (`ent_id`, `asset_id`, `asset_customer_id`, `cus_id`, `cus_name`, " \
                     "`cus_phone`, `cus_paperwork_type`, `cus_paperwork_no`, `emp_no`, `fa_id`, `fa_name`, " \
                     "`fa_phone`, `product_no`, `is_alone_catery`, `product_type`, `product_sort`, `category`, " \
                     "`product_name`, `order_no`, `order_status`, `trans_amount`, `trans_time`, `deadline_unit`, " \
                     "`deadline_num`, `contract_number`, `insurer`, `insured_name`, `insured_phone`, " \
                     "`insured_paperwork_type`, `order_comments`, `insured_paperwork_no`, `recognizee_name`, " \
                     "`recognizee_paperwork_type`, `recognizee_paperwork_no`, `insurance_police`, `interest_time`, " \
                     "`maturity_time`, `arrival_time`, `reference_income`, `insurance_effect_time`, " \
                     "`insurance_invalid_time`, `dept_code`, `create_by`, `create_time`, `update_by`, `update_time`, " \
                     "`first_invest`) VALUES('888','{0}','5659','238','常平','13555555807','1',NULL,NULL,'{1}'," \
                     "'{2}','{3}','HJH201606120001','2','3','10','7','应急计划','{5}'" \
                     ",'2','1000.0000','2019-12-12 09:54:56','2','3',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL," \
                     "NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'{4}','admin','2019-06-12 10:00:00'," \
                     "'admin','2019-12-12 10:00:00','0');".format(assert_id, fa_id, fa_info[fa_id][0], fa_info[fa_id][1], fa_info[fa_id][2], order_no)
        payment_status = random.choice(['1', '2'])
        payment_insert_sql = "INSERT INTO `wbs_received_payment` (`id`, `order_no`, `product_name`, `product_category`, " \
                     "`product_source`, `product_no`, `expected_exit_time`, `actual_exit_time`, `expected_repay`, " \
                     "`actual_repay`, `expected_exit_capital`, `actual_exit_capital`, `expected_exit_amount`, " \
                     "`actual_exit_amount`, `period`, `asset_cus_id`, `customer_id`, `mobile`, `document_type`, " \
                     "`document_no`, `status`, `update_by`, `create_by`, `update_time`, `create_time`, `fa_id`, " \
                     "`dept_code`, `name`, `product_id`, `refundOrderNumber`) VALUES('{1}'," \
                     "'{0}',NULL,NULL,'1','HTZ17100620','2019-12-24 00:00:00','2019-12-25 00:00:00'," \
                     "'50.00','30.00','120.00','200.00','50.00','300.00','21','5659','238','13555555807','1',NULL,'1',NULL,NULL," \
                     "NULL,NULL,{3},'{4}',NULL,NULL,'{1}');".format(order_no, (order_no + '1'), payment_status, fa_id, fa_info[fa_id][2])

        try:
            lock.acquire()
            self.insert_table(order_insert_sql)
            lock.release()

            lock.acquire()
            self.insert_table(payment_insert_sql)
            lock.release()

        except Exception as e:
            print(e)
            print("order_insert_sql" + order_insert_sql)
            print("payment_insert_sql" + payment_insert_sql)
            raise NameError('SQL 执行错误！！！')

    def order_insert_loop(self, num):
        success_num = 0
        for index in range(num_thread_per):
            try:
                self.do_order_payment_insert(str(num), str(index))
            except Exception as e:
                print(e)
                break
            else:
                success_num += 1
        print('线程%s完成，完成总数：%s' % (num, success_num))


def main():
    start_local_time = time.strftime('%y-%m-%d %H:%M:%S')
    print('开始时间：' + start_local_time)
    print('操作中》》》》》')
    opi = OrderPaymentInsert()
    go_thread(opi.order_insert_loop)
    opi.object_close()
    end_local_time = time.strftime('%y-%m-%d %H:%M:%S')
    print('结束时间：' + end_local_time)


if __name__ == '__main__':
    main()