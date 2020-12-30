# -*- coding: utf-8 -*-
from UI.base_case import BaseUITestCase
from UI.web.gwy.pages.resource_market_pages.finance_product_type_pages import FinanceProductTypePage
import time

class FinaceProductTypeTest(BaseUITestCase):

    def setUp(self):
        self.type_page = FinanceProductTypePage(self.browser)
        self.type_page.getting_type_page()


    def tests_a_add_type(self):
        self.assertEqual(self.type_page.add_type_do(), 'AutoTestAddFinanceProductLZH999')

    def tests_b_update_type(self):
        self.assertEqual(self.type_page.update_type_do(), 'AutoTestUpdateFinanceProductLZH998')

    def tests_c_delete_type(self):
        self.assertNotEqual(self.type_page.delete_type_do(), 'AutoTestUpdateFinanceProductLZH998' or 'AutoTestUpdateFinanceProductLZH998')