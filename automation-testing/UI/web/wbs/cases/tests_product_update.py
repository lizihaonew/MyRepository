# -*- coding: utf-8 -*-
import random
from UI.base_case import BaseUITestCase
from ..pages.product_page import ProductListPage, ProductPropertyElements, ProductSearchElements



class ProductUpdateTest(BaseUITestCase):

    def setUp(self):
        self.product_update = ProductListPage(self.browser)

    def product_update_category(self, productrelease, searchcategory, productcategory):
        self.product_update.select_product(category=searchcategory, release=productrelease)
        # self.product_update.update_product(productcategory)
        name1 = self.product_update.update_product(productcategory, productrelease)['name']
        name2 = self.product_update.select_product(name1)
        self.assertEqual(name1, name2)

    def tests_product_update_category1(self):
        self.product_update_category(1, 'value=1', 1)

    def tests_product_update_category2(self):
        self.product_update_category(1, 'value=2', 2)

    def tests_product_update_category3(self):
        self.product_update_category(1, 'value=3', 3)

    def tests_product_update_category4(self):
        self.product_update_category(1, 'value=4', 4)

    def tests_product_update_category5(self):
        self.product_update_category(1, 'value=5', 5)

    def tests_product_update_category6(self):
        self.product_update_category(1, 'value=6', 6)

    def tests_product_update_category7(self):
        self.product_update_category(1, 'value=7', 7)

    def tests_product_update_category8(self):
        self.product_update_category(1, 'value=8', 8)

    def tests_product_update_category9(self):
        self.product_update_category(1, 'value=9', 9)

    def tests_product_modify_release1(self):
        self.product_update_category(3, 'value=1', 1)

    def tests_product_modify_release2(self):
        self.product_update_category(3, 'value=2', 2)

    def tests_product_modify_release3(self):
        self.product_update_category(3, 'value=3', 3)

    def tests_product_modify_release4(self):
        self.product_update_category(3, 'value=4', 4)

    def tests_product_modify_release5(self):
        self.product_update_category(3, 'value=5', 5)

    def tests_product_modify_release6(self):
        self.product_update_category(3, 'value=6', 6)

    def tests_product_modify_release7(self):
        self.product_update_category(3, 'value=7', 7)

    def tests_product_modify_release8(self):
        self.product_update_category(3, 'value=8', 8)

    def tests_product_modify_release9(self):
        self.product_update_category(3, 'value=9', 9)
