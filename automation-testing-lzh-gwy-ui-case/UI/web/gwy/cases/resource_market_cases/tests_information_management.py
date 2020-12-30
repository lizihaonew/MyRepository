#coding:utf-8
'''
作者：李子浩
内容：顾问云资源市场管理模块下资讯管理相关case
'''

from UI.base_case import BaseUITestCase
from ...pages.resource_market_pages.information_management_pages import InformationPages


class InformationManagementTest(BaseUITestCase):
    def setUp(self):
        self.information_management = InformationPages(self.browser)

    def tests_a_add_information(self):
        self.assertEqual(self.information_management.do_add_information(), self.information_management.add_name)

    def tests_b_update_information(self):
        self.assertEqual(self.information_management.do_update_information(), self.information_management.update_name)

    def tests_c_select_information(self):
        self.assertEqual(self.information_management.do_select_information(), self.information_management.update_name)

    def tests_d_delete_information(self):
        self.assertEqual(self.information_management.do_delete_information(), u'删除成功！')