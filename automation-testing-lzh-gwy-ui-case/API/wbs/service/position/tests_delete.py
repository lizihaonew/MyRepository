# -*- coding: utf-8 -*-
from API.base_api import check_all_response_data, check_partial_response_data
from API.wbs.base_wbs_api import WBSAPIBaseTestMixin
import unittest
from fake_data import FakeData


class DeletePositionTest(WBSAPIBaseTestMixin, unittest.TestCase):
    view_url = '/ex/position/list.json'
    fake = FakeData()
    expected_response_format = {
        "success": bool,
        "msg": unicode,
    }

    @check_partial_response_data
    def tests_response_data_with_successful_workflow(self):
        self.expected_response = {
            "success": True,
            "msg": u"操作成功",
        }

    @check_partial_response_data
    def tests_response_data_with_deleting_position_with_employees(self):
        self.data = 'data={"token":' + self.generate_token() + ',"param":{"value":' + str(self.position_with_employee_id) + '}}'
        self.response = self.do_request(self.data)
        self.expected_response = {
            "success": False,
            "msg": u"该职位下有员工不能删除!"
        }

    @classmethod
    def setUpClass(cls):
        cls.data = 'data={"token":' + cls.generate_token() + ',"param": {}}'
        super(DeletePositionTest, cls).setUpClass()
        id = cls.response['data']['data']['list'][-1]['id']
        cls.position_with_employee_id = cls.response['data']['data']['list'][0]['id']
        cls.view_url = '/ex/position/delete.json'
        cls.data = 'data={"token":' + cls.generate_token() + ',"param":{"value":' + str(id) + '}}'
        cls.response = cls.do_request(cls.data)