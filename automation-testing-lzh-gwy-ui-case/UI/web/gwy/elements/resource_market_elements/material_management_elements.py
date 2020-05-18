#coding:utf-8
'''
作者：李子浩
内容：顾问云资源市场管理模块下素材管理相关元素集合
'''

from UI.base_element import BaseElement, AsyncElement, ElementCollection
from UI.special_elements.select_element import SelectElement

class MaterialListElements(ElementCollection):
    '''
    素材管理列表页相关元素集合
    '''
    def __init__(self):
        self.add_bt = AsyncElement('#page-wrapper > div > div > div > div > div.ibox-tab > div > a')    # 新增内容按钮
        self.title_box = BaseElement('#cp_name')    # 标题筛选项
        self.second_type = SelectElement('#pd_category')    # 二级类别筛选项
        self.query_bt = AsyncElement('#_query')     # 查询按钮
        self.first_row_title = AsyncElement(
            'div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td:nth-child(1)')   # 列表页第一条数据标题
        self.first_row_type = AsyncElement(
            'div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td:nth-child(2)')   # 列表页第一条数据二级类别
        self.first_row_update = AsyncElement(
            'div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td:nth-child(5) > a:nth-child(1)')  # 列表页第一条数据修改按钮
        self.first_row_delete = AsyncElement(
            'div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td:nth-child(5) > a:nth-child(2)')  # 列表页第一条数据删除按钮


class MaterialAddElements(ElementCollection):
    '''
    素材新增编辑页面元素集合
    '''
    def __init__(self):
        self.second_type = SelectElement('#materialForm > div.form-group.form-group-20 > div > select') # 二级类别
        self.title_box = BaseElement('#materialForm > div.form-group.form-group-50 > div > input')  # 标题
        self.file_post = BaseElement('#materialForm > div:nth-child(8) > div > div > input[type="file"]')   # 上传素材包
        self.img_post = BaseElement(
            '#materialForm > div:nth-child(10) > div > div > span.btn.btn-default.btn-file > input[type="file"]')    # 上传图片
        self.price_box = BaseElement('#materialForm > div.form-group.form-group20 > div > input')   # 价格
        self.confirm_bt = AsyncElement('.btn.btn-Save')     # 确定按钮
        self.file_success_return = '#modifyFileBtn'


class MaterialUpdateElements(ElementCollection):
    '''
    素材修改页面元素集合
    '''
    def __init__(self):
        self.title_box = BaseElement('#materialForm > div.form-group.form-group-50 > div > input')  # 标题
        self.confirm_bt = AsyncElement('.btn.btn-Save')     # 确定按钮


class MaterialDeleteElements(ElementCollection):
    '''
    素材删除页面元素集合
    '''
    def __init__(self):
        self.confirm_bt = AsyncElement('body > div.alertBox3 > div > div.content-wrapper > label > b.confirm-btn')  # 确定按钮
        self.success_tip = AsyncElement('.layui-layer-content')     # 操作成功提示框


