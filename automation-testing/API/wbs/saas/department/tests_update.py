# -*- coding: utf-8 -*-
from API.base_api import check_response_data
from API.wbs.base_wbs_api import WBSAPIBaseTestMixin
import unittest
import pytest
from nose.plugins.attrib import attr


#@attr('internal')
@attr('external')
class SectionModifyTest(WBSAPIBaseTestMixin, unittest.TestCase):
    expected_response_format = {
        "success": bool,
        "msg": unicode
    }

    @check_response_data
    def tests_response_data_with_successful_workflow(self):
        self.expected_response = {
            "success": True,
            "msg": u"操作成功"
        }

    @classmethod
    def setUpClass(cls):
        cls.view_url = 'department/list.json'
        data_dict = {
            "token": cls.generate_token(),
            "param": {}
        }
        cls.data = 'data={0}'.format(cls.dict_to_json(data_dict))
        super(SectionModifyTest, cls).setUpClass()
        dept_id = cls.response['data']['data']['list'][0]['id']
        cls.view_url = 'department/update.json'
        data_dict = {
                   "token": cls.generate_token(),
                   "param": {
                        "id": dept_id,
                        "name": "部门更新自动化",
                        "parentCode": '',
                        "departmentTypeCode": '2'
                   }
        }
        cls.data = 'data={0}'.format(cls.dict_to_json(data_dict))
        super(SectionModifyTest, cls).setUpClass()

