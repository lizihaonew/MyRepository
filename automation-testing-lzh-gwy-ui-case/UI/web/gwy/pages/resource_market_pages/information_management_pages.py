#coding:utf-8
'''
作者：李子浩
内容：顾问云资源市场管理模块资讯管理相关page类
'''

from UI.base_page import BasePage
import random,time
from ...elements.resource_market_elements.information_management_elements import InformationListElements, AddPageElements, UpdatePageElements, DeletePageElements


class InformationPages(BasePage):
    view_url = r'/html/marketNewsManagement.html'
    add_name = 'AutoTestAddName' + str(random.randint(1, 100)).zfill(3)
    phone_number = '1' + str(random.randint(0, 1000000000)).zfill(10)
    update_name = 'AutoTestUpdateName'
    img_path = r'..\..\..\file\timg.jpeg'

    def __init__(self, browser):
        self.information_list = InformationListElements()
        self.add_information = AddPageElements()
        self.update_information = UpdatePageElements()
        self.delete_information = DeletePageElements()
        self.set_browser(browser)
        self.get_url()

    def do_add_information(self):
        '''
        新增资讯
        :return: 列表页第一条数据的标题
        '''
        self.information_list.add_bt.click()
        self.add_information.second_type_select('index=1')
        self.add_information.title_box(self.add_name)
        self.add_information.summary_box(u'这是简介的内容！')
        self.add_information.img_box(self.img_path, file_type=True)
        self.add_information.price_box(20000)
        self.add_information.phone_number(self.phone_number)
        self.add_information.wechat_box('wechar_number')
        self.add_information.confirm_bt.click()
        self.wait_success_tip_invisible()
        # self.refresh_page()
        return self.information_list.first_row_title.get_text()

    def do_update_information(self):
        '''
        修改资讯
        :return:修改后的列表页第一条数据的标题
        '''
        self.information_list.first_row_update.click()
        self.update_information.title_box(self.update_name)
        self.update_information.confirm_bt.click()
        self.wait_success_tip_invisible()
        return self.information_list.first_row_title.get_text()

    def do_select_information(self):
        '''
        列表页筛选资讯
        :return:
        '''
        self.information_list.title_box(self.update_name)
        self.information_list.query_bt.click()
        return self.information_list.first_row_title.get_text()

    def do_delete_information(self):
        '''
        删除资讯
        :return:返回操作成功的文案
        '''
        self.information_list.first_row_delete.click()
        self.delete_information.confirm_bt.click()
        return self.delete_information.success_tip.get_text()



