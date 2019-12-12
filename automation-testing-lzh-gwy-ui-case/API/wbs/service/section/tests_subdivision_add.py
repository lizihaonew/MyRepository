# -*- coding: utf-8 -*-
from API.base_api import check_all_response_data
from API.wbs.base_wbs_api import WBSAPIBaseTestMixin
from API.base_api import check_partial_response_data
import unittest

class SubdivisionAddTest(WBSAPIBaseTestMixin, unittest.TestCase):

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
        cls.view_url = '/ex/department/list.json'
        cls.data = 'data={"token":' + str(cls.generate_token()) + ',"param":{}}'
        super(SubdivisionAddTest, cls).setUpClass()
        cls.code = cls.response['data']['data']['list'][-1]['code']

        cls.view_url = '/ex/department/add.json'
        #FIXME name字段需要优化成中文
        cls.data = 'data={"token":' + str(cls.generate_token()) + ',"param":{"name":"123nnn","parentCode":"'+ str(cls.code) +'"}}'
        super(SubdivisionAddTest, cls).setUpClass()