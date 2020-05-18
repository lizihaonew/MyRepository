#coding:utf-8
'''
作者：李子浩
内容：顾问云资源市场类别管理培训课程二级类别相关case
'''

from UI.base_case import BaseUITestCase
from ...pages.resource_market_pages.class_type_pages import ClassTypePages

class ResourceTypeTests(BaseUITestCase):
    def setUp(self):
        self.class_type = ClassTypePages(self.browser)
        self.class_type.getting_type_page()

    def tests_a_add_type(self):
        self.assertEqual(self.class_type.add_type_do(), 'AutoTestAddClassLZH999')

    def tests_b_update_type(self):
        self.assertEqual(self.class_type.update_type_do(), 'AutoTestUpdateClassLZH998')

    def tests_c_delete_type(self):
        self.assertNotEqual(self.class_type.delete_type_do(), 'AutoTestAddClassLZH999' or 'AutoTestUpdateClassLZH998')

