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
class InvestorViewCategoryListTest(WBSAPIBaseTestMixin, unittest.TestCase):
    phone = FakeData().phone_number()

    expected_response_format = {
        "success": bool,
        "msg": unicode,
        "errorCode": types.NoneType,
        # Fixme 以下数据不能判断
        # "data": [
        #             [
        #                 {
        #                     "id": int,
        #                     "name": unicode,
        #                     "property": int,
        #                     "propertyStr": unicode,
        #                     "seq": int
        #                 }
        #             ]
        # ]
    }

    @classmethod
    def setUpClass(cls):
        cls.view_url = 'categoryGroupList.json'
        data_dict = {
            "param": {}
        }
        cls.data = 'data={0}'.format(cls.dict_to_json(data_dict))
        super(InvestorViewCategoryListTest, cls).setUpClass()
