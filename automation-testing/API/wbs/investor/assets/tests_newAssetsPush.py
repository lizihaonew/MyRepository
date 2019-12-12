# -*- coding: utf-8 -*-
from API.wbs.base_wbs_api import WBSAPIBaseTestMixin
from API.base_api import check_response_data
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
class InvestorQuantityAssetsTest(WBSAPIBaseTestMixin, unittest.TestCase):
    phone = FakeData().phone_number()

    expected_response_format = {
        "success": bool,
        "msg": unicode,
        "errorCode": types.NoneType,
        "data": int
    }

    @check_response_data
    def test_check_response_with_successful_workflow(self):
        self.expected_response = {
            "success": True,
            "msg": u"操作成功"
        }

    @classmethod
    def setUpClass(cls):
        cls.view_url = 'assets/newAssetsPush.json'
        token = cls.generate_investor_token()
        data_dict = {
            "token": token,
            "param": {}
        }
        cls.data = 'data={0}'.format(cls.dict_to_json(data_dict))
        super(InvestorQuantityAssetsTest, cls).setUpClass()
