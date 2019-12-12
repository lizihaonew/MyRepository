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
class SingleAddPositionTest(WBSAPIBaseTestMixin, unittest.TestCase):
    view_url = 'position/add.json'
    fake = FakeData()
    expected_response_format = {
        "success": bool,
        "msg": unicode,
        "data": int
    }

    @check_response_data
    def tests_response_with_successful_workflow(self):
        self.expected_response = {
            "success": True,
            "msg": u"操作成功",
            "errorCode": None,
        }

    @check_response_data
    def tests_response_with_duplicate_position_name(self):
        self.response = self.do_request(self.data)
        self.expected_response = {
            "success": False,
            "msg": u"职位名称已存在！",
            "errorCode": None,
            "data": None
        }

    @check_response_data
    def tests_response_with_property_code_missed(self):
        self.data = 'data={"token":' + self.generate_token() + ',"param":{"name":' + self.fake.position_name() + '}}'
        self.response = self.do_request(self.data)
        self.expected_response = {
            "success": False,
            "msg": u"职位属性不能为空!",
            "errorCode": None,
            "data": None
        }

    @classmethod
    def setUpClass(cls):
        cls.data = 'data={"token":' + cls.generate_token() + ',"param":{"name":' + cls.fake.position_name() + ',"propertyCode":"1"}}'
        super(SingleAddPositionTest, cls).setUpClass()
