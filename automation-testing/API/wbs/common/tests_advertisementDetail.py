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
class InvestorViewAdvertisementTest(WBSAPIBaseTestMixin, unittest.TestCase):
    phone = FakeData().phone_number()

    expected_response_format = {
        "success": bool,
        "msg": unicode,
        "errorCode": types.NoneType,
        "data": {
            "id": int,
            "entId": int,
            "linkurls": [
                unicode
            ],
            "pictureUrls": [
                unicode
            ],
            "seqs": [
                unicode
            ],
            "platform": int,
            "platformStr": unicode,
            "position": int,
            "positionStr": unicode,
            "createdBy": int,
            "createTime": int,
            "updatedBy": int,
            "updateTime": int
        }
    }

    @classmethod
    def setUpClass(cls):
        cls.view_url = 'advertisementDetail.json'
        data_dict = {
            "param":
                {
                    "platform": 2,
                    "position": 1
                }
        }
        cls.data = 'data={0}'.format(cls.dict_to_json(data_dict))
        super(InvestorViewAdvertisementTest, cls).setUpClass()
