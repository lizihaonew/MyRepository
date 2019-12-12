# -*- coding: utf-8 -*-
import pytest
from nose.plugins.attrib import attr
from ..base_wbs_api import WBSAPIBaseTestMixin
import unittest
from fake_data import FakeData
import sys
import types

reload(sys)
sys.setdefaultencoding('utf-8')


@attr('internal')
@attr('externalopen')
class InvestorMyAssetsTest(WBSAPIBaseTestMixin, unittest.TestCase):
    phone = FakeData().phone_number()

    expected_response_format = {
        "success": bool,
        "msg": unicode,
        "errorCode": types.NoneType,
        "data": {
            "signAmount": float,
            "categoryPercent": [
                {
                    "name": unicode,
                    "value": int
                }
            ],
            "reservationCount": int,
            "messageCount": int,
            "surveyResult": unicode
        }
    }

    @classmethod
    def setUpClass(cls):
        cls.view_url = 'myAssetsIndex.json'
        token = cls.generate_investor_token()
        data_dict = {
            "token": token,
            "param": {}
        }
        cls.data = 'data={0}'.format(cls.dict_to_json(data_dict))
        super(InvestorMyAssetsTest, cls).setUpClass()
