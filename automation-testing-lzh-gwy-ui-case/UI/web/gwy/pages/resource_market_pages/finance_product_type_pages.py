# -*- coding: utf-8 -*-
'''
作者：李子浩
内容：顾问云资源市场管理类别管理中金融产品类别的相关page类
'''

from UI.base_page import BasePage
from UI.web.gwy.elements.resource_market_elements.finance_product_type_elements import FirstTypeListElement,TypeListElement,TypeAddPageElement,TypeUpdatePageElement,TypeDeletePageElement

class FinanceProductTypePage(BasePage):

    view_url = '/html/marketTypeManagement.html'

    def __init__(self, browser):
        self.first_type_list = FirstTypeListElement()
        self.type_list = TypeListElement()
        self.add_type = TypeAddPageElement()
        self.update_type = TypeUpdatePageElement()
        self.delete_type = TypeDeletePageElement()
        self.set_browser(browser)
        self.get_url()

    def getting_type_page(self):
        '''
        进入到金融产品二级类别列表页面
        :return: None
        '''
        self.first_type_list.finance.click()


    def add_type_do(self):
        '''
        新增一个金融产品二级类别
        :return: 新创建的二级类别的名称（类别列表第一行第一列的text）
        '''
        self.type_list.add_type_button.click()
        self.add_type.type_name('AutoTestAddFinanceProductLZH999')
        self.add_type.sort(999)
        self.add_type.confirm_button.click()
        self.refresh_page()
        return self.type_list.first_row_name.get_text()

    def update_type_do(self):
        '''
        修改创建好的金融产品二级类别
        :return: 修改后的二级类别的名称（类别列表第一行第一列的text）
        '''
        self.type_list.first_row_update.click()
        self.update_type.type_name('AutoTestUpdateFinanceProductLZH998')
        self.update_type.type_sort(998)
        self.update_type.confirm_button.click()
        self.refresh_page()
        return self.type_list.first_row_name.get_text()

    def delete_type_do(self):
        '''
        删除创建好的金融产品二级类别
        :return:
        '''
        self.type_list.first_row_delete.click()
        self.delete_type.confirm_button.click()
        self.refresh_page()
        if len(self.type_list.first_row_name()) > 0:
            return self.type_list.first_row_name.get_text()
        else:
            return 'the list is null'

