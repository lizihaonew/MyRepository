# -*- coding: utf-8 -*-
import pytest
from nose.plugins.attrib import attr
from API.base_api import check_response_data
from ..base_wbs_api import WBSAPIBaseTestMixin
import unittest
from fake_data import FakeData
import sys
import types

reload(sys)
sys.setdefaultencoding('utf-8')


@attr('internal')
@attr('externalopen')
class InvestorGetQuestionInfoTest(WBSAPIBaseTestMixin, unittest.TestCase):
    phone = FakeData().phone_number()

    expected_response_format = {
        "success": bool,
        "msg": unicode,
        "errorCode": types.NoneType,
        "data": {
            "questions": [
                {
                    "id": int,
                    "description": unicode,
                    "seq": int,
                    "type": int,
                    "scoreSection": unicode,
                    "updateTime": int,
                    "typeStr": unicode,
                    "options": [
                        {
                            "id": int,
                            "createdBy": int,
                            "createTime": int,
                            "updatedBy": int,
                            "updateTime": int,
                            "entId": int,
                            "surveyId": int,
                            "questionId": int,
                            "description": unicode,
                            "seq": int,
                            "status": int,
                            "score": int,
                            "optionId": int
                        }
                    ],
                    "questionId": int
                }
            ],
            "crierions": unicode,
            "enableHistory": int
        }
    }

    @classmethod
    def setUpClass(cls):
        cls.view_url = 'list.json'
        token = cls.generate_investor_token()
        data_dict = {
            "token": token,
            "param": {}
        }
        cls.data = 'data={0}'.format(cls.dict_to_json(data_dict))
        super(InvestorGetQuestionInfoTest, cls).setUpClass()
