# -*- coding: utf-8 -*-
from UI.base_page import BasePage
from ..elements.service_managent_element import ServiceManagent
from fake_data import FakeData
import random


class ServiceManagentPage(BasePage):

    view_url = '/html/productCategory.html'

    def __init__(self, browser):
        self.add_service_managent_elements = ServiceManagent()
        self.fake = FakeData()
        self.set_browser(browser)
        self.get_url()

    def add_service_managent(self, state=0, type=1):
        self.add_service_managent_elements.add_classify.click()
        self.add_service_managent_elements.add_managent_name(u'自动化新增 '+self.fake.text(max_length=5))
        self.add_service_managent_elements.add_managent_attribute('value={0}'.format(type))
        self.add_service_managent_elements.add_managent_confirm.click()
        return self.add_service_managent_elements.succeed_tip.get_text()



    def update_service_mangent(self,type=1):
        self.add_service_managent_elements.update.click(0)
        self.add_service_managent_elements.add_managent_name(u'自动化修改 '+self.fake.text(max_length=5))
        self.add_service_managent_elements.add_managent_confirm.click()
        return self.add_service_managent_elements.succeed_tip.get_text()

    def delete_sevice_mangent(self):
        self.add_service_managent_elements.delete.click(0)
        self.add_service_managent_elements.delete_confirm.click()
        return self.add_service_managent_elements.succeed_tip.get_text()

