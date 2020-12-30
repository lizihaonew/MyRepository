#coding:utf-8
'''
作者：李子浩
内容：顾问云资源市场管理模块资源管理相关元素集合
'''

from UI.base_element import BaseElement, AsyncElement, ElementCollection
from UI.special_elements.select_element import SelectElement

class ResourceListElements(ElementCollection):
    '''
    资源管理列表页相关元素集合
    '''
    def __init__(self):
        self.add_bt = AsyncElement('#page-wrapper > div > div > div > div > div.ibox-tab > div > a')    # 新增按钮
        self.title_box = BaseElement('#cp_name')    # 标题筛选
        self.second_type = SelectElement('#pd_category')    # 筛选二级分类
        self.query_bt = AsyncElement('#_query')
        self.first_row_title = AsyncElement('div:nth-child(4) > div > table > tbody > tr > td:nth-child(1)')    # 列表第一条数据标题
        self.first_row_type = AsyncElement('div:nth-child(4) > div > table > tbody > tr > td:nth-child(2)')     # 列表第一条数据二级类别
        self.first_row_update = AsyncElement(
            'div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td:nth-child(5) > a:nth-child(1)')      # 列表第一条数据修改按钮
        self.first_row_delete = AsyncElement(
            'div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td:nth-child(5) > a:nth-child(2)')      # 列表第一条数据删除按钮


class AddResurceElements(ElementCollection):
    '''
    新增资源编辑页面相关元素集合
    '''
    def __init__(self):
        self.second_type = SelectElement('#newsForm > div.form-group.form-group-20 > div > select')     # 二级类别
        self.title_box = BaseElement('#newsForm > div:nth-child(3) > div > input')  # 标题
        self.summary_box = BaseElement('.newsSummary')  # 简介
        self.img_send = BaseElement(
            '#newsForm > div:nth-child(7) > div > div > span.btn.btn-default.btn-file > input[type="file"]')    # 上传图片
        self.price_box = BaseElement('#newsForm > div.form-group.form-group20 > div > input')   # 价格
        self.phone_number_box = BaseElement('#newsForm > div:nth-child(11) > div > input')  # 联系电话
        self.wechat_box = BaseElement('#newsForm > div:nth-child(13) > div > input')    # 微信
        self.confirm_bt = AsyncElement('.btn.btn-Save')     # 确定


class UpdateResourceElements(ElementCollection):
    '''
    修改资源编辑页面相关元素集合
    '''
    def __init__(self):
        self.title_box = BaseElement('#newsForm > div:nth-child(3) > div > input')  # 标题
        self.confirm_bt = AsyncElement('.btn.btn-Save')  # 确定


class DeleteResourceElements(ElementCollection):
    '''
    删除资源页面元素集合
    '''
    def __init__(self):
        self.confirm_bt = AsyncElement('body > div.alertBox3 > div > div.content-wrapper > label > b.confirm-btn')  # 确定按钮
        self.success_tip = AsyncElement('.layui-layer-content')  # 操作成功提示框

