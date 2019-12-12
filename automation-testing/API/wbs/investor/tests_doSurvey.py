# -*- coding: utf-8 -*-
from API.base_api import check_response_data
from API.wbs.base_wbs_api import WBSAPIBaseTestMixin
import unittest
from nose.plugins.attrib import attr
import os
from fake_data import FakeData


@attr('issues')
#@attr('internal')
#@attr('external') list.json is not available in ex controller
#@attr('externalopen')
class SingleSurveyTest(WBSAPIBaseTestMixin, unittest.TestCase):
    view_url = 'list.json'

    expected_response_format = {
        "success": bool,
        "msg": unicode,
        "data": {
            "id": int,
            "entId": int,
            "investorId": int,
            "surveyId": int,
            "score": int,
            "riskValue": int,
            "riskName": unicode,
            "minScore": int,
            "maxScore": int,
            "riskValueId": int
        }
    }

    @classmethod
    def setUpClass(cls):
        cls.data = 'data={"token":' + str(cls.generate_investor_token()) + ',"param": {}}'
        super(SingleSurveyTest, cls).setUpClass()
        survey_id = cls.response['data']['data']['id']
        cls.view_url = 'investor/doSurvey.json' if os.getenv('api_type')=='ex' else 'doSurvey.json'
        cls.data = 'data={"token":' + str(cls.generate_token()) + ',"param": {"surveyId":' + str(survey_id) + \
           ', "answers":' \
           '[{"questionId": "1", "optionId": ["2"]},' \
           '{"questionId": "2", "optionId": ["6"]},' \
           '{"questionId": "3", "optionId": ["10"]},' \
           '{"questionId": "4", "optionId": ["14"]},' \
           '{"questionId": "5", "optionId": ["17"]},' \
           '{"questionId": "6", "optionId": ["20"]},' \
           '{"questionId": "7", "optionId": ["25"]},' \
           '{"questionId": "8", "optionId": ["31"]},' \
           '{"questionId": "9", "optionId": ["35"]},' \
           '{"questionId": "10", "optionId": ["41"]},' \
           '{"questionId": "11", "optionId": ["43"]},' \
           '{"questionId": "12", "optionId": ["49"]}]}}'
        super(SingleSurveyTest, cls).setUpClass()
