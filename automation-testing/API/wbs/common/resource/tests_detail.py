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
class InvestorViewResourceDetailTest(WBSAPIBaseTestMixin, unittest.TestCase):
    phone = FakeData().phone_number()

    expected_response_format = {
        "success": bool,
        "msg": unicode,
        "errorCode": types.NoneType,
        "data": {
            "id": int,
            "entId": int,
            "actTitle": unicode,
            "summary": unicode,
            "pictureUrl": unicode,
            "startTime": int,
            "endTime": int,
            "address": unicode,
            "peopleNum": int,
            "content": unicode,
            "scope": int,
            "scopeStr": unicode,
            "source": unicode,
            "readNum": int,
            "createdBy": int,
            "createTime": int,
            "updatedBy": int,
            "updateTime": int
        }
    }

    @classmethod
    def setUpClass(cls):
        cls.view_url = 'resource/detail.json'
        data_dict = {
            "param": {
                "value": 18
            }
        }
        cls.data = 'data={0}'.format(cls.dict_to_json(data_dict))
        super(InvestorViewResourceDetailTest, cls).setUpClass()
