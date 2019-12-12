# -*- coding: utf-8 -*-
from API.base_api import check_partial_response_data, check_all_response_data
from API.wbs.base_wbs_api import WBSAPIBaseTestMixin
import unittest
from fake_data import FakeData

class SectionModifyTest(WBSAPIBaseTestMixin, unittest.TestCase):
    view_url = '/ex/position/list.json'
    expected_response_format = {
        "success": bool,
        "msg": unicode
    }

    @check_partial_response_data
    def tests_response_data_with_successful_workflow(self):
        self.expected_response = {
            "success": True,
            "msg": u"操作成功"
        }

    @classmethod
    def setUpClass(cls):
        cls.view_url = '/ex/department/list.json'
        cls.data = 'data={"token":' + cls.generate_token() + ',"param": {}}'
        super(SectionModifyTest, cls).setUpClass()
        id = cls.response['data']['data']['list'][0]['id']
        cls.view_url = '/ex/department/update.json'
        cls.data = 'data={' \
                   '"token":' + cls.generate_token() +',' \
                   '"param":{' \
                   '"entId":1,' \
                   '"id":' + str(id) + ','\
                   '"name":"12321"' \
                   '}}'
        cls.response = cls.do_request(cls.data)
