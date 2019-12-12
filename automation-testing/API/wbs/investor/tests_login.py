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
class InvestorLoginTest(WBSAPIBaseTestMixin, unittest.TestCase):
    phone = FakeData().phone_number()

    expected_response_format = {
        "success": bool,
        "msg": unicode,
        "errorCode": types.NoneType,
        # "data": {
        #       "id": int,
        #      "entId": int,
        #   }
    }

    @check_response_data
    def test_response_data_with_error_phone(self):
        phone = random.randint(1828288, 18282882)
        data_dict = {
            "param":
                {"mobile": phone,
                 "password": "6846860684f05029abccc09a53cd66f1"
                 }
        }
        data = 'data={0}'.format(self.dict_to_json(data_dict))
        self.response = self.do_request(data)
        self.expected_response = {
            "msg": u"账号或密码错误！"
        }

    @check_response_data
    def test_response_data_with_three_times_error_phone(self):
        phone = random.randint(18282882, 182828821)
        data_dict = {
            "param":
                {"mobile": phone,
                 "password": "6846860684f05029abccc09a53cd66f1"
                 }
        }
        data = 'data={0}'.format(self.dict_to_json(data_dict))
        for i in range(0, 4):
            self.response = self.do_request(data)
        self.expected_response = {
            "msg": u"验证码为空！"
        }

    @check_response_data
    def test_response_data_with_six_times_error_phone(self):
        phone = random.randint(18282882, 182828821)
        data_dict = {
            "param": {
                "mobile": phone,
                "password": "6846860684f05029abccc09a53cd66f1"
            }
        }
        data = 'data={0}'.format(self.dict_to_json(data_dict))
        for i in range(0, 6):
            self.response = self.do_request(data)
        self.expected_response = {
            "msg": u"账号被锁定!"
        }

    @classmethod
    def setUpClass(cls):
        cls.view_url = 'register.json'
        data_dict = {
            "param": {
                "mobile": cls.phone,
                "authCode": "1234",
                "password": "6846860684f05029abccc09a53cd66f1"
            }
        }
        cls.data = 'data={0}'.format(cls.dict_to_json(data_dict))
        super(InvestorLoginTest, cls).setUpClass()
        cls.view_url = 'login.json'
        data_dict = {
            "param":
                {"mobile": cls.phone,
                 "captcha": "1234",
                 "password": "6846860684f05029abccc09a53cd66f1"
                 }
        }
        cls.data = 'data={0}'.format(cls.dict_to_json(data_dict))
        super(InvestorLoginTest, cls).setUpClass()
