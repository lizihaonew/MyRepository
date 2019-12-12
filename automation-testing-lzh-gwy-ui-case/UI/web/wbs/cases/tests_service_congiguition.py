# -*- coding: utf-8 -*-
from UI.base_case import BaseUITestCase
from ..pages.service_congiguiation_page import ServiceCongiguiationPage


class ServiceCongigurartionTest(BaseUITestCase):

    def setUp(self):
        self.service_conigurtion_page = ServiceCongiguiationPage(self.browser)

    def tests_a_add_service_conigurtion(self):
        self.assertEqual(self.service_conigurtion_page.add_service_configuration(),u'添加成功！')

    def tests_b_uptate_service_conigrtion(self):
        self.assertEqual(self.service_conigurtion_page.update_service_configuration(),u'修改成功！')

    def tests_c_delete_service_conigrtion(self):
        self.assertEqual(self.service_conigurtion_page.delete_sevice_configuration(),u'删除成功！')

