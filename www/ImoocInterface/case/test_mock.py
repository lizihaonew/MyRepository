#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : Lizihao
# @Time     : 2019/9/4 21:33
# @File     : demo.py

import unittest
from www.ImoocInterface.base.demo import RunMain
from mock import Mock
from www.ImoocInterface.base.mock_demo import mock_test


class TestMethod(unittest.TestCase):

    def setUp(self):
        self.run = RunMain()

    def test_01(self):
        url = 'http://www.imooc.com/m/web/shizhanapi/loadmorepingjia.html'
        data = {
            'cart': '11'
        }
        res = self.run.run_main(url, 'POST', data)
        self.assertEqual(res['code'], 200)
        globals()['userId'] = 2003
        print('这是我的第一个case')

    def test_02(self):
        url = 'http://www.imooc.com/m/web/shizhanapi/loadmorepingjia.html'
        data = {
            'cart': '12'
        }
        mock_data = {
            'username': 'xiaolizi',
            'password': '1234567',
            'code': 200
        }
        self.run.run_main = Mock(return_value=mock_data)
        res = self.run.run_main(url, 'POST', data)
        print(res)
        self.assertEqual(res['code'], 200)

    def test_03(self):
        url = 'http://www.imooc.com/m/web/shizhanapi/loadmorepingjia.html'
        data = {
            'cart': '12'
        }
        mock_data = {
            'username': 'xiaolizi',
            'password': '1234567',
            'code': 200
        }
        res = mock_test(self.run.run_main,url,'POST',data,mock_data)
        print(res)
        self.assertEqual(res['code'], 200)


if __name__ == '__main__':
    unittest.main()

