# -*- coding: utf-8 -*-
from UI.base_page import BasePage
from ..elements.service_configuration_elements import ServiceCongigurarion
from fake_data import FakeData
import random


class ServiceCongiguiationPage(BasePage):

    view_url = '/html/productRiskAssessment.html'

    def __init__(self, browser):
        self.add_service_configuration_elements = ServiceCongigurarion()
        self.fake = FakeData()
        self.set_browser(browser)
        self.get_url()

    def add_service_configuration(self, state=0):
        self.add_service_configuration_elements.add_configurarion.click()
        self.add_service_configuration_elements.add_configurarion_rank(u'自动化'+self.fake.text(max_length=5))
        self.add_service_configuration_elements.add_configurarion_sort("99")
        self.add_service_configuration_elements.add_configurarion_remark(u'自动化备注'+self.fake.text(max_length=20))
        self.add_service_configuration_elements.add_configurarion_confirm.click()
        return self.add_service_configuration_elements.succeed_tip.get_text()

    def update_service_configuration(self):
        self.add_service_configuration_elements.update.click(0)
        self.add_service_configuration_elements.add_configurarion_rank(u'修改'+self.fake.text(max_length=6))
        self.add_service_configuration_elements.add_configurarion_sort("99")
        self.add_service_configuration_elements.add_configurarion_remark(u'修改备注'+self.fake.text(max_length=20))
        self.add_service_configuration_elements.add_configurarion_confirm.click()
        return self.add_service_configuration_elements.succeed_tip.get_text()

    def delete_sevice_configuration(self):
        self.add_service_configuration_elements.delete.click()
        self.add_service_configuration_elements.delete_confirm.click()
        return self.add_service_configuration_elements.succeed_tip.get_text()


