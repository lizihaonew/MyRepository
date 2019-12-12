#!/usr/bin/python2
# -*- coding: utf-8 -*-
# @Author   : Li ZiHao
# @Time     : 2019/9/19 12:59
# @File     : mock_test.py

import unittest
from mock import Mock
from test_programe.interface.base.base_demo import RunMain
from test_programe.interface.base.base_mock import mock_test


class TestMock(unittest.TestCase):
    def setUp(self):
        self.run = RunMain()

    def test_01(self):
        url = 'http://www.imooc.com/m/web/shizhanapi/loadmorepingjia.html'
        data = {
            'cart': '11'
        }
        res = self.run.run_main(url, 'POST', data)
        self.assertEqual(res['code'], 200)

    def test_02(self):
        url = 'http://www.imooc.com/m/web/shizhanapi/loadmorepingjia.html'
        data = {
            'cart': '11'
        }
        mock_data = {
            'username': 'xiaolizi',
            'password': '1234567',
            'code': 2001
        }
        self.run.run_main = Mock(return_value=mock_data)
        res = self.run.run_main(url, 'POST', data)
        self.assertEqual(2001, res['code'])

    def test_03(self):
        url = 'http://www.imooc.com/m/web/shizhanapi/loadmorepingjia.html'
        data = {
            'cart': '11'
        }
        mock_data = {
            'username': 'xiaolizi',
            'password': '1234567',
            'code': 2001
        }
        res = mock_test(self.run.run_main, url, 'POST', data, mock_data)
        self.assertEqual(2001, res['code'])


if __name__ == '__main__':
    unittest.main()



