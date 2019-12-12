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
class InvestorCommendAllocationPlanTest(WBSAPIBaseTestMixin, unittest.TestCase):
    phone = FakeData().phone_number()

    expected_response_format = {
        "success": bool,
        "msg": unicode,
        "errorCode": types.NoneType,
        "data": {
            "assetsTemplateId": int,
            "faId": unicode,
            "faName": unicode,
            "investorId": unicode,
            "assetsTemplateName": unicode,
            "introduction": unicode,
            "riskValue": int,
            "riskName": unicode,
            "amount": unicode,
            "owner": int,
            "cateList": [
                {
                    "assetsCategoryTemplateId": int,
                    "assetsTemplateId": int,
                    "categoryId": int,
                    "categoryName": unicode,
                    "ratio": unicode,
                    "prdList": [
                        {
                            "assetsCategoryPrdId": int,
                            "assetsCategoryTemplateId": int,
                            "productId": int,
                            "productName": unicode,
                            "property": int,
                            "amount": unicode,
                            "currency": int,
                            "currencyStr": unicode,
                            "amountType": unicode,
                            "releaseStatus": int,
                            "prdRiskValue": int,
                            "prdRiskName": unicode,
                            "minAmount": float
                        }
                    ]
                }
            ],
            "outId": unicode
        }
    }

    @classmethod
    def setUpClass(cls):
        cls.view_url = 'assets/commend.json'
        token = cls.generate_investor_token()
        data_dict = {
            "token": token,
            "param": {}
        }
        cls.data = 'data={0}'.format(cls.dict_to_json(data_dict))
        super(InvestorCommendAllocationPlanTest, cls).setUpClass()
