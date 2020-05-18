#coding:utf-8
'''
作者：李子浩
内容：顾问云资源市场管理模块下的培训课程管理相关page类
'''

from UI.base_page import BasePage
from ...elements.resource_market_elements.class_management_elements import ClassListElements, AddClassElements, ClassDetailElements, UpdateClassElements, QueryClassElements, DeleteClassElements
import random

class ClassManagementPages(BasePage):
    view_url = r'/html/marketCourseManagement.html'
    add_title = 'AutoTestAddTitle' + str(random.randint(0, 99)).zfill(3)
    img_path = r'..\..\..\file\timg.jpeg'
    file_path = r'..\..\..\file\test_file.pdf'
    update_title = 'AutoTestUpdateTitle'

    def __init__(self, browser):
        self.class_list = ClassListElements()
        self.add_class = AddClassElements()
        self.class_detail = ClassDetailElements()
        self.update_class = UpdateClassElements()
        self.query_class = QueryClassElements()
        self.delete_class = DeleteClassElements()
        self.set_browser(browser)
        self.get_url()

    def do_add_class(self):
        '''
        添加课程操作
        :return: 添加课程后列表页面第一条数据的标题
        '''
        self.class_list.add_bt.click()
        self.add_class.second_type('index=2')
        self.add_class.type.click()
        self.add_class.title_box(self.add_title)
        self.add_class.img_send(self.img_path, file_type=True)
        self.add_class.author_box('AutoTestUser')
        self.add_class.summary_box(u'这是简介！')
        self.add_class.content_box('abcdefghijklmnopqrstuvwxyz123456789')
        self.add_class.file_send(self.file_path, file_type=True)
        self.add_class.price_box(20000)
        self.add_class.visible_range.click()
        self.add_class.confirm_bt.click()
        self.wait_success_tip_invisible()
        return self.class_list.first_row_title.get_text()

    def do_detail_class(self):
        '''
        查看课程详情操作
        :return: 详情页课程标题
        '''
        self.class_list.first_row_title.click()
        return self.class_detail.title.get_text()

    def do_update_class(self):
        '''
        修改课程操作
        :return: 修改后列表页面第一条数据的标题
        '''
        self.class_list.first_row_update.click()
        self.update_class.title_box(self.update_title)
        self.update_class.confirm_bt.click()
        self.wait_success_tip_invisible()
        return self.class_list.first_row_title.get_text()

    def do_query_class(self):
        '''
        通过标题筛选课程数据
        :return: 筛选出的第一条数据的标题
        '''
        self.class_list.title_box(self.update_title)
        self.class_list.query_bt.click()
        return self.class_list.first_row_title.get_text()

    def do_delete_class(self):
        '''
        删除课程操作
        :return: 操作成功提示框的文案
        '''
        self.class_list.first_row_delete.click()
        self.delete_class.confirm_bt.click()
        return self.delete_class.success_tip.get_text()

