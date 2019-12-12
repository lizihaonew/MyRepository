# -*- coding: utf-8 -*-
from API.wbs.base_wbs_api import WBSAPIBaseTestMixin
from API.base_api import check_response_data
import unittest
import pytest
from nose.plugins.attrib import attr


@attr('external')
class SectionSearchTest(WBSAPIBaseTestMixin, unittest.TestCase):
    view_url = 'department/list.json'
    expected_response_format = {
        "success": bool,
        "msg": unicode,
    }

    @check_response_data
    def test_check_response_with_successful_workflow(self):
        self.expected_response = {
            "success": True,
            "msg": u"操作成功"
        }

    @classmethod
    def setUpClass(cls):
        cls.data = 'data={"token":' + str(cls.generate_token()) + ',"param":{}}'
        super(SectionSearchTest, cls).setUpClass()