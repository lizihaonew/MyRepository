# -*- coding: utf-8 -*-
from UI.base_element import BaseElement, AsyncElement, ElementCollection
from UI.special_elements.select_element import SelectElement


class ProductSearchElements(ElementCollection):

    def __init__(self):
        self.product_name = AsyncElement('#pd_name')
        self.product_category = SelectElement('#pd_category')
        self.product_state = SelectElement('#pd_state')
        self.product_release = SelectElement('#pd_release')
        self.product_query = AsyncElement('#_query')


class ProductListElements(ElementCollection):

    def __init__(self):
        self.product_name = AsyncElement('.gradeX td:nth-child(2)')
        self.product_category = AsyncElement('.gradeX td:nth-child(3)')
        self.product_status = AsyncElement('.gradeX td:nth-child(5)')
        self.product_release = AsyncElement('.gradeX td:nth-child(6)')
        self.product_del = AsyncElement('._delete')
        self.product_update = AsyncElement('.pd_update')
        self.product_check_reservation = AsyncElement('.check_reservation')
        self.product_stand_up_down = AsyncElement('.stand_up_down')
        self.product_information_disclosure = AsyncElement('.information_disclosure')
        self.product_copy_links = AsyncElement('.copy_pd_links')
        self.product_add = AsyncElement('#add_product')


class ProductPropertyElements(ElementCollection):

    def __init__(self):
        # 产品基本信息元素#
        self.product_category = SelectElement('#pd_category')
        self.product_name = AsyncElement('#pd_name')
        self.product_opinion = AsyncElement('#pd_opinion')
        self.product_currency = SelectElement('#pd_currency')
        self.product_investment_amount = AsyncElement('#pd_investment_amount')
        self.product_deadline = AsyncElement('#pd_deadline')
        self.product_annual_yield = AsyncElement('#pd_annual_yield')
        self.product_netValue = AsyncElement('#pd_netValue')
        self.product_status = SelectElement('#pd_status')
        self.product_risk = AsyncElement('input[name="risk"]')
        self.product_riskTolerance = AsyncElement('input[class^="riskTolerance"]')
        # 产品介绍（富文本）#
        self.product_introduction = AsyncElement('.note-editable.panel-body')
        self.product_account_name = AsyncElement('#account_name')
        self.product_raise_bank = AsyncElement('#raise_bank')
        self.product_raise_account = AsyncElement('#raise_account')
        self.product_remark = AsyncElement('#remark')
        self.product_seq = AsyncElement('#pd_sequencing')
        self.product_cancel = AsyncElement('#go_back2')
        self.product_next_step1 = AsyncElement('#next_step')
        # 以下5个元素为营销信息#
        self.product_smallPicFile = AsyncElement('#smallPicFile')
        self.product_bigPicFile = AsyncElement('#bigPicFile')
        # 产品营销文案
        self.product_marketing_copy = AsyncElement('#product_content')
        # 风险提示富文本
        self.product_risk_warning = AsyncElement('.note-editable.panel-body')
        self.product_next_step2 = AsyncElement('#next_step2')
        # 以下元素为产品附件#
        self.product_add_attachment = AsyncElement('#add_product')
        self.product_attachment_type = AsyncElement('[name="adjunct_type"]')
        self.product_attachment_file = AsyncElement('[name="adjunct_file"]')
        self.product_attachment_visible_range_customer = AsyncElement('[name="_clientele"]')
        self.product_attachment_visible_range_employee = AsyncElement('[name="_interior"]')
        self.product_attachment_visible_range_fa = AsyncElement('[name="_independent"]')
        self.product_next_step3 = AsyncElement('#next_step3')
        # 以下元素为产品佣金配置
        self.product_productrate = AsyncElement('#productRate')
        self.product_commissionRate = AsyncElement('#commissionRate')
        self.product_independCommissionRatee = AsyncElement('#independCommissionRate')
        self.product_next_step4 = AsyncElement('#next_step4')
        # 统一使用一个返回
        self.product_go_back = AsyncElement('#go_back')
        # 修改时用到的属性
        self.product_update_introduction = AsyncElement('#tab-1 .note-editable.panel-body')
        self.product_update_risk_warning = AsyncElement('#tab-2 .note-editable.panel-body')
        self.product_update_next_step1 = AsyncElement('#next_step')
        self.product_update_next_step2 = AsyncElement('#__next_step2')
        self.product_update_next_step4 = AsyncElement('#next_step4')
        self.product_update_product_name = AsyncElement('.col-sm-10')
        # 弹框
        self.product_js_tip = AsyncElement('.content.js-tip')


class ProductViewElements(ElementCollection):

    def __init__(self):
        self.product_view = AsyncElement('div[id="tab-1"] .col-sm-2')
