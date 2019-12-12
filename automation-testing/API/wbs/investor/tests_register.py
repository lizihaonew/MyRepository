# -*- coding: utf-8 -*-
import pytest
from nose.plugins.attrib import attr
from API.base_api import check_response_data
from ..base_wbs_api import WBSAPIBaseTestMixin
import unittest
from fake_data import FakeData
import sys
import os

reload(sys)
sys.setdefaultencoding('utf-8')


@attr('internal')
@attr('external')
@attr('externalopen')
class InvestorRegisterTest(WBSAPIBaseTestMixin, unittest.TestCase):

    expected_response_format = {
        "success": bool,
        "msg": unicode,
    }

    @check_response_data
    def test_response_data(self):
        self.expected_response = {
            "success": True,
            "msg": u"操作成功",
            "errorCode": None,
            "data": None
        }

    @check_response_data
    def test_response_data_with_duplicate_phone(self):
        self.response = self.do_request(self.data)
        self.expected_response = {
            u"msg": u'手机号{0}已注册'.format(self.phone)
        }

    @classmethod
    def setUpClass(cls):
        cls.view_url = 'investor/register.json' if os.getenv('api_type') == 'ex' else 'register.json'
        cls.phone = FakeData().phone_number()
        data_dict = {
            "param": {
                "mobile": cls.phone,
                "authCode": "1234",
                "password": "6846860684f05029abccc09a53cd66f1"
            }
        }
        cls.data = 'data={0}'.format(cls.dict_to_json(data_dict))
        super(InvestorRegisterTest, cls).setUpClass()
        print cls.response.json()




