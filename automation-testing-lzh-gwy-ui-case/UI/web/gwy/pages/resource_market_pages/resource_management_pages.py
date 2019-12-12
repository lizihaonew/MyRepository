#coding:utf-8
'''
作者：李子浩
内容：顾问云资源市场管理模块下资源管理相关page类
'''

from UI.base_page import BasePage
from ...elements.resource_market_elements.resource_management_elements import ResourceListElements, AddResurceElements, UpdateResourceElements, DeleteResourceElements
import random

class ResourceManagementPages(BasePage):
    view_url = r'/html/marketRecourseManagement.html'
    add_title = 'AutoTestAddTitle' + str(random.randint(0, 99)).zfill(3)
    img_path = r'..\..\..\file\timg.jpeg'
    phone_number = '1' + str(random.randint(0, 1000000000)).zfill(10)
    update_title = 'AutoTestUpdateTitle'


    def __init__(self, browser):
        self.resource_list = ResourceListElements()
        self.add_resource = AddResurceElements()
        self.update_resource = UpdateResourceElements()
        self.delete_resource = DeleteResourceElements()
        self.set_browser(browser)
        self.get_url()

    def do_add_resource(self):
        '''
        新增资源操作
        :return: 新增的列表页第一条数据的标题
        '''
        self.resource_list.add_bt.click()
        self.add_resource.second_type('index=2')
        self.add_resource.title_box(self.add_title)
        self.add_resource.summary_box(u'这是简介输入框')
        self.add_resource.img_send(self.img_path, file_type=True)
        self.add_resource.price_box(20000)
        self.add_resource.phone_number_box(self.phone_number)
        self.add_resource.wechat_box('WechatNumber')
        self.add_resource.confirm_bt.click()
        self.wait_success_tip_invisible()
        return self.resource_list.first_row_title.get_text()

    def do_update_resource(self):
        '''
        修改资源操作
        :return: 修改后的列表页第一条数据的标题
        '''
        self.resource_list.first_row_update.click()
        self.update_resource.title_box(self.update_title)
        self.update_resource.confirm_bt.click()
        self.wait_success_tip_invisible()
        return self.resource_list.first_row_title.get_text()

    def do_query_resource(self):
        '''
        筛选查询列表资源数据
        :return: 通过title筛选出来的结果数据的title
        '''
        self.resource_list.title_box(self.update_title)
        self.resource_list.query_bt.click()
        return self.resource_list.first_row_title.get_text()

    def do_delete_resource(self):
        '''
        删除资源操作
        :return: 操作成功提示框的文案
        '''
        self.resource_list.first_row_delete.click()
        self.delete_resource.confirm_bt.click()
        return self.delete_resource.success_tip.get_text()


