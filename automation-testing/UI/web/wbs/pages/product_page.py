# -*- coding: utf-8 -*-
from UI.base_page import BasePage
from ..elements.product_element import ProductSearchElements, ProductPropertyElements, ProductListElements, ProductViewElements
from fake_data import FakeData
import random
import sys
import time

reload(sys)
sys.setdefaultencoding("utf-8")

class ProductListPage(BasePage):

    view_url = '/html/productList.html'

    def __init__(self, browser):
        self.select_product_elements = ProductSearchElements()
        self.list_product_elements = ProductListElements()
        self.add_product_elements = ProductPropertyElements()
        self.view_product_elements = ProductViewElements()
        self.set_browser(browser)
        self.get_url()

    def select_product(self, name='', category='index=0', state=0, release=0):
        # 往元素里面传值
        self.select_product_elements.product_name(name.decode())
        # 'value={0}'.format(FakeData.product_category()) 这种写法是value的值从FakeData.product_category()里取
        # self.select_product.product_category('value={0}'.format(FakeData.product_category()))
        # self.select_product.product_state('value={0}'.format(FakeData.product_state()))
        # self.select_product.product_release('value={0}'.format(FakeData.product_release()))

        self.select_product_elements.product_category(category)
        self.select_product_elements.product_state('index={0}'.format(state))
        self.select_product_elements.product_release('index={0}'.format(release))

        # 因为list页面locator始终不变，在click后，selenium立马会拿到old页面的locator，然后操作的时候，dom tree正在刷新，所以会报staleelementexception
        # 所以用到了下面的方法with self.wait_for_page_load
        with self.wait_for_page_load(self.list_product_elements.product_name()[0]):
            self.select_product_elements.product_query.click()

        return self.list_product_elements.product_name.get_text(index=0)

    def add_product(self, product_category):
        fake = FakeData()
        self.list_product_elements.product_add.click()
        self.add_product_elements.product_category('value={0}'.format(product_category))
        product_name = 'UI自动化产品名称{0}'.format(fake.text(max_length=5))
        self.add_product_elements.product_name(product_name.decode())

        product_opinion = 'UI自动化产品点评{0}'.format(fake.text(max_length=5))
        if product_category != 1:
            self.add_product_elements.product_opinion(product_opinion.decode())
        if product_category == 7:
            self.add_product_elements.product_currency('value={0}'.format(random.randrange(1,11)))
        self.add_product_elements.product_investment_amount(random.randrange(5, 1000))

        product_deadline = FakeData.product_deadline()
        if product_category != 9:
            self.add_product_elements.product_deadline(product_deadline.decode())
        if product_category not in (6, 9, 5):
            self.add_product_elements.product_annual_yield(FakeData.product_annual_yield().decode())
        if product_category in (6, 5):
            self.add_product_elements.product_netValue('1.8727')
        if product_category not in (1, 9):
            self.add_product_elements.product_status('value={0}'.format(FakeData.product_state()))
        if product_category != 9:
            self.add_product_elements.product_risk.click(index=0)
            for i in range(0, 5):
                self.add_product_elements.product_riskTolerance.click(index=i)
        # 产品介绍（富文本）#
        product_introduction = 'UI自动化产品介绍{0}'.format(fake.text(max_length=100))
        self.add_product_elements.product_introduction(product_introduction.decode())
        if product_category not in (6, 1, 9):
            product_account_name = 'UI自动化开户名{0}'.format(fake.text(max_length=5))
            self.add_product_elements.product_account_name(product_account_name.decode())
            self.add_product_elements.product_raise_bank(FakeData.bank_name().decode())
            self.add_product_elements.product_raise_account('8888 8888 8888 8888')
            product_remark = 'UI自动化打款备注{0}'.format(fake.text(max_length=5))
            self.add_product_elements.product_remark(product_remark.decode())
        self.add_product_elements.product_seq(random.randrange(1, 9999))
        self.add_product_elements.product_next_step1.click()


        # 以下5个元素为营销信息#
        self.add_product_elements.product_smallPicFile("/Users/lida/Downloads/timg.jpeg")
        self.add_product_elements.product_bigPicFile("/Users/lida/Downloads/timg.jpeg")
        # 产品营销文案
        product_marketing_copy = 'UI自动化产品营销文案{0}'.format(fake.text(max_length=20))
        self.add_product_elements.product_marketing_copy(product_marketing_copy.decode())
        # 风险提示富文本
        if product_category != 9:
            product_risk_warning = 'UI自动化产品风险提示{0}'.format(fake.text(max_length=20))
            self.add_product_elements.product_risk_warning(product_risk_warning.decode())
        self.add_product_elements.product_next_step2.click()
        # 以下元素为产品附件#
        # FIXME E InvalidElementStateException: Message: invalid element state: Element must be user-editable in order to clear it.
        # self.add_product_elements.product_add_attachment.click()
        # self.add_product_elements.product_attachment_type('value={0}'.format(FakeData.product_attachment_type()))
        # self.add_product_elements.product_attachment_file("/Users/lida/Downloads/timg.jpeg")
        # self.add_product_elements.product_attachment_visible_range_customer.click()
        # self.add_product_elements.product_attachment_visible_range_employee.click()
        # self.add_product_elements.product_attachment_visible_range_fa.click()
        self.add_product_elements.product_next_step3.click()
        # 以下元素为产品佣金配置
        self.add_product_elements.product_productrate('120')
        self.add_product_elements.product_commissionRate('2.22')
        self.add_product_elements.product_independCommissionRatee('1.11')
        self.add_product_elements.product_next_step4.click()

        return {"name": product_name, "category": product_category}

    def update_product(self, product_category=0, product_release=0):
        fake = FakeData()
        self.list_product_elements.product_update.click()
        # self.add_product_elements.product_category('value={0}'.format(product_category))
        if product_release in (1, 2):
            product_name = 'UI自动化修改产品名称{0}'.format(fake.text(max_length=5))
            self.add_product_elements.product_name(product_name.decode())
        else:
            product_name = self.add_product_elements.product_update_product_name.get_text(index=1)
        # 以下资料可以不用修改
        # product_opinion = 'UI自动化修改产品点评{0}'.format(fake.text(max_length=5))
        # if product_category != 1:
        #     self.add_product_elements.product_opinion(product_opinion.decode())
        # if product_category == 7:
        #     self.add_product_elements.product_currency('value={0}'.format(random.randrange(1,11)))
        # self.add_product_elements.product_investment_amount(random.randrange(5, 1000))
        #
        # product_deadline = FakeData.product_deadline()
        # if product_category != 9:
        #     self.add_product_elements.product_deadline(product_deadline.decode())
        # if product_category not in (6, 9, 5):
        #     self.add_product_elements.product_annual_yield(FakeData.product_annual_yield().decode())
        # if product_category in (6, 5):
        #     self.add_product_elements.product_netValue('1.8727')
        # if product_category not in (1, 9):
        #     self.add_product_elements.product_status('value={0}'.format(FakeData.product_state()))
        # if product_category != 9:
        #     self.add_product_elements.product_risk.click(index=0)
        #     for i in range(0, 5):
        #         self.add_product_elements.product_riskTolerance.click(index=i)
        #         self.add_product_elements.product_riskTolerance.click(index=i)
        # # 产品介绍（富文本）#
        # product_introduction = 'UI自动化修改产品介绍{0}'.format(fake.text(max_length=100))
        # self.add_product_elements.product_introduction(product_introduction.decode())
        # if product_category not in (6, 1, 9):
        #     product_account_name = 'UI自动化修改开户名{0}'.format(fake.text(max_length=5))
        #     self.add_product_elements.product_account_name(product_account_name.decode())
        #     self.add_product_elements.product_raise_bank(FakeData.bank_name().decode())
        #     self.add_product_elements.product_raise_account('8888 8888 8888 8888')
        #     product_remark = 'UI自动化修改打款备注{0}'.format(fake.text(max_length=5))
        #     self.add_product_elements.product_remark(product_remark.decode())
        # self.add_product_elements.product_seq(random.randrange(1, 9999))

        self.add_product_elements.product_update_next_step1.click()
        # 点击保存之后会有5秒弹框时间，等待弹框出现，然后等弹框消失，然后操作
        self.add_product_elements.product_js_tip.wait_until_element_visible()
        self.add_product_elements.product_js_tip.wait_until_element_invisible()
        # time.sleep(5)
        self.add_product_elements.product_go_back.click()
        # self.get_url()

        return {"name": product_name, "category": product_category}

    def view_product(self, category):
        self.select_product(category=category)
        self.list_product_elements.product_name.click()
        return [self.view_product_elements.product_view.get_text(index=index) for index in range(0, len(self.view_product_elements.product_view()))]
