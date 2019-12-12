# -*- coding: utf-8 -*-
from API.base_api import check_response_data
from API.wbs.base_wbs_api import WBSAPIBaseTestMixin
import unittest
from nose.plugins.attrib import attr
from fake_data import FakeData


@attr('issues')
#@attr('external')
class BatchSurveyTest(WBSAPIBaseTestMixin, unittest.TestCase):
    view_url = 'investor/search.json'

    expected_response_format = {
        "success": bool,
        "msg": unicode,
        "data": [
            {
                "id": int,
                "entId": int,
                "investorId": int,
                "surveyId": int,
                "score": int,
                "riskValue": int,
                "riskName": unicode,
                "minScore": int,
                "maxScore": int,
                "success": bool
            }
        ]
    }

    @classmethod
    def setUpClass(cls):
        cls.data = 'data={"token":' + str(cls.generate_token()) + ',"param": {}}'
        super(BatchSurveyTest, cls).setUpClass()
        investor_id1 = cls.response['data']['data']['list'][0]['investorId']
        investor_id2 = cls.response['data']['data']['list'][1]['investorId']
        cls.view_url = 'investor/batchDoSurvey.json'
        cls.data = 'data={' \
                   '"token":' + str(cls.generate_token()) + \
                   ',"param": ' \
                   '[' \
                   '{' \
                   '"investorId":' + str(investor_id1) + \
                   ', "answers":' \
                   '[' \
                   '{"questionId": "1", "optionId": "2"},' \
                   '{"questionId": "2", "optionId": "6"},' \
                   '{"questionId": "3", "optionId": "10"},' \
                   '{"questionId": "4", "optionId": "14"},' \
                   '{"questionId": "5", "optionId": "17"},' \
                   '{"questionId": "6", "optionId": "20"},' \
                   '{"questionId": "7", "optionId": "25"},' \
                   '{"questionId": "8", "optionId": "31"},' \
                   '{"questionId": "9", "optionId": "35"},' \
                   '{"questionId": "10", "optionId": "41"},' \
                   '{"questionId": "11", "optionId": "43"},' \
                   '{"questionId": "12", "optionId": "49"}' \
                   ']' \
                   '}, ' \
                   '{"investorId":' + str(investor_id2) + \
                   ', "answers":' \
                   '[' \
                   '{"questionId": "1","optionId": "2"},' \
                   '{"questionId": "2","optionId": "6"},' \
                   '{"questionId": "3","optionId": "10"},' \
                   '{"questionId": "4","optionId": "14"},' \
                   '{"questionId": "5","optionId": "17"},' \
                   '{"questionId": "6","optionId": "20"},' \
                   '{"questionId": "7","optionId": "25"},' \
                   '{"questionId": "8","optionId": "31"},' \
                   '{"questionId": "9","optionId": "35"},' \
                   '{"questionId": "10","optionId": "41"},' \
                   '{"questionId": "11","optionId": "43"},' \
                   '{"questionId": "12","optionId": "49"}' \
                   ']' \
                   '}' \
                   ']' \
                   '}'
        cls.response = cls.do_request(cls.data)
