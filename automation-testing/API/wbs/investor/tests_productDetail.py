# -*- coding: utf-8 -*-
import pytest
from nose.plugins.attrib import attr
from ..base_wbs_api import WBSAPIBaseTestMixin
import unittest
from fake_data import FakeData
import sys
import types
import os
from API import config

reload(sys)
sys.setdefaultencoding('utf-8')


@attr('internal')
@attr('externalopen')
class InvestorProductDetailsTest(WBSAPIBaseTestMixin, unittest.TestCase):
    phone = FakeData().phone_number()

    expected_response_format = {
        "success": bool,
        "msg": unicode,
        "errorCode": types.NoneType,
        "data": {
            "id": int,
            "name": unicode,
            "property": int,
            "source": int,
            "categoryProperty": int,
            "categoryId": int,
            "categoryName": unicode,
            "minAmount": float,
            "currencyUnit": unicode,
            "term": unicode,
            "annualReturn": unicode,
            "introduction": unicode,
            "productReview": unicode,
            "productLight": unicode,
            "netValue": unicode,
            "statusStr": unicode,
            "status": int,
            "releaseStatus": int,
            "seq": int,
            "currency": int,
            "currencyStr": unicode,
            "smallPic": unicode,
            "bigPic": unicode,
            "productMarketingCopy": unicode,
            "riskInformation": unicode,
            "accountName": unicode,
            "bankName": unicode,
            "accountNo": unicode,
            "memo": unicode,
            "riskLevel": int,
            "riskValue": int,
            "riskName": unicode,
            "riskLevelName": unicode,
            "outId": int,
            "videos": [
                {
                    "fileUrl":unicode,
                    "fileName":unicode,
                    "snapFile":unicode,
                    "fileType":unicode
                }
            ],
            "pdfs": list,
            "announcements": unicode
        }
    }

    @classmethod
    def setUpClass(cls):
        # 查询产品分类列表
        cls.view_url = 'categoryGroupList.json'
        token = cls.generate_investor_token()
        data_dict = {
            "token": token,
            "param": {}
        }
        cls.data = 'data={0}'.format(cls.dict_to_json(data_dict))
        super(InvestorProductDetailsTest, cls).setUpClass()
        #此处拿到的categoryId，调用selectByCategory接口得到的产品有可能为空，也就会出现数组越界错误，目前咱们没有接口能通过categoryproperty来取产品
        categoryId = cls.response['data']['data'][0][-2]['id']
        # 根据产品分类查询产品列表
        cls.view_url = config.select_by_category[os.getenv('api_type', None)]
        data_dict = {
            "token": token,
            "param": {
                "categoryId": categoryId
            }
        }
        cls.data = 'data={0}'.format(cls.dict_to_json(data_dict))
        cls.response = cls.do_request(cls.data)
        value = cls.response['data']['data'][0]['id']
        # 查询产品详情
        cls.view_url = 'productDetail.json'
        data_dict = {
            "token": token,
            "param": {
                "value": value
            }
        }
        cls.data = 'data={0}'.format(cls.dict_to_json(data_dict))
        super(InvestorProductDetailsTest, cls).setUpClass()
