# -*- coding: utf-8 -*-
from UI.base_element import BaseElement, AsyncElement, ElementCollection
from UI.special_elements.select_element import SelectElement


class ResourceElement(ElementCollection):

    def __init__(self):
        self.resource_add = AsyncElement('#add_resource')
        self.resource_title = AsyncElement('#title')
        self.resource_summary = AsyncElement('#summary')
        self.resource_start_time = AsyncElement('#startTime')
        self.resource_end_time = AsyncElement('#endTime')
        self.resource_address = AsyncElement('[name="address"]')
        self.resource_people_num = AsyncElement('#peopleNum')
        self.resource_content = AsyncElement('.note-editable.panel-body')
        self.resource_img = AsyncElement('#file_img')
        self.resource_visible_customer = AsyncElement('#scope_1')
        self.resource_visible_employee = AsyncElement('#scope_2')
        self.resource_visible_fa = AsyncElement('#scope_4')
        self.resource_submit = AsyncElement('#_submit')