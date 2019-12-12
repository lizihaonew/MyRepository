# -*- coding: utf-8 -*-
from API.base_api import check_response_data
from API.wbs.base_wbs_api import WBSAPIBaseTestMixin
import unittest
import pytest
from nose.plugins.attrib import attr
from fake_data import FakeData


@attr('external')
class BatchAddEmployeeTest(WBSAPIBaseTestMixin, unittest.TestCase):
    view_url = 'employee/batchAdd.json'
    fake = FakeData()
    phone1 = fake.phone_number()
    phone2 = fake.phone_number()

    expected_response_format = {
            "success": bool,
            "msg": unicode,
            "data": [
                {
                    "mobile": unicode,
                    "success": bool,
                },
                {
                    "mobile": unicode,
                    "success": bool,
                }
            ]
        }

    @check_response_data
    def test_response_with_successful_workflow(self):
        self.expected_response = {
            "success": True,
            "msg": u"操作成功",
            "errorCode": None,
            "data": [
                {
                    "mobile": self.phone1,
                    "success": True,
                    "msg": None
                },
                {
                    "mobile": self.phone2,
                    "success": True,
                    "msg": None
                }
            ]
        }

    @check_response_data
    def test_response_with_duplicate_phone(self):
        self.response = self.do_request(self.data)
        self.expected_response = {
            "success": False,
            "msg": u"批量添加员工失败！",
            "errorCode": None,
            "data": [
                {
                    "mobile": self.phone1,
                    "success": False,
                    "msg": u"手机号已存在！"
                },
                {
                    "mobile": self.phone2,
                    "success": False,
                    "msg": u"手机号已存在！"
                }
            ]
        }

    @classmethod
    def setUpClass(cls):
        data_dict = {
            "token": cls.generate_token(),
            "param": [
                {
                    "gender": 0,
                    "documentType": 1,
                    "joinDate": "2014-1-1",
                    "education": "1",
                    "married": "0",
                    "employeeNo": "Z001",
                    "deptCode": "0001",
                    "positionId": 1,
                    "roleId": 1,
                    "name": "AutomationTest",
                    "documentNo": "441800197601151022",
                    "admin": "1",
                    "mobile": cls.phone1
                 },
                {
                    "gender": 1,
                    "documentType": 1,
                    "joinDate": "2016-1-1",
                    "education": "1",
                    "married": "0",
                    "employeeNo": "Z002",
                    "deptCode": "NTBNBK0001",
                    "positionId": 1,
                    "roleId": 1,
                    "name": "AutomationTest",
                    "documentNo": "441800197601151022",
                    "admin": "1",
                    "mobile": cls.phone2
                }
            ]
        }
        cls.data = 'data={0}'.format(cls.dict_to_json(data_dict))
        super(BatchAddEmployeeTest, cls).setUpClass()
