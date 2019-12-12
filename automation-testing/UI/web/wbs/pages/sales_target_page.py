# -*- coding: utf-8 -*-
from UI.base_page import BasePage
from ..elements.sales_target_elements import SalesTargetElement
from fake_data import FakeData
import random
import sys
import time

reload(sys)
sys.setdefaultencoding("utf-8")

class SalesTargetPage(BasePage):

    view_url = '/html/programSales.html'

    def __init__(self, browser):
        self.sales_target_elements = SalesTargetElement()
        self.set_browser(browser)
        self.get_url()

    def set_sales_target_by_position(self):
        sales_target = []
        for i in range(0, len(self.sales_target_elements.position_sales_target_list())):
            sales_target1 = random.randint(100, 1000)
            self.sales_target_elements.position_sales_target_list(value=str(sales_target1), index=i)
            sales_target.append(sales_target1)
        with self.wait_for_page_load(self.sales_target_elements.position_sales_target_list()[0]):
            self.sales_target_elements.save_position.click()
        return sales_target

    def position_sales_target_list(self):
        sales_target = []
        for i in range(0, len(self.sales_target_elements.position_sales_target_list())):
            sales_target.append(int(self.sales_target_elements.position_sales_target_list()[i].get_attribute('value')))
        return sales_target

    def add_position_sales_target(self):
        # self.sales_target_elements.choice_position_list_page_size('value=30')
        self.sales_target_elements.add_position_button.click()
        name_list = []
        for i in range(0,len(self.sales_target_elements.choice_position_list())):
            self.sales_target_elements.choice_position_list.click(index=i)
            name_list.append(self.sales_target_elements.choice_position_name.get_text(index=i))
        self.sales_target_elements.choice_position_list_add.click()
        with self.wait_for_page_load(self.sales_target_elements.position_name()[0]):
            self.sales_target_elements.save_position.click()
        return name_list

    # 按职位设置目标的列表职位名称list
    def position_sales_name_list(self):
        # self.get_url()
        name_list = []
        for i in range(0, len(self.sales_target_elements.position_name())):
            name_list.append(self.sales_target_elements.position_name.get_text(index=i))
        return name_list

    # 删除职位目标
    def delete_position_sales_target(self):
        #for i in range(0,len(self.sales_target_elements.delete_list())):
        self.sales_target_elements.delete_list.click()
        self.switch_to_div_alert()
        with self.wait_for_page_load(self.sales_target_elements.position_name()[0]):
            self.sales_target_elements.delete_list_confirm_button.click()

    # 查询按职位设置的总个数
    def position_sales_target_num(self):
        num = len(self.sales_target_elements.position_name())
        return num

    # 按照部门设置销售目标
    def set_sales_target_by_department(self):
        self.sales_target_elements.tab2.click()
        # FIXME 不能只一级部门获取到，暂时先获取第一个部门
        # sales_target = []
        # for i in range(0, len(self.sales_target_elements.department_employee_sales_target_list())):
        #     sales_target1 = random.randint(100, 1000)
        #     self.sales_target_elements.department_employee_sales_target_list(value=str(sales_target1), index=i)
        #     sales_target.append(sales_target1)
        sales_target = random.randint(100, 1000)
        self.sales_target_elements.department_employee_sales_target_list(str(sales_target))
        with self.wait_for_page_load(self.sales_target_elements.department_employee_sales_target_list()[0]):
            self.sales_target_elements.save_dept.click()
        return sales_target

    # 查询按部门/人员设置目标所有的值list
    def department_sales_target_list(self):
        # sales_target = []
        # for i in range(0, len(self.sales_target_elements.department_employee_sales_target_list())):
        #     sales_target.append(int(self.sales_target_elements.department_employee_sales_target_list()[i].get_attribute('value')))

        # get_attribute('value') 是取属性中value的值
        sales_target = int(self.sales_target_elements.department_employee_sales_target_list()[0].get_attribute('value'))
        return sales_target

    def employee_sales_target_query(self, name='', id='', phone=''):
        self.sales_target_elements.tab2.click()
        self.sales_target_elements.employee_search.click()
        self.sales_target_elements.employee_name(name)
        self.sales_target_elements.employee_id(id)
        self.sales_target_elements.employee_phone(phone)
        self.sales_target_elements.employee_query_button.click()

    def employee_sales_target_list(self, name='', id='', phone=''):
        self.employee_sales_target_query(name=name, id=id, phone=phone)
        sales_target = []
        for i in range(0, len(self.sales_target_elements.employee_sales_target())):
            j = random.randint(100, 1000)
            self.sales_target_elements.employee_sales_target(j)
            sales_target.append(j)
        with self.wait_for_page_load(self.sales_target_elements.employee_sales_target()[0]):
            self.sales_target_elements.employee_sales_target_save.click()
            self.sales_target_elements.employee_sales_target_save_tip.wait_until_element_visible()
            self.sales_target_elements.employee_sales_target_save_tip.wait_until_element_invisible()
        return sales_target

    def employee_sales_target_list_search(self, name='', id='', phone=''):
        self.get_url()
        self.employee_sales_target_query(name=name, id=id, phone=phone)
        sales_target = []
        for i in range(0, len(self.sales_target_elements.employee_sales_target())):
            sales_target.append(int(self.sales_target_elements.employee_sales_target()[i].get_attribute('value')))
        return sales_target
