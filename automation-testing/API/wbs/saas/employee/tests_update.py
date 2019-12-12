# -*- coding: utf-8 -*-
from API.wbs.base_wbs_api import WBSAPIBaseTestMixin
from API.base_api import check_response_data
import unittest
import pytest
from nose.plugins.attrib import attr


@attr('issues')
#@attr('internal')
#@attr('external')
class EmployeeUpdateTest(WBSAPIBaseTestMixin, unittest.TestCase):

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

#字符串拼接的中文不用+ u
#字符串拼接中文不用强制转换str
#'"name":"' + cls.employee['name'] + '",' \
    @classmethod
    def setUpClass(cls):
        #先查询
        cls.view_url = 'employee/search.json'
        cls.data = 'data={"token":' + str(cls.generate_token()) + ',"param":{}}'
        super(EmployeeUpdateTest, cls).setUpClass()
        cls.employee = cls.response['data']['data']['list'][-1]

        cls.view_url = 'employee/update.json'
        #FIXME name字段需要优化成中文
        cls.data = 'data={"token":' + str(cls.generate_token()) + ',' \
                   '"param":{"gender":"0",' \
                   '"documentType":"1",' \
                   '"joinDate":"' + str(cls.employee['joinDate']) + '",' \
                   '"education":"1",' \
                   '"married":"0",' \
                   '"employeeNo":"' + str(cls.employee['employeeNo']) + '",' \
                   '"positionId":"' + str(cls.employee['positionId']) + '",' \
                   '"roleId":"1",' \
                   '"name":"TTXT",' \
                   '"documentNo":"' + str(cls.employee['documentNo']) + '",' \
                   '"admin":"1",' \
                   '"mobile":"' + str(cls.employee['mobile']) + '",' \
                   '"deptCode":"' + str(cls.employee["deptCode"]) + '",' \
                   '"id":"' + str(cls.employee["id"]) + '"}}'
        super(EmployeeUpdateTest, cls).setUpClass()
