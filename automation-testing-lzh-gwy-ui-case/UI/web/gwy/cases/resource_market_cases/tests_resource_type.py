#coding:utf-8
'''
作者：李子浩
内容：顾问云资源市场类别管理资源二级类别相关case
'''

from UI.base_case import BaseUITestCase
from ...pages.resource_market_pages.resource_type_pages import ResourceTypePages

class ResourceTypeTests(BaseUITestCase):
    def setUp(self):
        self.resource_type = ResourceTypePages(self.browser)
        self.resource_type.getting_type_page()

    def tests_a_add_type(self):
        self.assertEqual(self.resource_type.add_type_do(), 'AutoTestAddResourceLZH999')

    def tests_b_update_type(self):
        self.assertEqual(self.resource_type.update_type_do(), 'AutoTestUpdateResourceLZH998')

    def tests_c_delete_type(self):
        self.assertNotEqual(self.resource_type.delete_type_do(), 'AutoTestAddResourceLZH999' or 'AutoTestUpdateResourceLZH998')

