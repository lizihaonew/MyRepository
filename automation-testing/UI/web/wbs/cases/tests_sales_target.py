# -*- coding: utf-8 -*-
import random
from UI.base_case import BaseUITestCase
from ..pages.sales_target_page import SalesTargetPage


class SalesTargetTest(BaseUITestCase):

    def setUp(self):
        self.sales_target = SalesTargetPage(self.browser)
    #
    # def tests_add_position_sale_target(self):
    #     name_list1 = self.sales_target.add_position_sales_target()
    #     name_list2 = self.sales_target.position_sales_name_list()
    #     for name in name_list1:
    #         self.assertIn(name, name_list2)
    #
    # def tests_sales_target_save_by_position(self):
    #     sales_target1 = self.sales_target.set_sales_target_by_position()
    #     # 针对list进行从大到小排序（True），从小到大（False）
    #     sales_target1.sort(reverse=True)
    #     sales_target2 = self.sales_target.position_sales_target_list()
    #     self.assertListEqual(sales_target1, sales_target2)
    #
    # def tests_delete_position_sale_target(self):
    #     num1 = self.sales_target.position_sales_target_num()
    #     self.sales_target.delete_position_sales_target()
    #     num2 = self.sales_target.position_sales_target_num()
    #     self.assertEqual(num1-1, num2)

    # def tests_sales_target_save_by_department(self):
    #     sales_target1 = self.sales_target.set_sales_target_by_department()
    #     sales_target2 = self.sales_target.department_sales_target_list()
    #     self.assertEqual(sales_target1, sales_target2)

    def tests_sales_target_save_by_employee(self):
        phone = '18877777771'
        sales_target1 = self.sales_target.employee_sales_target_list(phone=phone)
        sales_target2 = self.sales_target.employee_sales_target_list_search(phone=phone)
        print 'sales_target1'
        print sales_target1
        print 'sales_target2'
        print sales_target2
        self.assertEqual(sales_target1, sales_target2)