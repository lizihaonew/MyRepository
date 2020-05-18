#coding:utf-8
'''
作者：李子浩
内容：顾问云资源市场管理模块下素材管理相关page类
'''

from UI.base_page import BasePage
from ...elements.resource_market_elements.material_management_elements import MaterialListElements, MaterialAddElements, MaterialUpdateElements, MaterialDeleteElements
import random
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class MaterialManagementPages(BasePage):
    view_url = r'/html/marketMaterialManagement.html'
    add_title = 'AutoTestAddTitle' + str(random.randint(0, 99)).zfill(3)
    file_path = r'..\..\..\file\material.rar'
    img_path = r'..\..\..\file\timg.jpeg'
    update_title = 'AutoTestUpdateTitle'


    def __init__(self, browser):
        self.material_list = MaterialListElements()
        self.material_add = MaterialAddElements()
        self.material_update = MaterialUpdateElements()
        self.material_delete = MaterialDeleteElements()
        self.set_browser(browser)
        self.get_url()

    def do_add_material(self):
        '''
        新增素材操作
        :return: 新增后列表页第一条数据的标题
        '''
        self.material_list.add_bt.click()
        self.material_add.second_type('index=1')
        self.material_add.title_box(self.add_title)
        self.material_add.file_post(self.file_path, file_type=True)
        self.material_add.img_post(self.img_path, file_type=True)
        self.material_add.price_box(20000)
        self.material_add.confirm_bt.click()
        self.wait_success_tip_invisible()
        return self.material_list.first_row_title.get_text()

    def do_update_material(self):
        '''
        修改素材操作
        :return: 修改后列表页第一条数据的标题
        '''
        self.material_list.first_row_update.click()
        self.material_update.title_box(self.update_title)
        self.material_update.confirm_bt.click()
        self.wait_success_tip_invisible()
        return self.material_list.first_row_title.get_text()

    def do_query_material(self):
        '''
        通过标题搜索素材
        :return: 搜索结果中第一条数据的标题
        '''
        self.material_list.title_box(self.update_title)
        self.material_list.query_bt.click()
        return self.material_list.first_row_title.get_text()

    def do_delete_material(self):
        '''
        删除素材操作
        :return: 操作成功提示框文案内容
        '''
        self.material_list.first_row_delete.click()
        self.material_delete.confirm_bt.click()
        return self.material_delete.success_tip.get_text()

