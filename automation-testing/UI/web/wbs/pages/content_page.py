# -*- coding: utf-8 -*-
from UI.base_page import BasePage
from ..elements.content_elements import InformationAddElements, InformationListElements, VisibilityScopeElements
from fake_data import FakeData


class InformationPage(BasePage):

    view_url = '/html/informationManagement.html'

    def __init__(self, browser):
        self.information_list_elements = InformationListElements()
        self.information_add_elements = InformationAddElements()
        self.visibility_scope_elements = VisibilityScopeElements()
        self.fake = FakeData()
        self.set_browser(browser)
        self.get_url()

    def new_information(self):
        self.information_list_elements.add_information.click()
        self.information_add_elements.title(u'自动化添加资讯'+self.fake.text(max_length=5))
        self.information_add_elements.author(self.fake.user_name())
        self.information_add_elements.summary(u'自动化资讯简介'+self.fake.text(max_length=50))
        self.information_add_elements.content(u'自动化资讯内容'+self.fake.text(max_length=100))
        self.information_add_elements.pic_attach("/Users/tommy/desktop/DesiredCapabilities.png")
        self.visibility_scope_elements.outer_consultant_scope.click()
        #FIXME click does not work here, WHY?
        self.information_add_elements.confirm.click()
