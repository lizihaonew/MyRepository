#coding:utf-8
'''
作者：李子浩
内容：顾问云资源市场管理模块下素材管理相关case
'''

from UI.base_case import BaseUITestCase
from ...pages.resource_market_pages.material_management_pages import MaterialManagementPages

class MaterialManagementTest(BaseUITestCase):
    def setUp(self):
        self.material_management = MaterialManagementPages(self.browser)

    def tests_a_add_material(self):
        self.assertEqual(self.material_management.do_add_material(), self.material_management.add_title)

    def tests_b_update_material(self):
        self.assertEqual(self.material_management.do_update_material(), self.material_management.update_title)

    def tests_c_query_material(self):
        self.assertEqual(self.material_management.do_query_material(), self.material_management.update_title)

    def tests_d_delete_material(self):
        self.assertEqual(self.material_management.do_delete_material(), u'删除成功！')