# -*- coding: utf-8 -*-
from UI.browser import DriverSingleton
import unittest


class AssetConfigurationTest(unittest.TestCase):

    def setUp(self):
        self.driver = DriverSingleton().browser
        self.driver.start_activity('cn.newbanker', '.ui.loginandregist.LoginActivity')
        self.driver.find_elements_by_id('cn.newbanker:id/txtDescription')[0].click()
        self.driver.find_element_by_id('cn.newbanker:id/net_demo').click()
        self.driver.find_element_by_class_name('android.widget.Button').click()
        self.driver.find_elements_by_id('cn.newbanker:id/txtDescription')[1].click()
        self.driver.find_element_by_id('cn.newbanker:id/net_demo').click()
        self.driver.find_element_by_class_name('android.widget.Button').click()
        self.driver.find_element_by_id('cn.newbanker:id/et_phone').send_keys('18910345678')
        self.driver.find_element_by_id('cn.newbanker:id/et_pwd').send_keys('a111111')
        self.driver.find_element_by_id('cn.newbanker:id/btn_login').click()

    def test_asset_list(self):
        self.driver.find_element_by_android_uiautomator("text(\"资产配置\")").click()

    def tearDown(self):
        self.driver.quit()