#coding:utf-8
'''
作者：李子浩
内容：顾问云资源市场管理模块下资源管理相关case
'''

from UI.base_case import BaseUITestCase
from ...pages.resource_market_pages.class_management_pages import ClassManagementPages

class ClassManagementTest(BaseUITestCase):
    def setUp(self):
        self.class_management = ClassManagementPages(self.browser)

    def tests_a_add_class(self):
        self.assertEqual(self.class_management.do_add_class(), self.class_management.add_title)

    def tests_b_detail_class(self):
        self.assertEqual(self.class_management.do_detail_class(), self.class_management.add_title)

    def tests_c_update_class(self):
        self.assertEqual(self.class_management.do_update_class(), self.class_management.update_title)

    def tests_d_query_class(self):
        self.assertEqual(self.class_management.do_query_class(), self.class_management.update_title)

    def tests_e_delete_class(self):
        self.assertEqual(self.class_management.do_delete_class(), u'删除成功！')