#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : Lizihao
# @Time     : 2019/9/4 21:33
# @File     : demo.py
import json
import unittest
from www.ImoocInterface.base.demo import RunMain

'''
class TestMethod(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print '类执行之前会打印，只打印一次！'

    @classmethod
    def tearDownClass(cls):
        print '类执行之后会打印，只打印一次！'

    def setUp(self):
        print 'test --> setup'

    def tearDown(self):
        print 'test -->tearDown'

    def test_01(self):
        print 'this is test method 01'

    def test_02(self):
        print 'this is test method 02'
'''


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

    def test_02(self):
        url = 'http://www.imooc.com/m/web/shizhanapi/loadmorepingjia.html'
        data = {
            'cart': '12'
        }
        res = self.run.run_main(url, 'POST', data)
        self.assertEqual(res['code'], 200)


if __name__ == '__main__':
    unittest.main()