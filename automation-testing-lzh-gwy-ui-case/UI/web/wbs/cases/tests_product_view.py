# -*- coding: utf-8 -*-
import random
from UI.base_case import BaseUITestCase
from ..pages.product_page import ProductListPage


class ProductViewTest(BaseUITestCase):

    def setUp(self):
        self.product_view = ProductListPage(self.browser)

    def tests_product_view1(self):
        list_view_1 = ['产品分类：', '产品名称：', '起投金额：', '产品期限：', '期待年回报率：', '产品风险等级：',
                       '允许客户风险类型：', '产品介绍：', '产品排序：']
        list1 = self.product_view.view_product('value=1')
        self.assertListEqual(list1, list_view_1)

    def tests_product_view2(self):
        list_view_2 = ['产品分类：', '产品名称：', '产品点评：', '起投金额：', '产品期限：','期待年回报率：',
                       '产品状态：', '产品风险等级：', '允许客户风险类型：', '产品介绍：',
                       '开户名：', '募集银行：', '募集账号：', '客户打款备注：', '产品排序：']
        list1 = self.product_view.view_product('value=2')
        self.assertListEqual(list1, list_view_2)

    def tests_product_view3(self):
        list_view_3 = ['产品分类：', '产品名称：', '产品点评：', '起投金额：', '产品期限：','期待年回报率：',
                       '产品状态：', '产品风险等级：', '允许客户风险类型：', '产品介绍：',
                       '开户名：', '募集银行：', '募集账号：', '客户打款备注：', '产品排序：']
        list1 = self.product_view.view_product('value=3')
        self.assertListEqual(list1, list_view_3)

    def tests_product_view4(self):
        list_view_4 = ['产品分类：', '产品名称：', '产品点评：', '起投金额：', '产品期限：','期待年回报率：',
                       '产品状态：', '产品风险等级：', '允许客户风险类型：', '产品介绍：',
                       '开户名：', '募集银行：', '募集账号：', '客户打款备注：', '产品排序：']
        list1 = self.product_view.view_product('value=4')
        self.assertListEqual(list1, list_view_4)

    def tests_product_view5(self):
        list_view_5 = ['产品分类：', '产品名称：', '产品点评：', '起投金额：', '产品期限：','净值：',
                       '产品状态：', '产品风险等级：', '允许客户风险类型：', '产品介绍：',
                       '开户名：', '募集银行：', '募集账号：', '客户打款备注：', '产品排序：']
        list1 = self.product_view.view_product('value=5')
        self.assertListEqual(list1, list_view_5)

    def tests_product_view6(self):
        list_view_6 = ['产品分类：', '产品名称：', '产品点评：', '起投金额：', '产品期限：','净值：',
                       '产品状态：', '产品风险等级：', '允许客户风险类型：', '产品介绍：', '产品排序：']
        list1 = self.product_view.view_product('value=6')
        self.assertListEqual(list1, list_view_6)

    def tests_product_view7(self):
        list_view_7 = ['产品分类：', '产品名称：', '产品点评：', '币种：', '起投金额：', '产品期限：','期待年回报率：',
                       '产品状态：', '产品风险等级：', '允许客户风险类型：', '产品介绍：',
                       '开户名：', '募集银行：', '募集账号：', '客户打款备注：', '产品排序：']
        list1 = self.product_view.view_product('value=7')
        self.assertListEqual(list1, list_view_7)

    def tests_product_view8(self):
        list_view_8 = ['产品分类：', '产品名称：', '产品点评：', '起投金额：', '产品期限：','期待年回报率：',
                       '产品状态：', '产品风险等级：', '允许客户风险类型：', '产品介绍：',
                       '开户名：', '募集银行：', '募集账号：', '客户打款备注：', '产品排序：']
        list1 = self.product_view.view_product('value=8')
        self.assertListEqual(list1, list_view_8)

    def tests_product_view9(self):
        list_view_9 = ['产品分类：', '产品名称：', '产品特点：', '参考保费：', '产品介绍：', '产品排序：']
        list1 = self.product_view.view_product('value=9')
        self.assertListEqual(list1, list_view_9)
