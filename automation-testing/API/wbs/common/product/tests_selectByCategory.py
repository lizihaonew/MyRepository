# -*- coding: utf-8 -*-
import pytest
from nose.plugins.attrib import attr
from API.wbs.base_wbs_api import WBSAPIBaseTestMixin
import unittest
from fake_data import FakeData
import sys
import types

reload(sys)
sys.setdefaultencoding('utf-8')


@attr('internal')
@attr('externalopen')
class InvestorViewProductListTest(WBSAPIBaseTestMixin, unittest.TestCase):
    phone = FakeData().phone_number()

    expected_response_format = {
        "success": bool,
        "msg": unicode,
        "errorCode": types.NoneType,
        "data": [
            {
                "id": int,
                "name": unicode,
                "categoryProperty": int,
                # FIXME 返回的是整数，
                "minAmount": float,
                "currencyUnit": unicode,
                "term": unicode,
                "annualReturn": unicode,
                "introduction": unicode,
                "productReview": unicode,
                "netValue": float,
                "smallPic": unicode,
                "bigPic": unicode,
                "productMarketingCopy": unicode,
                "status": int,
                "productCategoryName": unicode,
                "riskLevel": int,
                "riskValue": int,
                "riskName": unicode
            }
        ]
    }

    @classmethod
    def setUpClass(cls):
        cls.view_url = 'product/selectByCategory.json'
        data_dict = {
            "param": {
                "categoryId": 6
            }
        }
        cls.data = 'data={0}'.format(cls.dict_to_json(data_dict))
        super(InvestorViewProductListTest, cls).setUpClass()
