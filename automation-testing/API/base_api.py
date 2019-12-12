# -*- coding: utf-8 -*-

import functools
import json

import os
import requests

import config
import types


class APIBaseTestMixin(object):
    """
    APIBaseTestMixin

    base_url: Base url to run API against
    view_url: API endpoint
    authentication_type: Which kind of authentication needed to do api call
    auth_username: authenticated username
    auth_password: password
    api_token: token that can be used in internal testing
    method - Which method should API endpoint be called with
    data - Data to send with request
    headers: Additional headers for request
    request_required_fields: List of fields to check that without them API call results in BAD REQUEST 400 status
    expected_response_status: Expected API response status to check in test
    """
    base_url = os.getenv('test_server') or config.Test_Server_Address
    view_url = None

    authentication_type = 'OAUTH'
    auth_username = config.username
    auth_password = config.password
    api_token = config.API_TOKEN

    method = 'get'
    data = None

    headers = {
        'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'
    }
    request_required_fields = tuple()
    expected_response_status = 200
    expected_response_format = None

    @classmethod
    def _get_url(cls, view_url=None):
        """
        Make full API call url
        :param view_url: view url
        :return: full url
        """
        return '{0}{1}'.format(cls.base_url, view_url or cls.view_url)

    def _get_app_secrets(self):
        """
        Get oauth app secrets, this can be implemented depends on the different situation
        """
        pass

    def _get_token_request_data(self):
        """
        Prepare the data of requesting to get access token
        :return: token request data
        """
        client_id, client_secret = self._get_app_secrets()
        return {
            'grant_type': 'password',
            'client_id': client_id,
            'client_secret': client_secret,
            'username': self.auth_username,
            'password': self.auth_password
        }

    def _get_token(self, request_data):
        """
        Receive access token
        """
        token_url = '{0}{1}'.format(self.base_url, '/oauth2/token/')
        token_response = requests.post(token_url, request_data)
        return token_response.json()['access_token']

    @staticmethod
    def dict_to_json(dictionary):
        return json.dumps(dictionary)

    @classmethod
    def do_request(cls, data=None, view_url=None):
        """
        Send request to API with provided data
        :returns response
        """
        url = cls._get_url(view_url)
        if cls.authentication_type == 'OAUTH':
            cls.headers['Authorization'] = 'Bearer {0}'.format(cls._get_token(cls._get_token_request_data()))
        elif cls.authentication_type == 'TOKEN':
            cls.headers['Authorization'] = 'Token {0}'.format(cls.api_token)
        response = getattr(requests, cls.method)(url, data, headers=cls.headers, verify=False)

        try:
            return {'data': json.loads(response.content), 'status_code': response.status_code}
        except ValueError:
            raise Exception('Cannot load JSON from context={0}'.format(response.content))

    def _do_request_without_required_fields(self):
        """
        Request without those required fields and see what happens
        :return: response
        """
        for required_field in self.request_required_fields:
            # This is not suitable for those API whose content type is application/x-www-form-urlencoded; like wbs
            data = {key: value for key, value in self.data.iteritmes() if key != required_field}
            response = self.do_request(data=data)
            self.assertEqual(self.response['status_code'], 400)

    def _check_response_format(self, data, expected_format):
        """
        Check the response format we get is the same as what we provided in the test case
        """
        for field, field_type in expected_format.iteritems():
            self.assertIn(field, data.keys())
            if isinstance(data[field], dict):
                self._check_response_format(data[field], field_type)
            elif isinstance(data[field], types.NoneType) and type(field_type) == type:
                # For some reason, the actual data may not have value and cannot compare with expect data format,
                # So we just skip such None values.
                continue
            elif isinstance(data[field], list):
                if data[field]:
                    for item in data[field]:
                        if isinstance(item, dict):
                            # in this kind of situation, all others should be with the same format with the first child
                            self._check_response_format(item, field_type[0])
                        else:
                            self.assertIsInstance(item, field_type[0])
                else:
                    continue
            else:
                self.assertIsInstance(data[field], field_type)

    def update_expected_response_dynamic_data(self):
        """
        It's just a hook that defining loading of dynamic data here
        """
        pass

    @classmethod
    def setUpClass(cls):
        """
        This is a fixture that will be used in api tests
        """
        super(APIBaseTestMixin, cls).setUpClass()
        cls.response = cls.do_request(cls.data)

    def test_response_status_ok(self):
        self.assertEqual(self.response['status_code'], self.expected_response_status)

    def test_response_format_ok(self):
        self._check_response_format(self.response['data'], self.expected_response_format)

    '''def test_request_required_fields(self):
        self._do_request_without_required_fields()'''


def check_response_data(func):
    """
    It's just a decorator that checking all api response data
    期望json返回值可能有些是动态的，没法写死，所以需要update_dynamic_data
    :param func: test method
    :return: a method that completed wrappering
    """
    @functools.wraps(func)
    def wrapper(instance):
        func(instance)
        instance.update_expected_response_dynamic_data()
        # There's no need to request again cause we did it in setUpClass
        #instance.response = instance._do_request(instance.data)
        for key, value in instance.expected_response.iteritems():
            actual = instance.response['data'][key]
            expected = instance.expected_response[key]
            instance.assertEqual(actual, expected, msg='实际结果:{0} VS 期望结果：{1}'.format(actual, expected))
    return wrapper


'''def check_partial_response_data(func):
    """
    A decorator that checking partial response data
    :param func: test method
    :return: a method that completed wrappering
    """
    @functools.wraps(func)
    def wrapper(instance):
        func(instance)
        instance.update_expected_response_dynamic_data()
        instance.assertDictContainsSubset(instance.expected_response, instance.response['data'])
    return wrapper'''
