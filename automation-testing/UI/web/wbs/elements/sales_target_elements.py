# -*- coding: utf-8 -*-
from UI.base_element import BaseElement, AsyncElement, ElementCollection
from UI.special_elements.select_element import SelectElement


class SalesTargetElement(ElementCollection):

    def __init__(self):
        # 按照职位设置
        self.save_position = AsyncElement('#position_save')
        self.add_position_button = AsyncElement('#add_position')
        self.delete_list = AsyncElement('._delete')
        self.position_sales_target_list = AsyncElement('.position_goal')
        self.choice_position_list = AsyncElement('.checkbox_position')
        self.choice_position_list_page_size = AsyncElement('#pageSize')
        self.choice_position_list_add = AsyncElement('#_add')
        self.choice_position_list_title_search = AsyncElement('#position_title')
        self.choice_position_list_title_search_button = AsyncElement('#query_position')
        self.delete_list_confirm_button = AsyncElement('.btn.highlight.js-btn.js-ok')
        self.position_name = AsyncElement('[class="gradeX"] td:nth-child(1)')
        self.choice_position_name = AsyncElement('.gradeA td:nth-child(2)')

        # 按照部门/人员设置
        self.tab2 = AsyncElement('a[href="#tab-2"]')
        self.save_dept = AsyncElement('#dept_save')
        self.department_employee_sales_target_list = AsyncElement('.right_input')
        self.employee_search = AsyncElement('#_search')
        self.employee_name = AsyncElement('#name')
        self.employee_id = AsyncElement('#employeeId')
        self.employee_phone = AsyncElement('#phoneNumber')
        self.employee_query_button = AsyncElement('#queryEmployees')
        self.employee_sales_target = AsyncElement('.employee_goal')
        self.employee_sales_target_save = AsyncElement('#employees_save')
        self.employee_sales_target_save_tip = AsyncElement('.content.js-tip')
