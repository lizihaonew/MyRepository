# -*- coding: utf-8 -*-
import pytest
from nose.plugins.attrib import attr
from ..base_wbs_api import WBSAPIBaseTestMixin
import unittest
from fake_data import FakeData
import sys
import types
reload(sys)
sys.setdefaultencoding('utf-8')


@attr('internal')
@attr('externalopen')
class InvestorAttachmentTest(WBSAPIBaseTestMixin, unittest.TestCase):
    phone = FakeData().phone_number()

    expected_response_format = {
        "success": bool,
        "msg": unicode,
        "errorCode": types.NoneType,
        "data": [
            {
                "id": int,
                "customerId": int,
                "uploader": unicode,
                "memo": unicode,
                "createTime": int,
                "attachments": [
                    {
                        "fileUrl": unicode,
                        "fileName": unicode,
                        "snapFile": unicode,
                        "fileType": int
                    },
                    {
                        "fileUrl": unicode,
                        "fileName": unicode,
                        "snapFile": unicode,
                        "fileType": int
                    }
                ],
                "scope": int,
                "scopeStr": unicode,
                "modify": int,
                "visible": int,
                "uploadType": unicode
            }
        ]
}

    @classmethod
    def setUpClass(cls):
        cls.view_url = 'getCustomerAttachment.json'
        token = cls.generate_investor_token()
        data_dict = {
            "token": token,
            "param": {}
        }
        cls.data = 'data={0}'.format(cls.dict_to_json(data_dict))
        super(InvestorAttachmentTest, cls).setUpClass()