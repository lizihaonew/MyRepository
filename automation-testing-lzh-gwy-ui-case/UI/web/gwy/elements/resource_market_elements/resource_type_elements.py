#coding:utf-8

'''
作者：李子浩
内容：顾问云资源市场类别管理资源二级类别管理相关元素集合
'''

from UI.base_element import ElementCollection,AsyncElement,BaseElement

class FirstTypeListElements(ElementCollection):
    '''
    类别管理一级类别列表页面元素集合；
    '''
    def __init__(self):
        self.resource = AsyncElement('tr:nth-child(3) > td:nth-child(2) > a')    # 资源


class TypeListElements(ElementCollection):
    '''
    资源二级类别列表页元素集合
    '''
    def __init__(self):
        self.back_button = AsyncElement('div.ibox-content > div > div > div > a:nth-child(1)')  # 返回按钮
        self.add_button = AsyncElement('div.ibox-content > div > div > div > a:nth-child(2)')   # 新增按钮
        self.first_row_name = AsyncElement('div.ibox-content > div > table > tbody > tr:nth-child(1) > td:nth-child(1)')    # 列表第一行的类别名称
        self.first_row_update = AsyncElement('tr:nth-child(1) > td:nth-child(3) > a:nth-child(1)')  # 列表第一行的修改类别按钮
        self.first_row_delete = AsyncElement('tr:nth-child(1) > td:nth-child(3) > a:nth-child(2)')  # 列表第一行的删除类别按钮


class AddTypeElements(ElementCollection):
    '''
    新增二级类别页面元素集合
    '''
    def __init__(self):
        self.type_name = BaseElement('body > section > div.alertBox > div > div.content-wrapper > label:nth-child(1) > input[type="text"]') # 类别名称输入框
        self.type_sort = BaseElement('body > section > div.alertBox > div > div.content-wrapper > label:nth-child(2) > input[type="number"]')  # 类别排序输入框
        self.confirm_button = AsyncElement('body > section > div.alertBox > div > div.content-wrapper > label.alert-btn > b.confirm-btn')   # 确定按钮
        self.cancel_button = AsyncElement('body > section > div.alertBox > div > div.content-wrapper > label.alert-btn > b.cancel-btn') # 取消按钮


class UpdateTypeElements(ElementCollection):
    '''
    修改类别页面元素集合
    '''
    def __init__(self):
        self.type_name = BaseElement('body > section > div.alertBox2 > div > div.content-wrapper > label:nth-child(1) > input[type="text"]')    # 类别名称输入框
        self.type_sort = BaseElement('body > section > div.alertBox2 > div > div.content-wrapper > label:nth-child(2) > input[type="number"]')  # 类别排序输入框
        self.confirm_button = AsyncElement('body > section > div.alertBox2 > div > div.content-wrapper > label.alert-btn > b.confirm-btn')  # 确定按钮
        self.cancel_button = AsyncElement('body > section > div.alertBox2 > div > div.content-wrapper > label.alert-btn > b.cancel-btn')    # 取消按钮


class DeleteTypeElements(ElementCollection):
    '''
    删除类别页面元素集合
    '''
    def __init__(self):
        self.confirm_button = AsyncElement('body > section > div.alertBox3 > div > div.content-wrapper > label > b.confirm-btn')    # 确定按钮
        self.cancel_button = AsyncElement('body > section > div.alertBox3 > div > div.content-wrapper > label > b.cancel-btn')  # 取消按钮




