#coding:utf-8
'''
作者：李子浩
内容：顾问云资源市场金融产品管理相关元素集合
'''

from UI.base_element import BaseElement,AsyncElement,ElementCollection
from UI.special_elements.select_element import SelectElement

class ProductListPageElements(ElementCollection):
    '''
    产品管理已发布页面相关元素集合
    '''
    def __init__(self):
        self.published_tab = AsyncElement('div.ibox-tab > a:nth-child(1)')  # 已发布tab按钮
        self.unpublished_tab = AsyncElement('div.ibox-tab > a:nth-child(2)')  # 未发布tab按钮
        self.add_product_bt = AsyncElement('div.ibox-tab > div > a:nth-child(1)')   # 新增产品按钮
        self.product_recording_bt = AsyncElement('div.ibox-tab > div > a:nth-child(2)')   # 企业获取产品记录按钮
        self.product_name_box = BaseElement('#pd_name') # 筛选条件中的产品名称
        self.product_category_select = SelectElement('#pd_category')    # 筛选条件中的产品属性
        self.product_status_select = SelectElement('#pd_state')     # 筛选条件中的产品状态
        self.product_type_select = SelectElement('#pd_release')     # 筛选条件中的二级分类
        self.query_bt = AsyncElement('#_query')     # 查询按钮
        self.first_row_id = AsyncElement('div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td:nth-child(1)')  # 列表第一行产品编号
        self.first_row_name = AsyncElement('div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td:nth-child(2) > a')    # 列表第一行产品名称
        self.first_row_category = AsyncElement('div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td:nth-child(3)')    # 列表第一行产品属性
        self.first_row_status = AsyncElement('div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td:nth-child(5)')      # 列表第一行产品状态
        self.first_row_type = AsyncElement('div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td:nth-child(8)')        # 列表第一行二级类别
        self.first_row_sort = AsyncElement('div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td:nth-child(9)')        # 列表第一行排序
        self.first_update_sort = AsyncElement('div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td:nth-child(10) > a:nth-child(1)')   # 列表第一行修改排序按钮
        self.first_revoked_publish = AsyncElement('div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td:nth-child(10) > a:nth-child(2)')   # 列表第一行撤销发布按钮
        self.first_row_update = AsyncElement('div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td:nth-child(10) > a:nth-child(3)')        # 列表第一行修改按钮
        self.first_record_publish = AsyncElement('div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td:nth-child(9) > a:nth-child(1)')     # 未发布页第一行发布按钮
        self.first_record_update = AsyncElement('div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td:nth-child(9) > a:nth-child(2)')      # 未发布页第一行修改按钮
        self.first_record_delete = AsyncElement('div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td:nth-child(9) > a:nth-child(3)')      # 未发布页第一行删除按钮


class ProductAddElements(ElementCollection):
    '''
    产品新增页面元素集合
    '''
    def __init__(self):
        self.category_select = SelectElement('.chosen-select.property-select')    # 产品属性
        self.type_select = SelectElement('.chosen-select.chosen-selectTwoType')     # 产品二级类别
        self.name_box = BaseElement('div.tabs1.titleTabs.ibox-content.ibox-content1 > form.form-horizontal.basic-form > div:nth-child(5) > div > input')    # 产品名称输入框
        self.comments_box = BaseElement('div.tabs1.titleTabs.ibox-content.ibox-content1 > form.form-horizontal.basic-form > div:nth-child(7) > div > input')    # 产品点评输入框
        self.init_investment = BaseElement('div.tabs1.titleTabs.ibox-content.ibox-content1 > form.form-horizontal.basic-form > div:nth-child(9) > div > input') # 起投金额
        self.product_term = BaseElement('div.tabs1.titleTabs.ibox-content.ibox-content1 > form.form-horizontal.basic-form > div:nth-child(11) > div > input')   # 产品期限
        self.expected_annual_return = BaseElement('div.tabs1.titleTabs.ibox-content.ibox-content1 > form.form-horizontal.basic-form > div:nth-child(13) > div > input') # 预期年化收益率
        self.product_status_select = SelectElement('.chosen-select.chosenstatus-select')    # 产品状态
        self.product_description = BaseElement('div.tabs1.titleTabs.ibox-content.ibox-content1 > form.form-horizontal.basic-form > div:nth-child(17) > div > div.note-editor.note-frame.panel.panel-default > div.note-editing-area > div.note-editable.panel-body') # 产品介绍
        self.bank_username = BaseElement('div.tabs1.titleTabs.ibox-content.ibox-content1 > form.form-horizontal.basic-form > div:nth-child(20) > div > input')  # 开户名
        self.bank_name = BaseElement('div.tabs1.titleTabs.ibox-content.ibox-content1 > form.form-horizontal.basic-form > div:nth-child(21) > div > input')  # 募集银行
        self.bank_number = BaseElement('div.tabs1.titleTabs.ibox-content.ibox-content1 > form.form-horizontal.basic-form > div:nth-child(22) > div > input')    # 募集账号
        self.customer_pay_notes = BaseElement('div.tabs1.titleTabs.ibox-content.ibox-content1 > form.form-horizontal.basic-form > div:nth-child(23) > div > input') # 客户打款备注
        self.product_sort = BaseElement('div.tabs1.titleTabs.ibox-content.ibox-content1 > form.form-horizontal.basic-form > div:nth-child(25) > div > input')   # 产品排序
        self.back_bt = AsyncElement('.btn.btn-Cancel')  # 返回按钮
        self.first_page_confirm = AsyncElement('.btn.btn-Save') # 保存&下一步按钮
        self.small_img = BaseElement('#marketInfo > div:nth-child(3) > div > div > span.btn.btn-default.btn-file > input[type="file"]') # 产品小图上传入口
        self.big_img = BaseElement('#marketInfo > div:nth-child(5) > div > div > span.btn.btn-default.btn-file > input[type="file"]')   # 产品大图上传入口
        self.second_confirm = AsyncElement('#marketInfo > div:nth-child(11) > div > div.btn.btn-Save')  # 第二页的保存按钮
        self.add_attachment = AsyncElement('div.tabs3.titleTabs.ibox-content.ibox-content3 > div.ibox-create.ibox-create-re > a:nth-child(1)')  # 添加附件按钮
        self.attachment_type_select = SelectElement('#addAttachmentForm > div.form-group.form-group-50 > div > select')  # 选择附件类型
        self.attachment_send_box = BaseElement('#contactAttachments')   # 上传附件入口
        self.inner_customer = AsyncElement('#innerCustomer')    # 附件可见范围复选框(内部理财顾问)
        self.attachment_confirm_bt = AsyncElement('#addAttachmentForm > div.form-group.form-group-btn.form-group-btns > div > div.btn.btn-Save')    # 确定按钮
        self.third_next_bt = AsyncElement('div.tabs3.titleTabs.ibox-content.ibox-content3 > div.ibox-create.ibox-create-re > a:nth-child(2)')   # 第三页下一步按钮
        self.discount_rate = BaseElement('#addCompany4 > div:nth-child(1) > div > input')   # 产品折标率
        self.inner_commission_rate = BaseElement('#addCompany4 > div:nth-child(3) > div > input')   # 内部理财顾问佣金分成比例
        self.outer_commission_rate = BaseElement('#addCompany4 > div:nth-child(5) > div > input')   # 外部独立理财顾问佣金分成比例
        self.forth_confirm_bt = AsyncElement('#addCompany4 > div:nth-child(7) > div > div.btn.btn-Save')    # 确定按钮


class UnpublishedUpdateElement(ElementCollection):
    '''
    未发布列表修改页面元素集合
    '''
    def __init__(self):
        self.product_name = BaseElement('div.tabs1.titleTabs.ibox-content.ibox-content-show.ibox-content1 > form.form-horizontal.basic-form > div:nth-child(5) > div > input')  # 产品名称输入框
        self.confirm_bt = AsyncElement('div.tabs1.titleTabs.ibox-content.ibox-content-show.ibox-content1 > form.form-horizontal.basic-form > div:nth-child(27) > div > div.btn.btn-Save')   # 保存按钮
        self.back_bt = AsyncElement('#marketInfo > div:nth-child(11) > div > div.btn.btn-Cancel')   # 修改页面第二页返回按钮


class PublishElement(ElementCollection):
    '''
    未发布列表发布页面元素集合
    '''
    def __init__(self):
        self.sort_box = BaseElement('body > section > div.alertBox3.alert-no > div > div.content-wrapper.content-nowrapper > label:nth-child(1) > input[type="number"]')    # 排序值输入框
        self.confirm_bt = AsyncElement('body > section > div.alertBox3.alert-no > div > div.content-wrapper.content-nowrapper > label.alert-btn > b.confirm-btn')   # 确定按钮


class UpdateSortElement(ElementCollection):
    '''
    已发布列表修改排序页面元素集合
    '''
    def __int__(self):
        self.sort_box = BaseElement('body > section > div.alertBox3.alert-no > div > div.content-wrapper.content-nowrapper > label:nth-child(1) > input[type="text"]')  # 排序值输入框
        self.confirm_bt = AsyncElement('body > section > div.alertBox3.alert-no > div > div.content-wrapper.content-nowrapper > label.alert-btn > b.confirm-btn')   # 确定按钮


class PublishedUpdateElement(ElementCollection):
    '''
    已发布列表修改页面元素集合
    '''
    def __init__(self):
        self.second_type = SelectElement('div.tabs1.titleTabs.ibox-content.ibox-content-show.ibox-content1 > form.form-horizontal.basic-form > div:nth-child(3) > div > select')    # 二级类别下拉框
        self.product_name = BaseElement('div.tabs1.titleTabs.ibox-content.ibox-content-show.ibox-content1 > form.form-horizontal.basic-form > div:nth-child(5) > div > input')  # 产品名称输入框
        self.confirm_bt = AsyncElement('div.tabs1.titleTabs.ibox-content.ibox-content-show.ibox-content1 > form.form-horizontal.basic-form > div:nth-child(27) > div > div.btn.btn-Save') # 保存按钮
        self.back_bt = AsyncElement('#marketInfo > div:nth-child(11) > div > div.btn.btn-Cancel')   # 修改页面第二页返回按钮


class ProductDetail(ElementCollection):
    '''
    金融产品详情页查询
    '''
    def __init__(self):
        self.product_name = AsyncElement('div.tabs1.titleTabs.ibox-content.ibox-content-show.ibox-content1 > div.form-horizontal.basic-form > div:nth-child(5) > div > span')   # 详情页产品名称


class RevokePublishElement(ElementCollection):
    '''
    撤销发布页面元素集合
    '''
    def __init__(self):
        self.confirm_bt = AsyncElement('body > section > div.alertBox4 > div > div.content-wrapper > label > b.confirm-btn')    # 确认按钮
        self.cancel_bt = AsyncElement('body > section > div.alertBox4 > div > div.content-wrapper > label > b.cancel-btn')      # 取消按钮


class DeleteElement(ElementCollection):
    '''
    删除页面元素集合
    '''
    def __init__(self):
        self.confirm_bt = AsyncElement('body > section > div.alertBox4 > div > div.content-wrapper > label > b.confirm-btn')    # 确认按钮
        self.cancel_bt = AsyncElement('body > section > div.alertBox4 > div > div.content-wrapper > label > b.cancel-btn')      # 取消按钮

