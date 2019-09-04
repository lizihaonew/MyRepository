# -*- coding: utf-8 -*-
from ..base_wbs_api import WBSAPIBaseTestMixin
import unittest, time
import requests


class ReserveProductTest(WBSAPIBaseTestMixin, unittest.TestCase):
    view_url = '/ex/open/investor/reserveProduct.json'
    expected_response_format = {
        "success": bool,
        "msg": unicode,
        "errorCode": None
    }

    @classmethod
    def setUpClass(cls):

        cls.data = 'data={"token":' \
                   '"ded7e335-37bd-4a76-a388-a1fd24f145bc",' \
                   '"param":{' \
                   '"productId":"79",' \
                   '"reservationAmount":"100",' \
                   '"reservationDate":%s,' % time.strftime('%Y-%m-%d', time.localtime()) + \
                   '"memo":"123456123"}}'
        super(InvestorSearchTest, cls).setUpClass()


