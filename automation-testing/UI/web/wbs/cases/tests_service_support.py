#coding:utf-8
from UI.base_case import BaseUITestCase
from ..pages.service_support_page import ServiceSupportPage


class ServiceSupportTest(BaseUITestCase):

    def setUp(self):
        self.service_support_page = ServiceSupportPage(self.browser)

    def tests_service_support(self):
        self.assertEqual(self.service_support_page.add_service_support(),u'添加成功！')

    def tests_support_delete(self):
        self.assertEqual(self.service_support_page.service_delete(),u'删除成功！')
