# -*- coding: utf-8 -*-
from API.base_api import check_all_response_data
from API.wbs.base_wbs_api import WBSAPIBaseTestMixin
from API.base_api import check_partial_response_data
import unittest


class EmployeeQuitTest(WBSAPIBaseTestMixin, unittest.TestCase):
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

    @check_partial_response_data
    def test_check_response_with_false_message(self):
        self.response = self.do_request(self.data)
        self.expected_response = {
            "success": False,
            "msg": u"员工已离职！"
        }

    @classmethod
    def setUpClass(cls):
        # 先查询
        cls.view_url = '/ex/employee/search.json'
        cls.data = 'data={' \
                   '"token":' + str(cls.generate_token()) + ',' \
                   '"param":{' \
                   '"deptCode":"NTBNBK0001"' \
                   '}}'
        super(EmployeeQuitTest, cls).setUpClass()
        cls.id = cls.response['data']['data']['list'][-1]['id']
        # 离职
        cls.view_url = '/ex/employee/dismission.json'
        cls.data = 'data={' \
                   '"token":' + str(cls.generate_token()) + ',' \
                   '"param":{' \
                   '"id":"' + str(cls.id) + '",' \
                   '"dismissionReason": "接口离职",' \
                   '"dismissionDate":"2017-08-30"' \
                   '},"sign":"354d13a6f4f2e8ff58a5d93a757c1bae"}'
        super(EmployeeQuitTest, cls).setUpClass()


class EmployeeBatchQuitTest(WBSAPIBaseTestMixin, unittest.TestCase):
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

    @check_partial_response_data
    def test_check_response_with_false_message(self):
        self.response = self.do_request(self.data)
        self.expected_response = {
            "success": False,
            "msg": u"批量员工离职失败！"
        }

    @classmethod
    def setUpClass(cls):
        # 先查询
        cls.view_url = '/ex/employee/search.json'
        cls.data = 'data={' \
                   '"token":' + str(cls.generate_token()) + ',' \
                   '"param":{' \
                   '"deptCode":"NTBNBK0001"' \
                   '}}'
        super(EmployeeBatchQuitTest, cls).setUpClass()
        cls.id1 = cls.response['data']['data']['list'][-1]['id']
        cls.id2 = cls.response['data']['data']['list'][-2]['id']

        cls.view_url = '/ex/employee/batchDismission.json'
        cls.data = 'data={' \
                   '"token":' + str(cls.generate_token()) + ',' \
                   '"param":[' \
                   '{"id":"' + str(cls.id1) + '","dismissionReason":"接口离职","dismissionDate":"2017-08-31"},' \
                   '{"id":"' + str(cls.id2) + '","dismissionReason":"接口离职","dismissionDate":"2017-08-31"}' \
                   ']}'
        super(EmployeeBatchQuitTest, cls).setUpClass()