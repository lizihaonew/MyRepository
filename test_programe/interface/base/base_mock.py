#!/usr/bin/python2
# -*- coding: utf-8 -*-
# @Author   : Li ZiHao
# @Time     : 2019/9/19 13:06
# @File     : base_mock.py

from mock import Mock


def mock_test(test_method, url, method, req_data, resp_data):
    test_method = Mock(return_value=resp_data)
    res = test_method(url, method, req_data)
    return res