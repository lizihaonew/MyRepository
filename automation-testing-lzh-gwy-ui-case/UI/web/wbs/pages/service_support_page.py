# -*- coding: utf-8 -*-
from UI.base_page import BasePage
from ..elements.service_support_elements import ServiceSupport
from fake_data import FakeData
import random


class ServiceSupportPage(BasePage):

    view_url = '/html/backup.html'

    def __init__(self, browser):
        self.service_support_elements = ServiceSupport()
        self.fake = FakeData()
        self.set_browser(browser)
        self.get_url()

    def add_service_support(self, state=0):
        self.service_support_elements.service_support_add.click()
        self.service_support_elements.service_support_add_department(u'自动化 '+self.fake.text(max_length=5))
        self.service_support_elements.service_support_add_phone('010-12345'+str(random.randint(100, 999)))
        self.service_support_elements.service_support_add_clientele.click()
        self.service_support_elements.service_support_add_interior.click()
        self.service_support_elements.service_support_add_independent.click()
        self.service_support_elements.service_support_add_confirm.click()
        return self.service_support_elements.succeed_tip.get_text()

    def service_delete(self,type=-1):
        self.service_support_elements.service_support_add_delete.click(type)
        self.service_support_elements.service_support_add_delete_ok.click()
        return self.service_support_elements.succeed_tip.get_text()
