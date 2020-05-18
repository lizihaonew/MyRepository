#coding:utf-8

'''
作者：李子浩
内容：顾问云资源市场素材二级类别相关page类
'''

from UI.base_page import BasePage
from ...elements.resource_market_elements.material_type_elements import FirstTypeListElements,TypeListElements,AddTypeElements,UpdateTypeElements,DeleteTypeElements

class MaterialTypePages(BasePage):
    view_url = '/html/marketTypeManagement.html'

    def __init__(self, browser):
        self.first_type_list = FirstTypeListElements()
        self.type_list = TypeListElements()
        self.add_type = AddTypeElements()
        self.update_type = UpdateTypeElements()
        self.delete_type = DeleteTypeElements()
        self.set_browser(browser)
        self.get_url()

    def getting_type_page(self):
        '''
        进入到素材二级类别列表
        :return: None
        '''
        self.first_type_list.material.click()

    def add_type_do(self):
        '''
        新增素材二级类别
        :return: 新创建的二级类别名称
        '''
        self.type_list.add_button.click()
        self.add_type.type_name('AutoTestAddMaterialLZH999')
        self.add_type.type_sort(999)
        self.add_type.confirm_button.click()
        self.refresh_page()
        return self.type_list.first_row_name.get_text()


    def update_type_do(self):
        '''
        修改新增的素材二级类别
        :return: 修改后的二级类别名称
        '''
        self.type_list.first_row_update.click()
        self.update_type.type_name('AutoTestUpdateMaterialLZH998')
        self.update_type.type_sort(998)
        self.update_type.confirm_button.click()
        self.refresh_page()
        return self.type_list.first_row_name.get_text()

    def delete_type_do(self):
        '''
        删除新增的素材二级类别
        :return: 二级类别列表第一行的类别名称
        '''
        self.type_list.first_row_delete.click()
        self.delete_type.confirm_button.click()
        self.refresh_page()
        if len(self.type_list.first_row_name()) > 0:
            return self.type_list.first_row_name.get_text()
        else:
            return 'the list is null'





