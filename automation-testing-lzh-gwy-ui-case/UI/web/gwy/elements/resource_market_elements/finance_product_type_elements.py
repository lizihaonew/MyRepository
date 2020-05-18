#coding:utf-8

'''
作者：李子浩
内容：顾问云资源市场管理中类别管理的金融产品二级类别相关页面元素集合
'''

from UI.base_element import BaseElement, AsyncElement, ElementCollection

class FirstTypeListElement(ElementCollection):
    '''
    类别管理一级类别列表页面元素集合；
    '''
    def __init__(self):
        self.finance = AsyncElement('tr:nth-child(1) > td:nth-child(2) > a')    # 金融产品


class TypeListElement(ElementCollection):
    '''
    金融产品二级类别列表页面元素集合
    '''
    def __init__(self):
        self.backing = AsyncElement('div.ibox-content > div > div > div > a:nth-child(1)')  # 返回按钮
        self.add_type_button = AsyncElement('div.ibox-content > div > div > div > a:nth-child(2)') # 新增二级类别按钮
        self.first_row_name = BaseElement('div.ibox-content > div > table > tbody > tr:nth-child(1) > td:nth-child(1)')    # 列表第一行的类别名称
        self.first_row_update = AsyncElement('tr:nth-child(1) > td:nth-child(3) > a:nth-child(1)')  # 列表第一行修改按钮
        self.first_row_delete = AsyncElement('tr:nth-child(1) > td:nth-child(3) > a:nth-child(2)')  # 列表第一行删除按钮


class TypeAddPageElement(ElementCollection):
    '''
    金融产品二级类别新增页面集合
    '''
    def __init__(self):
        self.type_name = BaseElement('body > section > div.alertBox > div > div.content-wrapper > label:nth-child(1) > input[type="text"]')    # 类别名称输入框
        self.sort = BaseElement('body > section > div.alertBox > div > div.content-wrapper > label:nth-child(2) > input[type="number"]')   # 排序输入框
        self.confirm_button = AsyncElement('body > section > div.alertBox > div > div.content-wrapper > label.alert-btn > b.confirm-btn')   # 确定按钮
        self.cancel_button = AsyncElement('body > section > div.alertBox > div > div.content-wrapper > label.alert-btn > b.cancel-btn')    # 取消按钮


class TypeUpdatePageElement(ElementCollection):
    '''
    金融产品修改类别页面元素集合
    '''
    def __init__(self):
        self.type_name = BaseElement('body > section > div.alertBox2 > div > div.content-wrapper > label:nth-child(1) > input[type="text"]')   # 类别名称输入框
        self.type_sort = BaseElement('body > section > div.alertBox2 > div > div.content-wrapper > label:nth-child(2) > input[type="number"]') # 排序输入框
        self.confirm_button = AsyncElement('body > section > div.alertBox2 > div > div.content-wrapper > label.alert-btn > b.confirm-btn')  # 确定按钮
        self.cancel_button = AsyncElement('body > section > div.alertBox2 > div > div.content-wrapper > label.alert-btn > b.cancel-btn')    # 取消按钮


class TypeDeletePageElement(ElementCollection):
    '''
    金融产品类别删除页面元素集合
    '''
    def __init__(self):
        self.confirm_button = AsyncElement('body > section > div.alertBox3 > div > div.content-wrapper > label > b.confirm-btn')    # 确定按钮
        self.cancel_button = AsyncElement('body > section > div.alertBox3 > div > div.content-wrapper > label > b.cancel-btn')  # 取消按钮


