# -*- coding: utf-8 -*-
from ..base_wbs_api import WBSAPIBaseTestMixin
import unittest


class ReservationSearchTest(WBSAPIBaseTestMixin, unittest.TestCase):
    view_url = '/ex/reservation/search.json'
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
        super(ReservationSearchTest, cls).setUpClass()