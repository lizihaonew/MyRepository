# -*- coding: utf-8 -*-
from API.base_api import check_all_response_data
from ..base_wbs_api import WBSAPIBaseTestMixin
import unittest
from fake_data import FakeData
'''import sys

reload(sys)
sys.setdefaultencoding('utf-8')'''


class SingleIdAuthTest(WBSAPIBaseTestMixin, unittest.TestCase):
    view_url = '/ex/investor/register.json'
    fake = FakeData()
    registered_phone = fake.phone_number()

    data = 'data={"param":{"mobile":' + registered_phone + ',"authCode":"1234","password":"6846860684f05029abccc09a53cd66f1"}}'

    expected_response_format = {
        "success": bool,
        "msg": unicode
    }

    @check_all_response_data
    def test_response_data_with_successful_workflow(self):
        self.expected_response = {
            "success": True,
            "msg": u"操作成功",
            "errorCode": None,
        }

    @check_all_response_data
    def test_response_data_with_duplicate_pii(self):
        #This can be successful cause it seemed that self.response can't change cls.respone at all
        self.response = self.do_request(self.data)
        self.expected_response = {
            "success": False,
            "msg": u"该身份证号已经被申请！",
            "errorCode": None
        }

    @classmethod
    def setUpClass(cls):
        super(SingleIdAuthTest, cls).setUpClass()
        cls.view_url = '/ex/investor/idAuth.json'
        token = cls.generate_token()
        #FIXME when name is assigned chinese character, always encounter 'token is empty' which is that token is not quoted
        cls.data = 'data={"token":' + str(token) + ',"param":{"mobile":' + cls.registered_phone + ',"documentNo":' + cls.fake.pii() + ',"name": "test"}}'
        #cls.data = 'data={"token":' + str(token) + ',"param":{"mobile":' + cls.registered_phone + ',"documentNo":' + cls.fake.pii() + ',"name": "测试"}}'
        cls.response = cls.do_request(cls.data)


class BatchIdAuthTest(WBSAPIBaseTestMixin, unittest.TestCase):
    view_url = '/ex/investor/batchRegister.json'
    fake = FakeData()
    registered_phone1 = fake.phone_number()
    registered_phone2 = fake.phone_number()
    data = 'data={"param":[{"mobile":' + registered_phone1 + ',"password":"6846860684f05029abccc09a53cd66f2"},{"mobile":' + registered_phone2 + ',"password":"6846860684f05029abccc09a53cd66f1"}]}'
    expected_response_format = {
        "success": bool,
        "msg": unicode,
        "data": [
            {
                "name": unicode,
                "success": bool,
            }
        ]
    }

    @check_all_response_data
    def test_response_data_with_successful_workflow(self):
        self.expected_response = {
            "success": True,
            "msg": u"操作成功",
            "errorCode": None,
            "data": [
                {
                    "name": "test1",
                    "success": True,
                    "msg": None
                },
                {
                    "name": "test2",
                    "success": True,
                    "msg": None
                }
            ]
    }

    @check_all_response_data
    def test_response_data_with_duplicate_pii(self):
        # We must set this, or we will encounter the error like 'Diff is 1014 characters long. Set self.maxDiff to None to see it.'
        self.maxDiff = None
        self.response = self.do_request(self.data)
        self.expected_response = {
            "success": False,
            "msg": u"校验投资人异常！",
            "errorCode": None,
            "data": [
                {
                    "name": "test1",
                    "success": False,
                    "msg": u"该身份证号已经被申请！"
                },
                {
                    "name": "test2",
                    "success": False,
                    "msg": u"该身份证号已经被申请！"
                }
            ]
    }

    @classmethod
    def setUpClass(cls):
        super(BatchIdAuthTest, cls).setUpClass()
        cls.view_url = '/ex/investor/batchIdAuth.json'
        token = cls.generate_token()
        cls.data = 'data={"token":' + str(token) + ',"param":[{"mobile":' + cls.registered_phone1 + ',"documentNo":' + cls.fake.pii() + ',"name": "test1"}, {"mobile":' + cls.registered_phone2 + ',"documentNo":' + cls.fake.pii() + ',"name": "test2"}]}'
        cls.response = cls.do_request(cls.data)
