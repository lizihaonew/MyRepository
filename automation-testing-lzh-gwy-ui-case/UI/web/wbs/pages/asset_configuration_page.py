# -*- coding: utf-8 -*-
import sys
import random
from fake_data import FakeData
from UI.base_page import BasePage
from ..elements.asset_configuration_elements import AddAssetConfigurationElementCollection, AssetConfigurationListElementCollection

reload(sys)
sys.setdefaultencoding("utf-8")


class AssetConfigurationPage(BasePage):
    view_url = '/html/assetAllocationManagement.html'

    def __init__(self, browser):
        self.add_asset_configuration = AddAssetConfigurationElementCollection()
        self.asset_configuration_list = AssetConfigurationListElementCollection()
        self.fake = FakeData()
        self.set_browser(browser)
        self.get_url()

    def select_product(self, product_number=1, index=0):
        self.add_asset_configuration.choose_product.click(index)
        self.switch_to_div_alert()
        for i in range(0, product_number):
            if product_number == 1:
                self.add_asset_configuration.product_checkbox.click(random.randint(0, 10))
            else:
                self.add_asset_configuration.product_checkbox.click(i)
        self.add_asset_configuration.confirm_product_selection.click()

    def new_asset_configuration(self, risk_type_index=0, category_number=1, product_number=1):
        self.asset_configuration_list.add_asset.click()
        risk_type_dict = {
            0: '保守型',
            1: '稳健型',
            2: '平衡型',
            3: '进取型',
            4: '激进型',
        }
        asset_name = '自动化测试{0}-----{1}'.format(risk_type_dict[risk_type_index], self.fake.text(max_length=5))
        self.add_asset_configuration.asset_name(asset_name.decode())
        asset_introduction = "自动化测试{0}资产配置介绍-----{1}".format(risk_type_dict[risk_type_index], self.fake.text(50))
        self.add_asset_configuration.asset_introduction(asset_introduction.decode())
        self.add_asset_configuration.asset_risk_type()[risk_type_index].click()
        if category_number >= 1:
            # We don't have one category added by default
            for i in range(0, category_number):
                self.add_asset_configuration.add_part.click()
        ratio = self.generate_rand(category_number, 100)
        for i in range(0, category_number):
            self.add_asset_configuration.asset_category('select_index={0}'.format(i+1), i)
            self.add_asset_configuration.ratio(value=ratio[i], index=i)
            self.select_product(product_number, i)
        self.add_asset_configuration.submit_add_button.click()
        self.asset_configuration_list.action_tip.wait_until_element_visible()
        self.asset_configuration_list.action_tip.wait_until_element_invisible()
        return asset_name

    def delete_asset_configuration(self, index=0):
        self.asset_configuration_list.delete.click(index=index)
        self.switch_to_div_alert()
        self.asset_configuration_list.confirm_delete.click()
        self.asset_configuration_list.action_tip.wait_until_element_visible()
        self.asset_configuration_list.action_tip.wait_until_element_invisible()

    def modify_asset_configuration(self, previous_asset_name, changed_asset_name=None, index=0):
        self.asset_configuration_list.modify.click(index=index)
        changed_asset_name = changed_asset_name or '{0}修改'.format(previous_asset_name)
        self.add_asset_configuration.asset_name(changed_asset_name.decode())
        self.add_asset_configuration.submit_add_button.click()
        self.asset_configuration_list.action_tip.wait_until_element_visible()
        self.asset_configuration_list.action_tip.wait_until_element_invisible()
        return changed_asset_name

    def query_asset_configuration(self, asset_name):
        self.asset_configuration_list.asset_allocation_name(asset_name.decode())
        with self.wait_for_page_load(self.asset_configuration_list.query_asset_name()[0]):
            self.asset_configuration_list.query_asset.click()
        query_asset_name = self.asset_configuration_list.query_asset_name
        return {
            'asset_name': [query_asset_name.get_text(index) for index in range(0, len(query_asset_name()))],
            'modify': self.asset_configuration_list.modify,
            'delete': self.asset_configuration_list.delete
        }

    def get_asset_configuration_names(self, index=0):
        return self.asset_configuration_list.query_asset_name.get_text(index)

    @staticmethod
    def generate_rand(n, sum_v):
        rand = []
        for i in range(0, n - 1):
            ran = random.randint(1, sum_v / n)
            rand.append(ran)
        rand.append(sum_v - sum(rand))

        return rand
