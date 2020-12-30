#coding:utf-8
'''
作者：李子浩
内容：顾问云资源市场管理模块下资讯管理相关元素集合
'''

from UI.base_element import BaseElement, ElementCollection, AsyncElement
from UI.special_elements.select_element import SelectElement


class InformationListElements(ElementCollection):
    '''
    资源管理列表页面元素集合
    '''
    def __init__(self):
        self.add_bt = AsyncElement('.creaseCompany')    # 新增内容按钮
        self.title_box = BaseElement('#cp_name')    # 标题输入框
        self.second_type = SelectElement('#pd_category')    # 二级分类
        self.query_bt = AsyncElement('#_query')     # 查询按钮
        self.first_row_title = AsyncElement(
            'div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td:nth-child(1)')   # 列表第一条数据的标题
        self.first_row_type = AsyncElement(
            'div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td:nth-child(2)')    # 列表第一行的二级类别
        self.first_row_update = AsyncElement(
            'div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td:nth-child(5) > a:nth-child(1)') # 列表第一条数据修改按钮
        self.first_row_delete = AsyncElement(
            'div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td:nth-child(5) > a:nth-child(2)') # 列表第一行的删除按钮


class AddPageElements(ElementCollection):
    '''
    新增内容编辑页面元素集合
    '''

    def __init__(self):
        self.second_type_select = SelectElement('.chosen-select.twoType-select')   # 二级类别
        self.title_box = BaseElement('#newsForm > div:nth-child(3) > div > input')  # 标题
        self.summary_box = BaseElement('.newsSummary')  # 简介
        self.img_box = BaseElement(
            '#newsForm > div:nth-child(7) > div > div > span.btn.btn-default.btn-file > input[type="file"]') # 上传图片
        self.price_box = BaseElement('#newsForm > div.form-group.form-group20 > div > input')   # 价格
        self.phone_number = BaseElement('#newsForm > div:nth-child(11) > div > input')  # 联系电话
        self.wechat_box = BaseElement('#newsForm > div:nth-child(13) > div > input')    # 微信
        self.confirm_bt = AsyncElement('.btn.btn-Save') # 确定按钮


class UpdatePageElements(ElementCollection):
    '''
    修改内容页面元素集合
    '''
    def __init__(self):
        self.title_box = BaseElement('#newsForm > div:nth-child(3) > div > input')  # 标题
        self.confirm_bt = AsyncElement('#newsForm > div:nth-child(15) > div > div.btn.btn-Save')     # 确定按钮


class DeletePageElements(ElementCollection):
    '''
    删除页面元素集合
    '''
    def __init__(self):
        self.confirm_bt = AsyncElement('div.alertBox3 > div > div.content-wrapper > label > b.confirm-btn')     # 确定按钮
        self.cancel_bt = AsyncElement('div.alertBox3 > div > div.content-wrapper > label > b.cancel-btn')       # 取消按钮
        self.success_tip = AsyncElement('.layui-layer-content')

