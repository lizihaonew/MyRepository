# -*- coding: utf-8 -*-
import random
from UI.base_case import BaseUITestCase
from ..pages.product_page import ProductListPage


class ProductSearchTest(BaseUITestCase):

    def setUp(self):
        self.product_search = ProductListPage(self.browser)

    def tests_product_search(self):
        self.product_search.select_product('财富')
