# -*- coding: utf-8 -*-
from API.base_api import check_response_data
from API.wbs.base_wbs_api import WBSAPIBaseTestMixin
import unittest
from nose.plugins.attrib import attr
from fake_data import FakeData


@attr('external')
class BatchRegisterTest(WBSAPIBaseTestMixin, unittest.TestCase):
    view_url = 'investor/batchRegister.json'
    fake = FakeData()
    mobile1 = fake.phone_number()
    mobile2 = fake.phone_number()
    data = 'data={"param":[{"mobile":' + mobile1 + ',"password":"6846860684f05029abccc09a53cd66f2"},{"mobile":' + mobile2 + ',"password":"6846860684f05029abccc09a53cd66f1"}]}'
    expected_response_format = {
        "success": bool,
        "msg": unicode,
        "data": [
            {
                "mobile": unicode,
                "success": bool
            }
        ]
    }

    @check_response_data
    def test_response_data(self):
        self.expected_response = {
            "success": True,
            "msg": u"操作成功",
            "errorCode": None,
            "data": [
                {
                    "mobile": self.mobile1,
                    "success": True,
                    "msg": None
                },
                {
                    "mobile": self.mobile2,
                    "success": True,
                    "msg": None
                }
            ]
        }
