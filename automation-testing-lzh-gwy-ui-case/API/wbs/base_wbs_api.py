from API.base_api import APIBaseTestMixin
import requests
import json


class WBSAPIBaseTestMixin(APIBaseTestMixin):

    method = 'post'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    authentication_type = None

    @classmethod
    def generate_token(cls):
        response = requests.post('http://192.168.0.222/api/saas/login.json', data='data={"param":{"password":"6846860684f05029abccc09a53cd66f1","mobile":"18877777771"}, "sign":"053b7bc0bd45d5414173d265752e24de"}', headers=cls.headers)
        return json.dumps(response.json()['data']['token'])
