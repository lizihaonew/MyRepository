# -*- coding: utf-8 -*-
from API.base_api import check_response_data
from API.wbs.base_wbs_api import WBSAPIBaseTestMixin
import unittest
import pytest
import os
from nose.plugins.attrib import attr
from fake_data import FakeData


#@attr('internal') search.json is only avaiable in ex apis
@attr('external')
class SectionDeleteTest(WBSAPIBaseTestMixin, unittest.TestCase):
    fake = FakeData()
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
        cls.view_url = 'department/add.json'
        dept_name = cls.fake.department_name()
        data_dict = {
            "token": cls.generate_token(),
            "param": {
                "name": dept_name,
                "departmentTypeCode": "1"
            }
        }
        cls.data = 'data={0}'.format(cls.dict_to_json(data_dict))
        super(SectionDeleteTest, cls).setUpClass()
        cls.view_url = 'department/search.json'
        data_dict = {
            "token": cls.generate_token(),
            "param": {
                "name": dept_name
            }
        }
        cls.data = 'data={0}'.format(cls.dict_to_json(data_dict))
        super(SectionDeleteTest, cls).setUpClass()
        dept_id = cls.response['data']['data']['list'][0]['id']
        cls.view_url = 'department/delete.json'
        data_dict = {
            "token": cls.generate_token(),
            "param": {
                "value": dept_id
            }
        }
        cls.data = 'data={0}'.format(cls.dict_to_json(data_dict))
        super(SectionDeleteTest, cls).setUpClass()
