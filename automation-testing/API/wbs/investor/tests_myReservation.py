# -*- coding: utf-8 -*-
import pytest
from nose.plugins.attrib import attr
from API.base_api import check_response_data
from ..base_wbs_api import WBSAPIBaseTestMixin
import unittest
from fake_data import FakeData
import sys
import types
import random

reload(sys)
sys.setdefaultencoding('utf-8')


@attr('internal')
@attr('externalopen')
class InvestorMyReservationTest(WBSAPIBaseTestMixin, unittest.TestCase):
    phone = FakeData().phone_number()

    expected_response_format = {
        "success": bool,
        "msg": unicode,
        "errorCode": types.NoneType,
        "data": [
            {
                "id": int,
                "productId": int,
                "reservationDate": int,
                "reservationAmount": float,
                "currentUnit": unicode,
                "productName": unicode,
                "customerName": unicode,
                "mobile": unicode,
                "no": unicode,
                "signAmount": float,
                "term": unicode,
                "memo": unicode,
                "status": int,
                "performanceDate": int,
                "createTime": int,
                "statusStr": unicode,
                "faId": int,
                "ifaId": int,
                "entId": int,
                "contractNo": unicode,
                "currency": int,
                "categoryProperty": int,
                "deptCode": unicode,
                "signDate": int,
                "documentNo": unicode,
                "reserveSource": int,
                "ifaName": unicode
            }
        ]
    }

    @classmethod
    def setUpClass(cls):
        cls.view_url = 'myReservation.json'
        token = cls.generate_investor_token()
        value = random.randint(0, 3)
        data_dict = {
            "token": token,
            "param": {
                "value": value
            }
        }
        cls.data = 'data={0}'.format(cls.dict_to_json(data_dict))
        super(InvestorMyReservationTest, cls).setUpClass()
