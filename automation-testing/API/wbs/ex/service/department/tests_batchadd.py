# -*- coding: utf-8 -*-
from API.wbs.base_wbs_api import WBSAPIBaseTestMixin
from API.base_api import check_response_data
import unittest
import pytest
from nose.plugins.attrib import attr
from fake_data import FakeData


@attr('external')
class DepartmentBatchAddTest(WBSAPIBaseTestMixin, unittest.TestCase):
    fake = FakeData()
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

    @classmethod
    def setUpClass(cls):
        # 先查询
        cls.view_url = 'department/batchAdd.json'
        data_dict = {
            "token": str(cls.generate_token()),
            "param":
                [
                    {
                        "name": cls.fake.department_name(),
                        "departmentTypeCode": "1",
                        "parentCode": ""
                    },
                    {
                        "name": cls.fake.department_name(),
                        "departmentTypeCode": "1",
                        "parentCode": ""
                    },
                    {
                        "name": cls.fake.department_name(),
                        "departmentTypeCode": "1",
                        "parentCode": ""
                    }
                ]
        }
        cls.data = 'data={0}'.format(cls.dict_to_json(data_dict))
        super(DepartmentBatchAddTest, cls).setUpClass()