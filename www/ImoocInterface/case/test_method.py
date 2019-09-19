#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : Lizihao
# @Time     : 2019/9/4 21:33
# @File     : demo.py

import json
import time
import unittest
from www.ImoocInterface.base.demo import RunMain
from HTMLTestRunner import HTMLTestRunner

'''
class TestMethod(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('类执行之前会打印，只打印一次！')

    @classmethod
    def tearDownClass(cls):
        print('类执行之后会打印，只打印一次！')

    def setUp(self):
        print('test --> setup')

    def tearDown(self):
        print('test -->tearDown')

    def test_01(self):
        print('this is test method 01')

    def test_02(self):
        print('this is test method 02')
'''


class TestMethod(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     print('类执行之前会打印，只打印一次！')
    #
    # @classmethod
    # def tearDownClass(cls):
    #     print('类执行之后会打印，只打印一次！')

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

    # @unittest.skip('test_02')
    def test_02(self):
        # print(userId)
        url = 'http://www.imooc.com/m/web/shizhanapi/loadmorepingjia.html'
        data = {
            'cart': '12'
        }
        res = self.run.run_main(url, 'POST', data)
        self.assertEqual(res['code'], 200)
        print('这是我的第二个case')

    @unittest.skipIf(1 > 2, 'this is skip case!!')
    def test_03(self):
        # print(userId)
        url = 'http://www.imooc.com/m/web/shizhanapi/loadmorepingjia.html'
        data = {
            'cart': '12'
        }
        res = self.run.run_main(url, 'POST', data)
        self.assertEqual(res['code'], 200)
        print('这是我的第三个case')


if __name__ == '__main__':
    # unittest.main()
    '''
    testSuit = unittest.TestSuite()
    testSuit.addTest(TestMethod('test_01'))
    testSuit.addTest(TestMethod('test_02'))
    testSuit.addTest(TestMethod('test_03'))
    # unittest.TextTestRunner(testSuit)
    # unittest.TextTestRunner().run(testSuit)
    
    test_dir = './'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
    nowTime = time.strftime('%Y-%m-%d %H_%M_%S')
    filePath = r"../report/" + nowTime + "_report.html"
    with open(filePath, 'wb') as fp:
        runner = HTMLTestRunner(
            stream=fp,
            title='this is first report',
            description='Implementation Example with:'
        )
        runner.run(discover)
        
    '''
    test_dir = './'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
    now_time = time.strftime('%Y-%m-%d %H_%M_%S')
    report_file = r'../report/' + now_time + '_report.html'
    with open(report_file, 'wb') as fp:
        runner = HTMLTestRunner(
            stream=fp,
            title='this is the test',
            description='this is descrptiono'
        )
        runner.run(discover)

