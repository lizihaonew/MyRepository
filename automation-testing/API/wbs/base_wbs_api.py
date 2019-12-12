from API.base_api import APIBaseTestMixin
import requests
import json
import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class WBSAPIBaseTestMixin(APIBaseTestMixin):
    method = 'post'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    authentication_type = None

    @classmethod
    def _get_internal_api_url(cls):
        test_class_path = str(cls)
        first_cut = 'wbs'
        last_cut = 'tests'
        return {
            "ex_open": "ex/open/investor/",
            "ex": "ex/",
            "internal": (test_class_path.split(first_cut)[1].split(last_cut)[0]).replace('.', '/')
        }

    @classmethod
    def generate_token(cls):
        data_dict = {
            "param":
                {
                    "password": "6846860684f05029abccc09a53cd66f1",
                    "mobile": "18888888888"
                }
        }
        response = requests.post('{0}saas/login.json'.format(cls.base_url),
                                 data='data={0}'.format(cls.dict_to_json(data_dict)),
                                 headers=cls.headers)
        return response.json()['data']['token']

    @classmethod
    def generate_investor_token(cls):
        data_dict = {
            "param":
                {
                    "password": "6846860684f05029abccc09a53cd66f1",
                    "mobile": "15810345678"
                }
        }
        response = requests.post('{0}ex/open/investor/login.json'.format(cls.base_url),
                                 data='data={0}'.format(cls.dict_to_json(data_dict)),
                                 headers=cls.headers)
        return response.json()['data']['token']

    @classmethod
    def setUpClass(cls):
        """
        This is a fixture that will be used in api tests
        """
        if os.getenv('api_type') == 'internal':
            cls.view_url = cls.view_url.split('/')[1] if '/' in cls.view_url else cls.view_url
        cls.view_url = cls._get_internal_api_url()[os.getenv('api_type', None)] + cls.view_url
        cls.response = cls.do_request(cls.data)
