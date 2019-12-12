# -*- coding: utf-8 -*-
from API.base_api import check_all_response_data
from API.wbs.base_wbs_api import WBSAPIBaseTestMixin
from API.base_api import check_partial_response_data
import unittest

class EmployeeUpdateTest(WBSAPIBaseTestMixin, unittest.TestCase):

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

#字符串拼接的中文不用+ u
#字符串拼接中文不用强制转换str
#'"name":"' + cls.employee['name'] + '",' \
    @classmethod
    def setUpClass(cls):
        #先查询
        cls.view_url = '/ex/employee/search.json'
        cls.data = 'data={"token":' + str(cls.generate_token()) + ',"param":{}}'
        super(EmployeeUpdateTest, cls).setUpClass()
        cls.employee = cls.response['data']['data']['list'][-1]
        print cls.employee['name']

        cls.view_url = '/ex/employee/update.json'
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
        print cls.data
        super(EmployeeUpdateTest, cls).setUpClass()


class EmployeeBatchUpdateTest(WBSAPIBaseTestMixin, unittest.TestCase):

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
        #先查询
        cls.view_url = '/ex/employee/search.json'
        cls.data = 'data={"token":' + str(cls.generate_token()) + ',"param":{}}'
        super(EmployeeBatchUpdateTest, cls).setUpClass()
        cls.employee = cls.response['data']['data']['list'][-1]
        cls.employee1 = cls.response['data']['data']['list'][-2]

        cls.view_url = '/ex/employee/batchUpdate.json'
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
