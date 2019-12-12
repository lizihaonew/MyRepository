# -*- coding: utf-8 -*-
import pytest
from nose.plugins.attrib import attr
from API.base_api import check_response_data
from ..base_wbs_api import WBSAPIBaseTestMixin
import unittest
from fake_data import FakeData
import sys
import types
import json
import requests
import random

reload(sys)
sys.setdefaultencoding('utf-8')


@attr('internal')
@attr('externalopen')
class InvestorGetInfoTest(WBSAPIBaseTestMixin, unittest.TestCase):
    phone = FakeData().phone_number()

    expected_response_format = {
        "success": bool,
        "msg": unicode,
        "errorCode": types.NoneType,
        "data": {
            "id": int,
            "entId": int,
            "faId": int,
            "name": unicode,
            "mobile": unicode,
            "riskValue": int,
            "riskName": unicode,
            "serviceHotLine": unicode,
            "customerId": int,
            "status": int,
            "type": int,
            "documentNo": unicode,
            "identifiedAuth": int,
            "name1": unicode,
            "updateTime": int,
            "token": unicode,
            "createTime": int,
            "pictureUrl": unicode,
            "createdBy": int,
            "updatedBy": int,
            "lastLoginIp": unicode,
            "registerSource": int,
            "doneRiskSurvey": int,
            "auditOpinion": unicode,
            "weixinName": unicode,
            "unionId": int,
            "headimgurl": unicode,
            "hasPass": bool,
            "qualified": int
        }
    }

    @check_response_data
    def test_response_data_with_error_pass(self):
        data_dict = {
            "token": "12313131313",
            "param": {}
        }
        data = 'data={0}'.format(self.dict_to_json(data_dict))
        self.response = self.do_request(data)
        self.expected_response = {
            "msg": u"获取信息失败！"
        }

    @classmethod
    def setUpClass(cls):
        cls.view_url = 'myInfo.json'
        token = cls.generate_investor_token()
        data_dict = {
            "token": token,
            "param": {}
        }
        cls.data = 'data={0}'.format(cls.dict_to_json(data_dict))
        super(InvestorGetInfoTest, cls).setUpClass()
