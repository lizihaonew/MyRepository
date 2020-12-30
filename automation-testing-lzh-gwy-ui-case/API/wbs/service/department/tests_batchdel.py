# -*- coding: utf-8 -*-
from API.base_api import check_all_response_data
from API.wbs.base_wbs_api import WBSAPIBaseTestMixin
from API.base_api import check_partial_response_data
import unittest


class DepartmentBatchDelTest(WBSAPIBaseTestMixin, unittest.TestCase):
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
    def test_check_response_with_error_message(self):
        self.response = self.do_request(self.data)
        self.expected_response = {
            "success": False,
            "msg": u"批量删除异常！"
        }

    @classmethod
    def setUpClass(cls):
        # 先查询
        cls.view_url = '/ex/department/search.json'
        cls.data = 'data={"token":' + str(cls.generate_token()) + ',"param":{"entId":1}}'
        super(DepartmentBatchDelTest, cls).setUpClass()
        cls.id1 = cls.response['data']['data']['list'][-1]['id']
        cls.id2 = cls.response['data']['data']['list'][-2]['id']
        cls.id3 = cls.response['data']['data']['list'][-3]['id']

        cls.view_url = '/ex/department/batchDelete.json'
        cls.data = 'data={' \
                   '"token":' + str(cls.generate_token()) + ',' \
                   '"param": [' \
                   '{"value":' + str(cls.id1) + '},' \
                   '{"value":' + str(cls.id2) + '},' \
                   '{"value":' + str(cls.id3) + '}' \
                   ']}'
        super(DepartmentBatchDelTest, cls).setUpClass()