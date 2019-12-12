# -*- coding: utf-8 -*-
import pytest
from nose.plugins.attrib import attr
from API.base_api import check_response_data
from ..base_wbs_api import WBSAPIBaseTestMixin
import unittest
from fake_data import FakeData
import sys
import types

reload(sys)
sys.setdefaultencoding('utf-8')


@attr('internal')
@attr('externalopen')
class InvestorChangePasswordTest(WBSAPIBaseTestMixin, unittest.TestCase):
    phone = FakeData().phone_number()

    expected_response_format = {
        "success": bool,
        "msg": unicode,
        "errorCode": types.NoneType
    }

    @check_response_data
    def test_response_data_with_error_pass(self):
        data_dict = {
            "token": self.generate_investor_token(),
            "param":
                {
                    "oldPassword": "68468684f05029abccc09a53cd66f1",
                    "password": "6846860684f05029abccc09a53cd66f1"
                }
        }
        data = 'data={0}'.format(self.dict_to_json(data_dict))
        self.response = self.do_request(data)
        self.expected_response = {
            "msg": u"原密码不正确!"
        }

    @classmethod
    def setUpClass(cls):
        cls.view_url = 'changePassword.json'
        data_dict = {
            "token": cls.generate_investor_token(),
            "param": {
                "oldPassword": "6846860684f05029abccc09a53cd66f1",
                "password": "6846860684f05029abccc09a53cd66f1"
            }
        }
        cls.data = 'data={0}'.format(cls.dict_to_json(data_dict))
        super(InvestorChangePasswordTest, cls).setUpClass()
