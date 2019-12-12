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
class InvestorViewContentDetailTest(WBSAPIBaseTestMixin, unittest.TestCase):
    phone = FakeData().phone_number()

    expected_response_format = {
        "success": bool,
        "msg": unicode,
        "errorCode": types.NoneType,
        "data": {
            "id": int,
            "entId": int,
            "title": unicode,
            "status": int,
            "author": unicode,
            "source": unicode,
            "summary": unicode,
            "content": unicode,
            "scope": int,
            "scopeStr": unicode,
            "pictureUrl": unicode,
            "pdfs": unicode,
            "videos": [
                {
                    "fileUrl": unicode,
                    "fileName": unicode,
                    "snapFile": unicode,
                    "fileType": unicode
                }
            ],
            "deleted": int,
            "createdBy": int,
            "createTime": int,
            "updatedBy": int,
            "updateTime": int
        }
    }

    @classmethod
    def setUpClass(cls):
        # 查询list里的id
        cls.view_url = 'content/list.json'
        data_dict = {
            "param": {}
        }
        cls.data = 'data={0}'.format(cls.dict_to_json(data_dict))
        super(InvestorViewContentDetailTest, cls).setUpClass()
        id = cls.response['data']['data'][0]['id']
        cls.view_url = 'content/detail.json'
        data_dict = {
            "param": {
                "value": id
            }
        }
        cls.data = 'data={0}'.format(cls.dict_to_json(data_dict))
        super(InvestorViewContentDetailTest, cls).setUpClass()
