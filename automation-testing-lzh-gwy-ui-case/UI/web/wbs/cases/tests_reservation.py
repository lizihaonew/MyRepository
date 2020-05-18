# -*- coding: utf-8 -*-
from UI.base_case import BaseUITestCase
from ..pages.reservation_page import ReservationPage
import sys

reload(sys)
sys.setdefaultencoding('utf8')


class ReservationTest(BaseUITestCase):

    def setUp(self):
        self.reservation_page = ReservationPage(self.browser)

    def tests_reservation_search(self):
        status_list = [u'预约服务不成功', u'待咨询顾问受理', u'受理中(待审核)', u'受理中(待签约)', u'已签约']
        for status in status_list:
            queried_status = self.reservation_page.search_reservation(status)
            for q_status in queried_status:
                self.assertIn(status, q_status)
