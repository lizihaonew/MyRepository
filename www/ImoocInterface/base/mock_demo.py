#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : Li ZiHao
# @Time     : 2019/9/4 21:33
# @File     : mock_demo.py

from mock import mock


def mock_test(mock_method, url, method, request_data, response_data):
    mock_method = mock.Mock(return_value=response_data)
    res = mock_method(url, method, request_data)
    return res