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
class InvestorQualifiedTest(WBSAPIBaseTestMixin, unittest.TestCase):
    phone = FakeData().phone_number()

    expected_response_format = {
        "success": bool,
        "msg": unicode,
        "errorCode": types.NoneType,
        "data": int
    }

    @classmethod
    def setUpClass(cls):
        cls.view_url = 'checkSurveyEnable.json'
        data_dict = {
            "token": cls.generate_investor_token(),
            "param": {}
        }
        cls.data = 'data={0}'.format(cls.dict_to_json(data_dict))
        super(InvestorQualifiedTest, cls).setUpClass()