# -*- coding: utf-8 -*-
import pytest
from nose.plugins.attrib import attr
from ..base_wbs_api import WBSAPIBaseTestMixin
import unittest
import requests
from fake_data import FakeData
import os
import sys
import types

reload(sys)
sys.setdefaultencoding('utf-8')


@attr('internal')
@attr('externalopen')
class InvestorDeleteAttachmentTest(WBSAPIBaseTestMixin, unittest.TestCase):
    phone = FakeData().phone_number()

    expected_response_format = {
        "success": bool,
        "msg": unicode,
        "errorCode": types.NoneType,
    }

    @classmethod
    def setUpClass(cls):
        # 添加
        cls.view_url = 'addAttachment.json'
        token = cls.generate_investor_token()
        cls.files = {
            'files': ("timg.jpeg", open('{0}/file/timg.jpeg'.format(os.path.dirname(__file__)), 'rb'), "image/jpeg"),
            'token': (None, str(token))
        }

        requests.post(cls._get_url('/ex/open/investor/addAttachment.json'), cls.data, files=cls.files)
        #super(InvestorDeleteAttachmentTest, cls).setUpClass()

        # 查询
        cls.view_url = 'getCustomerAttachment.json'
        token = cls.generate_investor_token()
        data_dict = {
            "token": token,
            "param": {}
        }
        cls.data = 'data={0}'.format(cls.dict_to_json(data_dict))
        super(InvestorDeleteAttachmentTest, cls).setUpClass()
        value = cls.response['data']['data'][0]['id']
        # 删除
        cls.view_url = 'deleteAttachment.json'
        data_dict = {
            "token": token,
            "param": {
                "value": value
            }
        }
        cls.data = 'data={0}'.format(cls.dict_to_json(data_dict))
        super(InvestorDeleteAttachmentTest, cls).setUpClass()
