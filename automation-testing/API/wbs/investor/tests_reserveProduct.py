# -*- coding: utf-8 -*-
import pytest
from nose.plugins.attrib import attr
from ..base_wbs_api import WBSAPIBaseTestMixin
from API.base_api import check_response_data
import unittest
from fake_data import FakeData
import sys
import time
import random
from API import config
import os
reload(sys)
sys.setdefaultencoding('utf-8')


@attr('internal')
@attr('externalopen')
class InvestorProductDetailsTest(WBSAPIBaseTestMixin, unittest.TestCase):

    expected_response_format = {
        "success": bool,
        "msg": unicode,
        # "errorCode": types.NoneType,
    }

    @check_response_data
    def test_check_response_with_successful_workflow(self):
        self.expected_response = {
            "success": True,
            "msg": u"操作成功"
        }

    @classmethod
    def setUpClass(cls):
        # 查询产品分类列表
        cls.view_url = 'categoryGroupList.json'
        token = cls.generate_investor_token()
        data_dict = {
            "token": token,
            "pageSize": 8,
            "param": {}
        }
        cls.data = 'data={0}'.format(cls.dict_to_json(data_dict))
        super(InvestorProductDetailsTest, cls).setUpClass()
        #强制选择保险产品来预约
        category_groups = cls.response['data']['data']
        x_index = 0
        y_index = 0
        for category_group in category_groups:
            print len(category_group)
            for i in range(0, len(category_group)-1):
                if category_group[i]['property'] == 9:
                    return
                else:
                    y_index += 1
            x_index += 1
        # 此处拿到的categoryId，调用selectByCategory接口得到的产品有可能为空，也就会出现数组越界错误，目前咱们没有接口能通过categoryproperty来取产品
        categoryId = category_groups[x_index][y_index]['id']
        cls.view_url = config.select_by_category[os.getenv('api_type', None)]
        token = cls.generate_investor_token()
        data_dict = {
            "token": token,
            "param": {
                "categoryId": categoryId
            }
        }
        cls.data = 'data={0}'.format(cls.dict_to_json(data_dict))
        cls.response = cls.do_request(cls.data)
        data = cls.response['data']['data']
        index = random.randint(0, len(data)-1)
        product_id = data[index]['id']
        # 预约产品
        cls.view_url = 'reserveProduct.json'
        data_dict = {
            "token": token,
            "param":
                {
                    "productId": product_id,
                    "reservationAmount": '100{0}'.format(FakeData().product_category()),
                    "reservationDate": time.strftime('%Y-%m-%d', time.localtime()),
                    "memo": '接口自动化{0}'.format(FakeData().bank_name())
                }
        }
        cls.data = 'data={0}'.format(cls.dict_to_json(data_dict))
        super(InvestorProductDetailsTest, cls).setUpClass()



