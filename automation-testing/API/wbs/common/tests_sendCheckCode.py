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
class InvestorSendCheckCodeTest(WBSAPIBaseTestMixin, unittest.TestCase):
    phone = FakeData().phone_number()

    expected_response_format = {
        "success": bool,
        "msg": unicode,
        "errorCode": types.NoneType,
    }

    @check_response_data
    def test_response_data_with_error_type(self):
        data_dict = {
            "param": {
                "mobile": self.phone,
                "type": "10231"
            }
        }
        data = 'data={0}'.format(self.dict_to_json(data_dict))
        self.response = self.do_request(data)
        self.expected_response = {
            "msg": u"无效验证码类型！"
        }

    @classmethod
    def setUpClass(cls):
        cls.view_url = 'sendCheckCode.json'
        data_dict = {
            "param":
                {
                    "mobile": cls.phone,
                    "type": "100"
                }
        }
        cls.data = 'data={0}'.format(cls.dict_to_json(data_dict))
        super(InvestorSendCheckCodeTest, cls).setUpClass()
