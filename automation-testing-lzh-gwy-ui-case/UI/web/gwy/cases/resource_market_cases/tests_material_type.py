#coding:utf-8
'''
作者：李子浩
内容：顾问云资源市场类别管理素材二级类别相关case
'''

from UI.base_case import BaseUITestCase
from ...pages.resource_market_pages.material_type_pages import MaterialTypePages

class ResourceTypeTests(BaseUITestCase):
    def setUp(self):
        self.material_type = MaterialTypePages(self.browser)
        self.material_type.getting_type_page()

    def tests_a_add_type(self):
        self.assertEqual(self.material_type.add_type_do(), 'AutoTestAddMaterialLZH999')

    def tests_b_update_type(self):
        self.assertEqual(self.material_type.update_type_do(), 'AutoTestUpdateMaterialLZH998')

    def tests_c_delete_type(self):
        self.assertNotEqual(self.material_type.delete_type_do(), 'AutoTestAddMaterialLZH999' or 'AutoTestUpdateMaterialLZH998')

