# -*- coding: utf-8 -*-
from API.base_api import check_all_response_data
from API.wbs.base_wbs_api import WBSAPIBaseTestMixin
from API.base_api import check_partial_response_data
import unittest
from fake_data import FakeData


class DepartmentBatchAddTest(WBSAPIBaseTestMixin, unittest.TestCase):
    fake = FakeData()
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
        # 先查询
        cls.view_url = '/ex/department/batchAdd.json'
        cls.data = 'data={"' \
                   'token":' + str(cls.generate_token()) + ',' \
                   '"param":[' \
                   '{"name":' + cls.fake.department_name() + ',"departmentTypeCode": "1", "parentCode":""},' \
                   '{"name":' + cls.fake.department_name() + ',"departmentTypeCode": "1", "parentCode":""},' \
                   '{"name":' + cls.fake.department_name() + ',"departmentTypeCode": "1", "parentCode":""}]}'
        super(DepartmentBatchAddTest, cls).setUpClass()