# -*- coding: utf-8 -*-
from API.base_api import check_all_response_data
from API.wbs.base_wbs_api import WBSAPIBaseTestMixin
from API.base_api import check_partial_response_data
import unittest

class SectionSearchTest(WBSAPIBaseTestMixin, unittest.TestCase):
    view_url = '/ex/department/list.json'
    expected_response_format = {
        "success": bool,
        "msg": unicode,
    }

    @check_partial_response_data
    def test_check_response_with_successful_workflow(self):
        self.expected_response = {
            "success": True,
            "msg": u"操作成功"
        }

    @classmethod
    def setUpClass(cls):
        cls.data = 'data={"token":' + str(cls.generate_token()) + ',"param":{}}'
        super(SectionSearchTest, cls).setUpClass()