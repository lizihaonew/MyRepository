import requests
import unittest
import os
import json


class CheckLatestCodeTest(unittest.TestCase):

    base_api_url = os.getenv('api_server')
    base_investor_url = os.getenv('investor_url')
    base_service_url = os.getenv('service_url')
    insurance = int(os.getenv('insurance'))
    data = 'data={0}'.format(json.dumps({
            "param": {
            }
        }))
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }

    def test_check_interface_latest_code(self):
        response = requests.post(self.base_api_url + '/version/getWbsVersion.json', self.data, headers=self.headers)
        data = json.loads(response.content)
        print response.content
        self.assertEqual(data['data'], 'wbs2.1.6 code freeze')

    def test_check_permission_from_gwy(self):
        pass

    def test_investor_has_latest_code(self):
        page = requests.get(self.base_investor_url+'/views/login.html')
        self.assertIn('2.1.5 code freeze', page.text)

    def test_service_has_latest_code(self):
        page = requests.get(self.base_service_url+'/login')
        if not self.insurance:
            self.assertIn('2.1.6 code freeze', page.text)
        else:
            self.assertIn('2.1.6 insurance', page.text)








