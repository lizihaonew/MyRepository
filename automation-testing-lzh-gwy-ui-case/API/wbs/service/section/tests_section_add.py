# -*- coding: utf-8 -*-
from API.base_api import check_partial_response_data, check_all_response_data
from API.wbs.base_wbs_api import WBSAPIBaseTestMixin
import unittest
from fake_data import FakeData


class SectionAddTest(WBSAPIBaseTestMixin, unittest.TestCase):
    view_url = '/ex/department/add.json'
    fake = FakeData()
    expected_response_format = {
        "success": bool,
        "msg": unicode
    }

    @check_partial_response_data
    def tests_response_with_successful_workflow(self):
        self.expected_response = {
            "success": True,
            "msg": u"操作成功"
        }

    @classmethod
    def setUpClass(cls):
        cls.data = 'data={"token":' + cls.generate_token() + ',"param":{"name":' + cls.fake.position_name() + ',"propertyCode":"1"}}'
        super(SectionAddTest, cls).setUpClass() 