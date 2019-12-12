# -*- coding: utf-8 -*-
from API.wbs.base_wbs_api import WBSAPIBaseTestMixin
import unittest
import pytest
from nose.plugins.attrib import attr
from fake_data import FakeData
import sys
import types

reload(sys)
sys.setdefaultencoding('utf-8')


@attr('internal')
@attr('externalopen')
class InvestorConfigurationListTest(WBSAPIBaseTestMixin, unittest.TestCase):
    phone = FakeData().phone_number()

    expected_response_format = {
        "success": bool,
        "msg": unicode,
        "errorCode": types.NoneType,
        "data": [
            {
                "faId": unicode,
                "faName": unicode,
                "customerMessage": unicode,
                "assetsTemplateName": unicode,
                "assetsTemplateId": unicode,
                "createTime": int
            }
        ]
    }

    @classmethod
    def setUpClass(cls):
        cls.view_url = 'assets/acceptList.json'
        token = cls.generate_investor_token()
        data_dict = {
            "token": token,
            "param": {}
        }
        cls.data = 'data={0}'.format(cls.dict_to_json(data_dict))
        super(InvestorConfigurationListTest, cls).setUpClass()
