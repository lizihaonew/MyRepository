# -*- coding: utf-8 -*-
import pytest
from nose.plugins.attrib import attr
from API.base_api import check_response_data
from API.wbs.base_wbs_api import WBSAPIBaseTestMixin
import unittest
from fake_data import FakeData
import sys
import types

reload(sys)
sys.setdefaultencoding('utf-8')


@attr('internal')
#@attr('externalopen') 此接口从2.0不对外开放了
class InvestorCheckAuthCodeTest(WBSAPIBaseTestMixin, unittest.TestCase):
    phone = FakeData().phone_number()

    expected_response_format = {
        "success": bool,
        "msg": unicode,
        "errorCode": types.NoneType
    }

    @check_response_data
    def test_response_data_with_error_type(self):
        data_dict = {
            "param": {
                "mobile": self.phone,
                "type": "100121",
                "authCode": "1827"
            }
        }
        data = 'data={0}'.format(self.dict_to_json(data_dict))
        self.response = self.do_request(data)
        self.expected_response = {
            "msg": u"无效验证码类型！"
        }

    @check_response_data
    def test_response_data_with_empty_type(self):
        data_dict = {
            "param": {
                "mobile": self.phone,
                "type": "100",
                "authCode": ""
            }
        }
        data = 'data={0}'.format(self.dict_to_json(data_dict))
        self.response = self.do_request(data)
        self.expected_response = {
            "msg": u"验证码不能为空！"
        }

    @classmethod
    def setUpClass(cls):
        cls.view_url = 'checkAuthCode.json'
        data_dict = {
            "param": {
                "mobile": cls.phone,
                "type": "100",
                "authCode": "1827"
            }
        }
        cls.data = 'data={0}'.format(cls.dict_to_json(data_dict))
        super(InvestorCheckAuthCodeTest, cls).setUpClass()
