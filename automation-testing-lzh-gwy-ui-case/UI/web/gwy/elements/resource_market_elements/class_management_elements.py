#coding:utf-8
'''
作者：李子浩
内容：顾问云资源市场管理模块下的培训课程管理相关元素集合
'''

from UI.base_element import BaseElement, AsyncElement, ElementCollection
from UI.special_elements.select_element import SelectElement

class ClassListElements(ElementCollection):
    '''
    课程管理列表页面相关元素集合
    '''
    def __init__(self):
        self.add_bt = AsyncElement('div:nth-child(2) > form > div:nth-child(4) > div > a')  # 新增内容
        self.title_box = BaseElement('#cp_name')    # 标题筛选框
        self.second_type = SelectElement('#pd_category')    # 二级类别筛选项
        self.query_bt = AsyncElement('#_query')     # 查询
        self.first_row_title = AsyncElement(
            'div:nth-child(3) > div > table > tbody > tr:nth-child(1) > td:nth-child(1) > a')   # 列表第一条数据标题
        self.first_row_type = AsyncElement(
            'div:nth-child(3) > div > table > tbody > tr:nth-child(1) > td:nth-child(2) > span')    # 列表第一条数据二级类别
        self.first_row_update = AsyncElement(
            'div:nth-child(3) > div > table > tbody > tr:nth-child(1) > td:nth-child(7) > a:nth-child(1)')  # 列表第一条数据的修改按钮
        self.first_row_delete = AsyncElement(
            'div:nth-child(3) > div > table > tbody > tr:nth-child(1) > td:nth-child(7) > a:nth-child(2)')  # 列表第一条数的删除按钮


class AddClassElements(ElementCollection):
    '''
    新增课程编辑页面相关元素集合
    '''
    def __init__(self):
        self.second_type = SelectElement('#newsForm > div.form-group.form-group-20 > div > select')     # 二级类别
        self.type = AsyncElement('#newsForm > div:nth-child(3) > div > label:nth-child(1) > input[type="radio"]')   # 类型
        self.title_box = BaseElement('#newsForm > div:nth-child(5) > div > input')  # 标题
        self.img_send = BaseElement(
            '#newsForm > div:nth-child(7) > div > div > span.btn.btn-default.btn-file > input[type="file"]')    # 上传图片
        self.author_box = BaseElement('#newsForm > div:nth-child(9) > div > input')     # 作者
        self.summary_box = BaseElement('#newsForm > div:nth-child(11) > div > textarea')    # 简介
        self.content_box = BaseElement(
            '#newsForm > div.form-group.form-group-80 > div > div.note-editor.note-frame.panel.panel-default > div.note-editing-area > div.note-editable.panel-body')
        self.file_send = BaseElement('#contactAttachments')     # 文本附件
        self.price_box = BaseElement('#newsForm > div:nth-child(17) > div > input')     # 价格
        self.visible_range = AsyncElement(
            '#newsForm > div:nth-child(19) > div > div > label:nth-child(1) > input[type="checkbox"]')  # 可见范围配置
        self.confirm_bt = AsyncElement('.btn.btn-Save')     # 确定


class ClassDetailElements(ElementCollection):
    '''
    课程详情页面相关元素集合
    '''
    def __init__(self):
        self.title = AsyncElement('#form > div > fieldset > div > div > div:nth-child(5) > div > span')     # 详情页标题


class UpdateClassElements(ElementCollection):
    '''
    课程修改页面相关元素集合
    '''
    def __init__(self):
        self.title_box = BaseElement('#newsForm > div:nth-child(5) > div > input')  # 标题
        self.confirm_bt = AsyncElement('.btn.btn-Save')     # 确定


class QueryClassElements(ElementCollection):
    '''
    按照标题筛选课程数据
    '''
    def __init__(self):
        self.title_box = BaseElement('#cp_name')    # 标题
        self.query_bt = AsyncElement('#_query')     # 查询按钮


class DeleteClassElements(ElementCollection):
    '''
    删除课程相关元素集合
    '''
    def __init__(self):
        self.confirm_bt = AsyncElement(
            'body > div.alertBox3 > div > div.content-wrapper > label > b.confirm-btn')  # 确定按钮
        self.success_tip = AsyncElement('.layui-layer-content')     # 操作成功提示框


