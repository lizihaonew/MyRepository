# -*- coding: utf-8 -*-
from API.wbs.base_wbs_api import WBSAPIBaseTestMixin
from API.base_api import check_response_data
import unittest
import pytest
from nose.plugins.attrib import attr


@attr('external')
class EmployeeBatchUpdateTest(WBSAPIBaseTestMixin, unittest.TestCase):

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
        #先查询
        cls.view_url = 'employee/search.json'
        cls.data = 'data={"token":' + str(cls.generate_token()) + ',"param":{}}'
        super(EmployeeBatchUpdateTest, cls).setUpClass()
        cls.employee = cls.response['data']['data']['list'][-1]
        cls.employee1 = cls.response['data']['data']['list'][-2]

        cls.view_url = 'employee/batchUpdate.json'
        #FIXME name字段需要优化成中文
        cls.data = 'data={"token":' + str(cls.generate_token()) + ',' \
                   '"param":[' \
                   '{"id":"' + str(cls.employee["id"]) + '",' \
                   '"name":"PL0001",' \
                   '"deptCode":"' + str(cls.employee["deptCode"]) + '",' \
                   '"documentType":"1",' \
                   '"mobile":"' + str(cls.employee['mobile']) + '",' \
                   '"documentNo":"' + str(cls.employee['documentNo']) + '",' \
                   '"positionId":"' + str(cls.employee['positionId']) + '",' \
                   '"joinDate":"' + str(cls.employee['joinDate']) + '",' \
                   '"education":"1"},' \
                   '{"id":"' + str(cls.employee1["id"]) + '",' \
                   '"name":"PL0002",' \
                   '"deptCode":"' + str(cls.employee1["deptCode"]) + '",' \
                   '"documentType":"1",' \
                   '"mobile":"' + str(cls.employee1['mobile']) + '",' \
                   '"documentNo":"' + str(cls.employee1['documentNo']) + '",' \
                   '"positionId":"' + str(cls.employee1['positionId']) + '",' \
                   '"joinDate":"' + str(cls.employee1['joinDate']) + '",' \
                   '"education":"1"}],' \
                   '"sign":"354d13a6f4f2e8ff58a5d93a757c1bae"}'

        super(EmployeeBatchUpdateTest, cls).setUpClass()
