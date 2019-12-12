# -*- coding: utf-8 -*-
from API.base_api import check_response_data
from API.wbs.base_wbs_api import WBSAPIBaseTestMixin
import unittest
import pytest
from nose.plugins.attrib import attr


@attr('issues')
#@attr('internal')
#@attr('external')
class SearchEmployeeTest(WBSAPIBaseTestMixin, unittest.TestCase):
    view_url = 'employee/search.json'
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

    @check_response_data
    def check_response_with_successful_workflow(self):
        self.expected_response = {
            "success": True,
            "msg": u"操作成功"
        }

    @classmethod
    def setUpClass(cls):
        cls.data = 'data={"token":"5c0b8849-aab1-4159-8ca8-8996a926959a","param":{}}'
        super(SearchEmployeeTest, cls).setUpClass()