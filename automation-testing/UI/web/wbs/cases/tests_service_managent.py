# -*- coding: utf-8 -*-
from UI.base_case import BaseUITestCase
from ..pages.service_managent_page import ServiceManagentPage

class ServiceCongigurartionTest(BaseUITestCase):

    def setUp(self):
        self.service_mangent_page = ServiceManagentPage(self.browser)

    # def tests_add_service_managent(self):
    #     self.service_mangent_page.add_service_managent(1)

    def tests_a_add_service_managent_calss(self):
        self.assertEqual(self.service_mangent_page.add_service_managent(), u'添加成功！')

    def tests_b_update_service_managent(self):
        self.assertEqual(self.service_mangent_page.update_service_mangent(),u'修改成功！')

    def tests_c_delete_service_managent(self):
        self.assertEqual(self.service_mangent_page.delete_sevice_mangent(),u'删除成功！')

