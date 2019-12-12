# -*- coding: utf-8 -*-
import pytest
from nose.plugins.attrib import attr
from API.base_api import check_response_data
from ..base_wbs_api import WBSAPIBaseTestMixin
import unittest
from fake_data import FakeData
import sys
import os
import types

reload(sys)
sys.setdefaultencoding('utf-8')


@attr('internal')
@attr('external')
@attr('externalopen')
class InvestorIdAuthTest(WBSAPIBaseTestMixin, unittest.TestCase):
    view_url = 'investor/register.json' if os.getenv('api_type') == 'ex' else 'register.json'
    fake = FakeData()
    registered_phone = fake.phone_number()

    expected_response_format = {
        "success": bool,
        "msg": unicode,
        "errorCode": types.NoneType,
        "data": {
            "success": int,
            "returnMsg": unicode,
            "mobile": types.NoneType,
            "name": types.NoneType,
            "documentNoType": types.NoneType,
            "documentNo": types.NoneType,
            "errcode": types.NoneType,
            "complaintStatus": int
        }
    }

    @check_response_data
    def test_response_data_with_successful_workflow(self):
        self.expected_response = {
            "success": True,
            "msg": u"操作成功",
            "errorCode": None,

        }

    @classmethod
    def setUpClass(cls):
        data_dict = {
            "param":
                {
                    "mobile": cls.registered_phone,
                    "authCode": "1234",
                    "password": "6846860684f05029abccc09a53cd66f1"
                 }
        }
        cls.data = 'data={0}'.format(cls.dict_to_json(data_dict))
        super(InvestorIdAuthTest, cls).setUpClass()
        if os.getenv('api_type') == 'ex':
            token = cls.generate_token()
        else:
            cls.view_url = 'login.json'
            data_dict = {
                "param":
                    {
                        "mobile": cls.registered_phone,
                        "password": "6846860684f05029abccc09a53cd66f1"
                     }
            }
            cls.data = 'data={0}'.format(cls.dict_to_json(data_dict))
            super(InvestorIdAuthTest, cls).setUpClass()
            token = cls.response['data']['data']['token']
        cls.view_url = 'investor/idAuth.json' if os.getenv('api_type') == 'ex' else 'idAuth.json'
        data_dict = {
            "token": token,
            "param": {
                "name": cls.fake.user_name(),
                "documentNo": cls.fake.pii()
            }
        }
        cls.data = 'data={0}'.format(cls.dict_to_json(data_dict))
        super(InvestorIdAuthTest, cls).setUpClass()
