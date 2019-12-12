# -*- coding: utf-8 -*-
from API.base_api import check_partial_response_data, check_all_response_data
from API.wbs.base_wbs_api import WBSAPIBaseTestMixin
import unittest
from fake_data import FakeData


class SingleAddPositionTest(WBSAPIBaseTestMixin, unittest.TestCase):
    view_url = '/ex/position/add.json'
    fake = FakeData()
    expected_response_format = {
        "success": bool,
        "msg": unicode,
        "data": int
    }

    @check_partial_response_data
    def tests_response_with_successful_workflow(self):
        self.expected_response = {
            "success": True,
            "msg": u"操作成功",
            "errorCode": None,
        }

    @check_all_response_data
    def tests_response_with_duplicate_position_name(self):
        self.response = self.do_request(self.data)
        self.expected_response = {
            "success": False,
            "msg": u"职位名称已存在！",
            "errorCode": None,
            "data": None
        }

    @check_all_response_data
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
