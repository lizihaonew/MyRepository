# -*- coding: utf-8 -*-
from API.wbs.base_wbs_api import WBSAPIBaseTestMixin
import unittest
from nose.plugins.attrib import attr


@attr('external')
class InvestorSearchTest(WBSAPIBaseTestMixin, unittest.TestCase):
    view_url = 'investor/search.json'
    expected_response_format = {
        "success": bool,
        "msg": unicode,
        "data": {
            "totalCount": int,
            "list": [
                {
                    "id": int,
                }
            ]
        }
    }

    @classmethod
    def setUpClass(cls):
        cls.data = 'data={"token":' + str(cls.generate_token()) + ',"param": {}}'
        super(InvestorSearchTest, cls).setUpClass()
