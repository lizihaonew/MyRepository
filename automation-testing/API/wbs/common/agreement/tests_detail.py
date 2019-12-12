# -*- coding: utf-8 -*-
import pytest
from nose.plugins.attrib import attr
from API.base_api import check_response_data
from API.wbs.base_wbs_api import WBSAPIBaseTestMixin
import unittest
from fake_data import FakeData
import sys
import types
reload(sys)
sys.setdefaultencoding('utf-8')


@attr('internal')
@attr('externalopen')
class InvestorViewRegistrationProtocolsTest(WBSAPIBaseTestMixin, unittest.TestCase):
    phone = FakeData().phone_number()

    expected_response_format = {
        "success": bool,
        "msg": unicode,
        "errorCode": types.NoneType,
        "data": {
            "id": int,
            "createdBy": int,
            "createTime": int,
            "name": unicode,
            "content": unicode,
            "updatedBy": int,
            "updateTime": int,
            "entId": int,
            "type": int
        }
    }

    @check_response_data
    def test_response_data_with_success(self):
        self.expected_response = {
            "msg": u"操作成功"
        }

    @check_response_data
    def test_response_data_with_error_type(self):
        data = 'data={"param":{"value":"5"}}'
        self.response = self.do_request(data)
        self.expected_response = {
            "msg": u"查看合作协议内容失败！"
        }

    @classmethod
    def setUpClass(cls):
        cls.view_url = 'agreement/detail.json'
        param_dict = {
            'param':
                {
                    'value': '2'
                }
        }
        cls.data = 'data={0}'.format(cls.dict_to_json(param_dict))
        super(InvestorViewRegistrationProtocolsTest, cls).setUpClass()

