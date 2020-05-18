#coding:utf-8
'''
作者：李子浩
内容：顾问云资源市场管理模块下的资源管理相关case集合
'''

from UI.base_case import BaseUITestCase
from ...pages.resource_market_pages.resource_management_pages import ResourceManagementPages

class ResourceManagementTests(BaseUITestCase):
    def setUp(self):
        self.resource_management = ResourceManagementPages(self.browser)

    def tests_a_add_resource(self):
        self.assertEqual(self.resource_management.do_add_resource(), self.resource_management.add_title)

    def tests_b_update_resource(self):
        self.assertEqual(self.resource_management.do_update_resource(), self.resource_management.update_title)

    def tests_c_query_resource(self):
        self.assertEqual(self.resource_management.do_query_resource(), self.resource_management.update_title)

    def tests_d_delete_resource(self):
        self.assertEqual(self.resource_management.do_delete_resource(), u'删除成功！')


