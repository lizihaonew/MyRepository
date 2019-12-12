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
class InvestorChangePhoneTest(WBSAPIBaseTestMixin, unittest.TestCase):
    phone = FakeData().phone_number()
    change_phone = FakeData().phone_number()
    expected_response_format = {
        "success": bool,
        "msg": unicode,
        "errorCode": types.NoneType
    }

    @check_response_data
    def test_response_data_with_error_pass(self):
        token = self.generate_investor_token()
        data_dict = {
            "token": token,
            "param": {
                "mobile": self.change_phone,
                "authCode": "1231"
            }
        }
        data = 'data={0}'.format(self.dict_to_json(data_dict))
        self.response = self.do_request(data)
        self.expected_response = {
            "msg": u"新手机号已注册！"
        }

    @classmethod
    def setUpClass(cls):
        # 注册
        cls.view_url = 'register.json'
        data_dict = {
            "param": {
                "mobile": cls.phone,
                "authCode": "1234",
                "password": "6846860684f05029abccc09a53cd66f1"
            }
        }
        cls.data = 'data={0}'.format(cls.dict_to_json(data_dict))
        super(InvestorChangePhoneTest, cls).setUpClass()
        # 登录获取token
        cls.view_url = 'login.json'
        data_dict = {
            "param":
                {"mobile": cls.phone,
                 "password": "6846860684f05029abccc09a53cd66f1"
                 }
        }
        cls.data = 'data={0}'.format(cls.dict_to_json(data_dict))
        super(InvestorChangePhoneTest, cls).setUpClass()
        token = cls.response['data']['data']['token']
        # 发送旧手机验证码
        cls.view_url = 'sendCheckCode.json'
        data_dict = {
            "param": {
                "mobile": cls.phone,
                "type": "102"
            }
        }
        cls.data = 'data={0}'.format(cls.dict_to_json(data_dict))
        super(InvestorChangePhoneTest, cls).setUpClass()
        # 验证旧手机验证码
        cls.view_url = 'checkAuthCode.json'
        data_dict = {
            "param": {
                "mobile": cls.phone,
                "type": "102",
                "authCode": "1827"
            }
        }
        cls.data = 'data={0}'.format(cls.dict_to_json(data_dict))
        super(InvestorChangePhoneTest, cls).setUpClass()
        # 修改手机号
        cls.view_url = 'changeMobile.json'
        data_dict = {
            "token": token,
            "param": {
                "mobile": cls.change_phone,
                "authCode": "1231"
            }
        }
        cls.data = 'data={0}'.format(cls.dict_to_json(data_dict))
        super(InvestorChangePhoneTest, cls).setUpClass()
