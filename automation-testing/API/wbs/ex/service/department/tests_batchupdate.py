# -*- coding: utf-8 -*-
from API.wbs.base_wbs_api import WBSAPIBaseTestMixin
from API.base_api import check_response_data
import unittest
import pytest
from nose.plugins.attrib import attr
from fake_data import FakeData


@attr('external')
class DepartmentBatchUpdateTest(WBSAPIBaseTestMixin, unittest.TestCase):
    fake = FakeData()
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
        # 先查询
        cls.view_url = 'department/search.json'
        cls.data = 'data={"token":' + str(cls.generate_token()) + ',"param":{"entId":1}}'
        super(DepartmentBatchUpdateTest, cls).setUpClass()
        cls.id1 = cls.response['data']['data']['list'][-1]['id']
        cls.id2 = cls.response['data']['data']['list'][-2]['id']
        cls.id3 = cls.response['data']['data']['list'][-3]['id']

        cls.view_url = 'department/batchUpdate.json'
        cls.data = 'data={' \
                   '"token":' + str(cls.generate_token()) + ',' \
                   '"param":[' \
                   '{"entId":1,"id":' + str(cls.id1) + ',"name":' + cls.fake.department_update_name() + '},' \
                   '{"entId":1,"id":' + str(cls.id1) + ',"name":' + cls.fake.department_update_name() + '},' \
                   '{"entId":1,"id":' + str(cls.id1) + ',"name":' + cls.fake.department_update_name() + '}' \
                   ']}'
        super(DepartmentBatchUpdateTest, cls).setUpClass()