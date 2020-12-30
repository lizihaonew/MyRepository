#coding:utf-8

'''
作者：李子浩
内容：顾问云类别管理资讯相关二级类别测试case
'''

from UI.base_case import BaseUITestCase
from ...pages.resource_market_pages.information_type_pages import InformationTypePages

class InformationTypeTests(BaseUITestCase):

    def setUp(self):
        self.type_page = InformationTypePages(self.browser)
        self.type_page.getting_type_list()

    def tests_a_add_type(self):
        self.assertEqual(self.type_page.add_type_do(), 'AutoTestAddInformationLZH999')

    def tests_b_update_type(self):
        self.assertEqual(self.type_page.update_type_do(), 'AutoTestUpdateInformationLZH998')

    def tests_c_delete_type(self):
        self.assertNotEqual(self.type_page.delete_type_do(), 'AutoTestAddInformationLZH999' or 'AutoTestUpdateInformationLZH998')
