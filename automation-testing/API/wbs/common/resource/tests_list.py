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


# @attr('deleted')
class InvestorViewResourceListTest(WBSAPIBaseTestMixin, unittest.TestCase):
    phone = FakeData().phone_number()

    expected_response_format = {
        "success": bool,
        "msg": unicode,
        "errorCode": types.NoneType,
        "data": [
            {
                "id": int,
                "actTitle": unicode,
                "pictureUrl": unicode,
                "startTime": int,
                "summary": unicode,
                "isHistory": int
            }
        ]
    }

    @classmethod
    def setUpClass(cls):
        cls.view_url = 'resource/list.json'
        data_dict = {
            "param": {}
        }
        cls.data = 'data={0}'.format(cls.dict_to_json(data_dict))
        super(InvestorViewResourceListTest, cls).setUpClass()
