# -*- coding: utf-8 -*-
from API.base_api import check_response_data
from API.wbs.base_wbs_api import WBSAPIBaseTestMixin
import unittest
import pytest
import os
from nose.plugins.attrib import attr
from fake_data import FakeData


@attr('internal')
@attr('external')
class DepartmentAddTest(WBSAPIBaseTestMixin, unittest.TestCase):
    view_url = 'department/add.json' if os.getenv('api_type') == 'ex' else 'add.json'
    fake = FakeData()
    expected_response_format = {
        "success": bool,
        "msg": unicode
    }

    @check_response_data
    def tests_response_with_successful_workflow(self):
        self.expected_response = {
            "success": True,
            "msg": u"操作成功"
        }

    @classmethod
    def setUpClass(cls):
        data_dict = {
            "token": cls.generate_token(),
            "param": {
                "name": cls.fake.department_name(),
                "departmentTypeCode": "1"
            }
        }
        cls.data = 'data={0}'.format(cls.dict_to_json(data_dict))
        super(DepartmentAddTest, cls).setUpClass()
