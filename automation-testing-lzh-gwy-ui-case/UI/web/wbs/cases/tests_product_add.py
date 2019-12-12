# -*- coding: utf-8 -*-
import random
from UI.base_case import BaseUITestCase
from ..pages.product_page import ProductListPage, ProductPropertyElements, ProductSearchElements


class ProductAddTest(BaseUITestCase):

    def setUp(self):
        self.product_add = ProductListPage(self.browser)

    def procuct_add_category(self, category):
        name1 = self.product_add.add_product(category)['name']
        name2 = self.product_add.select_product(name1)
        self.assertEqual(name1, name2)

    # 类固收
    def tests_product_add_category_p2p(self):
        self.procuct_add_category(1)

    # 信托
    def tests_product_add_category_trust(self):
        self.procuct_add_category(2)

    # 资管计划
    def tests_product_add_category_information_management_plan(self):
        self.procuct_add_category(3)

    # 有限合伙
    def tests_product_add_category_limited_partnership(self):
        self.procuct_add_category(4)

    # 阳光私募
    def tests_product_add_category_sunshine_private_placement(self):
        self.procuct_add_category(5)

    # 公募基金
    def tests_product_add_category_public_fund(self):
        self.procuct_add_category(6)

    # 海外投资
    def tests_product_add_category_overseas_investment(self):
        self.procuct_add_category(7)

    # 母基金
    def tests_product_add_category_fof(self):
        self.procuct_add_category(8)

    # 保险
    def tests_product_add_category_insurance(self):
        self.procuct_add_category(9)

