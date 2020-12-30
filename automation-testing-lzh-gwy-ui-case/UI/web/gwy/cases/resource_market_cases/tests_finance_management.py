#coding:utf-8
'''
作者：李子浩
内容：顾问云资源市场金融产品管理相关测试cases
'''

from UI.base_case import BaseUITestCase
from ...pages.resource_market_pages.finance_management_pages import FinanceMangementPages

class FinanceManagementTest(BaseUITestCase):
    def setUp(self):
        self.finance_management = FinanceMangementPages(self.browser)

    def tests_a_add_product(self):
        self.assertEqual(self.finance_management.do_add_product(), self.finance_management.product_add_name)

    def tests_b_update_product(self):
        self.assertEqual(self.finance_management.do_unpublished_update(), self.finance_management.product_update_name1)

    def tests_c_publish_product(self):
        self.assertEqual(self.finance_management.do_publish(), self.finance_management.product_update_name1)

    def tests_d_published_update(self):
        self.assertEqual(self.finance_management.do_published_update(), self.finance_management.product_update_name2)

    def tests_e_product_detail(self):
        self.assertEqual(self.finance_management.do_product_detail(), self.finance_management.product_update_name2)

    def tests_f_revoke_publish(self):
        self.assertEqual(self.finance_management.do_revoke_publish(), self.finance_management.product_update_name2)

    def tests_g_product_delete(self):
        self.assertNotEqual(self.finance_management.do_product_delete(), self.finance_management.product_update_name2)