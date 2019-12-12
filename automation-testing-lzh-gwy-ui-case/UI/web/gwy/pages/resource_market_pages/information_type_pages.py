#coding:utf-8
'''
作者：李子浩
内容：顾问云类别管理资讯二级类别相关page类
'''

from UI.base_page import BasePage
from ...elements.resource_market_elements.information_type_elements import FirstTypeListElement,TypeListElements,AddTypeElements,UpdateTypeElements,DeleteTypeElements

class InformationTypePages(BasePage):
    view_url = '/html/marketTypeManagement.html'

    def __init__(self, browser):
        self.first_type_list = FirstTypeListElement()
        self.type_list = TypeListElements()
        self.add_type = AddTypeElements()
        self.update_type = UpdateTypeElements()
        self.delete_type = DeleteTypeElements()
        self.set_browser(browser)
        self.get_url()

    def getting_type_list(self):
        '''
        进入到资讯类别列表页面
        :return: None
        '''
        self.first_type_list.information.click()

    def add_type_do(self):
        '''
        新增资讯二级类别
        :return: 返回二级类别列表第一行的名称
        '''
        self.type_list.add_button.click()
        self.add_type.type_name('AutoTestAddInformationLZH999')
        self.add_type.type_sort(999)
        self.add_type.confirm_button.click()
        self.refresh_page()
        return self.type_list.first_row_name.get_text()

    def update_type_do(self):
        '''
        修改资讯二级类别
        :return: 返回二级类别列表第一行的名称
        '''
        self.type_list.first_row_update.click()
        self.update_type.type_name('AutoTestUpdateInformationLZH998')
        self.update_type.type_sort(998)
        self.update_type.confirm_button.click()
        self.refresh_page()
        return self.type_list.first_row_name.get_text()

    def delete_type_do(self):
        '''
        删除资讯二级类别
        :return: 返回二级类别列表第一行的名称
        '''
        self.type_list.first_row_delete.click()
        self.delete_type.confirm_button.click()
        self.refresh_page()
        if len(self.type_list.first_row_name()) > 0:
            return self.type_list.first_row_name.get_text()
        else:
            return 'the list is null'
