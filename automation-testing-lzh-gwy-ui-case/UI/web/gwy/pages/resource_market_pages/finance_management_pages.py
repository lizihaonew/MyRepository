#coding:utf-8
'''
作者：李子浩
内容：顾问云资源市场金融产品管理相关page类
'''

from UI.base_page import BasePage
from ...elements.resource_market_elements.finance_management_elements import ProductListPageElements, ProductAddElements, RevokePublishElement, DeleteElement, ProductDetail
from ...elements.resource_market_elements.finance_management_elements import UnpublishedUpdateElement, PublishElement, UpdateSortElement, PublishedUpdateElement
import random

class FinanceMangementPages(BasePage):

    view_url = r'/html/financialProductManagement.html'
    product_add_name = 'AutoTestAdd' + str(random.randint(1, 99)).zfill(3)
    small_img_path = r'..\..\..\file\timg.jpeg'
    big_img_path = r'..\..\..\file\timg.jpeg'
    attachment_path = r'..\..\..\file\test_file.pdf'
    product_update_name1 = 'AutoTestUpdate1' + str(random.randint(1, 99)).zfill(3)
    product_update_name2 = 'AutoTestUpdate2' + str(random.randint(1, 99)).zfill(3)

    def __init__(self, browser):
        self.product_list = ProductListPageElements()
        self.product_add = ProductAddElements()
        self.unpublished_update = UnpublishedUpdateElement()
        self.publish = PublishElement()
        self.update_sort = UpdateSortElement()
        self.published_update = PublishedUpdateElement()
        self.product_detail = ProductDetail()
        self.revoke_publish = RevokePublishElement()
        self.product_delete = DeleteElement()
        self.set_browser(browser)
        self.get_url()

    def do_add_product(self):
        '''
        新增金融产品操作
        :return: 未发布列表第一行的产品名称
        '''
        self.product_list.add_product_bt.click()
        self.product_add.category_select('index=1')
        self.product_add.type_select('index=1')
        self.product_add.name_box(self.product_add_name)
        self.product_add.comments_box('This is a good product')
        self.product_add.init_investment(1000)
        self.product_add.product_term(u'最长24个月')
        self.product_add.expected_annual_return('15%')
        self.product_add.product_status_select('index=1')
        self.product_add.product_description('This is a good product, add just sell it!')
        self.product_add.bank_username('Whatever bank username')
        self.product_add.bank_name('Whatever bank name')
        self.product_add.bank_number('12345678998752')
        self.product_add.customer_pay_notes('Whatever pay notes')
        self.product_add.product_sort(9999)
        self.product_add.first_page_confirm.click()
        self.product_add.small_img(self.small_img_path, file_type=True)
        self.product_add.big_img(self.big_img_path, file_type=True)
        self.product_add.second_confirm.click()
        self.wait_for_page_load()
        self.product_add.add_attachment.click()
        self.product_add.attachment_type_select('index=1')
        self.product_add.attachment_send_box(self.attachment_path, file_type=True)
        self.product_add.inner_customer.click()
        self.product_add.attachment_confirm_bt.click()
        self.wait_for_page_load()
        self.refresh_page()
        self.product_add.third_next_bt.click()
        self.product_add.discount_rate(10)
        self.product_add.inner_commission_rate(10)
        self.product_add.outer_commission_rate(10)
        self.product_add.forth_confirm_bt.click()
        self.wait_for_page_load()
        return self.product_list.first_row_name.get_text()

    def do_unpublished_update(self):
        '''
        未发布列表第一行修改
        :return: 修改后的第一行的产品名称
        '''
        self.product_list.unpublished_tab.click()
        self.product_list.first_record_update.click()
        self.unpublished_update.product_name(self.product_update_name1)
        self.unpublished_update.confirm_bt.click()
        self.unpublished_update.back_bt.click()
        return self.product_list.first_row_name.get_text()

    def do_publish(self):
        '''
        未发布列表第一行数据发布
        :return: 已发布列表第一行数据的产品名称
        '''
        self.product_list.unpublished_tab.click()
        self.product_list.first_record_publish.click()
        self.publish.sort_box(9998)
        self.publish.confirm_bt.click()
        self.wait_for_page_load()
        # time.sleep(2)
        self.wait_success_tip_invisible()
        self.product_list.published_tab.click()
        self.refresh_page()
        return self.product_list.first_row_name.get_text()

    def do_sort_update(self):
        '''
        已发布列表修改排序
        :return: 修改后的排序号
        '''
        self.product_list.first_update_sort.click()
        self.update_sort.sort_box(9997)
        self.update_sort.confirm_bt.click()
        self.refresh_page()
        return self.product_list.first_row_sort.get_text()

    def do_published_update(self):
        '''
        已发布列表修改操作
        :return:修改后的产品名称
        '''
        self.product_list.first_row_update.click()
        self.published_update.second_type('index=1')
        self.published_update.product_name(self.product_update_name2)
        self.published_update.confirm_bt.click()
        self.published_update.back_bt.click()
        self.refresh_page()
        return self.product_list.first_row_name.get_text()

    def do_product_detail(self):
        '''
        查看金融产品详情页
        :return: 金融产品详情页中金融产品名称
        '''
        self.product_list.first_row_name.click()
        return self.product_detail.product_name.get_text()

    def do_revoke_publish(self):
        '''
        撤销发布操作
        :return: 未发布列表第一行产品名称
        '''
        self.product_list.first_revoked_publish.click()
        self.revoke_publish.confirm_bt.click()
        # time.sleep(2)
        self.wait_success_tip_invisible()
        self.product_list.unpublished_tab.click()
        self.refresh_page()
        return self.product_list.first_row_name.get_text()

    def do_product_delete(self):
        '''
        删除金融产品
        :return: 未发布列表第一行产品名称
        '''
        self.product_list.unpublished_tab.click()
        self.product_list.first_record_delete.click()
        self.product_delete.confirm_bt.click()
        self.refresh_page()
        return self.product_list.first_row_name.get_text()




