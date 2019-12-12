# -*- coding: utf-8 -*-
from API.base_api import check_response_data
from API.wbs.base_wbs_api import WBSAPIBaseTestMixin
import unittest
import pytest
from nose.plugins.attrib import attr
from fake_data import FakeData


@attr('issues')
#@attr('internal')
#@attr('external')
class PositionModifyTest(WBSAPIBaseTestMixin, unittest.TestCase):
    view_url = 'position/list.json'
    fake = FakeData()
    expected_response_format = {
        "success": bool,
        "msg": unicode,
        "data": int
    }

    @check_response_data
    def tests_response_data_with_successful_workflow(self):
        self.expected_response = {
            "success": True,
            "msg": u"操作成功",
        }

    @check_response_data
    def tests_response_data_with_property_code_missed(self):
        self.data = 'data={"token":' + self.generate_token() + ',"param":{"id": "3", "name":' + self.fake.position_name() + '}}'
        self.response = self.do_request(self.data)
        self.expected_response = {
            "success": False,
            "msg": u"职位属性不能为空!",
            "errorCode": None,
            "data": None
        }

    @classmethod
    def setUpClass(cls):
        cls.data = 'data={"token":' + cls.generate_token() + ',"param": {}}'
        super(PositionModifyTest, cls).setUpClass()
        id = cls.response['data']['data']['list'][0]['id']
        property_code = cls.response['data']['data']['list'][0]['propertyCode']
        cls.view_url = 'position/update.json'
        cls.data = 'data={"token":' + cls.generate_token() + ',"param":{"id":' + str(id) + ',"propertyCode":' + str(property_code) + ',"name":' + cls.fake.position_name() + '}}'
        super(PositionModifyTest, cls).setUpClass()