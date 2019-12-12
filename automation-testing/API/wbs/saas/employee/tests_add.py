# -*- coding: utf-8 -*-
from API.base_api import check_response_data
from API.wbs.base_wbs_api import WBSAPIBaseTestMixin
import unittest
import pytest
from nose.plugins.attrib import attr
from fake_data import FakeData


@attr('issues')
#@attr('internal')
#@attr('external')
class SingleAddEmployeeTest(WBSAPIBaseTestMixin, unittest.TestCase):
    view_url = 'employee/add.json'
    fake = FakeData()

    expected_response_format = {
        "success": bool,
        "msg": unicode,
    }

    @check_response_data
    def test_response_with_successful_workflow(self):
        self.expected_response = {
            "success": True,
            "msg": u"操作成功",
            "errorCode": None,
            "data": None
        }

    @check_response_data
    def test_response_with_duplicate_phone(self):
        self.response = self.do_request(self.data)
        self.expected_response = {
            "success": False,
            "msg": u"手机号已存在！",
            "errorCode": None,
            "data": None
        }

    @classmethod
    def setUpClass(cls):
        cls.data = 'data={' \
                   '"token":' + cls.generate_token()+ \
                   ',"param":' \
                   '{"gender": 0,' \
                   '"documentType": 1,' \
                   '"joinDate": "2014-1-1",' \
                   '"education": "1",' \
                   '"married": "0",' \
                   '"employeeNo": "Z001",' \
                   '"deptCode": "NTBNBK0001",' \
                   '"positionId": 1,' \
                   '"roleId": 1,' \
                   '"name": "AutomationTest",' \
                   '"documentNo": "441800197601151022",' \
                   '"admin": "1",' \
                   '"mobile":' + cls.fake.phone_number()+'}}'
        super(SingleAddEmployeeTest, cls).setUpClass()
