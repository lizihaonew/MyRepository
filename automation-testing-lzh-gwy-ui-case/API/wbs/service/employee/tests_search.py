# -*- coding: utf-8 -*-
from API.base_api import check_partial_response_data
from API.wbs.base_wbs_api import WBSAPIBaseTestMixin
import unittest


class SearchEmployeeTest(WBSAPIBaseTestMixin, unittest.TestCase):
    view_url = '/ex/employee/search.json'
    expected_response_format = {
        "success": bool,
        "msg": unicode,
        "data": {
            "totalCount": int,
            "list": [
                {
                    "id": int,
                    "name": unicode,
                }
            ]
        }
    }

    @check_partial_response_data
    def check_response_with_successful_workflow(self):
        self.expected_response = {
            "success": True,
            "msg": u"操作成功"
        }

    @classmethod
    def setUpClass(cls):
        cls.data = 'data={"token":"5c0b8849-aab1-4159-8ca8-8996a926959a","param":{}}'
        super(SearchEmployeeTest, cls).setUpClass()