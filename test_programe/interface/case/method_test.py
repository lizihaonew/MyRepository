#!/usr/bin/python2
# -*- coding: utf-8 -*-
# @Author   : Li ZiHao
# @Time     : 2019/9/19 11:35
# @File     : method_test.py

import time
import unittest
from test_programe.interface.base.base_demo import RunMain
import random
from HTMLTestRunner import HTMLTestRunner


'''
class TestMethod(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("类执行之前会打印，且只打印一次")

    @classmethod
    def tearDownClass(cls):
        print("类执行后会打印，且只打印一次")

    def setUp(self):
        print("每个case执行前都会执行一次")

    def tearDown(self):
        print("每个case执行后都会执行一次")

    def test_01(self):
        print('第一个case！！')

    def test_02(self):
        print('第二个case！！')
'''


class TestMethod(unittest.TestCase):
    username = ''
    password = random.randint(1, 3)

    def setUp(self):
        self.run = RunMain()

    def test_01(self):
        url = 'http://www.imooc.com/m/web/shizhanapi/loadmorepingjia.html'
        data = {
            'cart': '11'
        }
        res = self.run.run_main(url, 'POST', data)
        self.assertEqual(res['data']['errorCode'], 1006)
        globals()['code'] = res['code']
        print("这是我的第一个case！！")

    # @unittest.skip('skip test_02 because cart is null')
    def test_02(self):
        url = 'http://www.imooc.com/m/web/shizhanapi/loadmorepingjia.html'
        data = {
            'cart': ''
        }
        res = self.run.run_main(url,'GET',data)
        self.assertEqual(res['data']['errorCode'], 1006)
        self.assertEqual(res['code'], code)
        print("这是我的第二个case！！")

    @unittest.skipIf(username == '', 'skip test_03 if username is null ')
    def test_03(self):
        url = 'http://www.imooc.com/m/web/shizhanapi/loadmorepingjia.html'
        data = {
            'cart': ''
        }
        res = self.run.run_main(url, 'GET', data)
        self.assertEqual(res['data']['errorCode'], 1006)
        print("这是我的第三个case！！")

    @unittest.skipUnless(password == 2, 'skip test_04 unless password == 2')
    def test_04(self):
        url = 'http://www.imooc.com/m/web/shizhanapi/loadmorepingjia.html'
        data = {
            'cart': ''
        }
        res = self.run.run_main(url, 'GET', data)
        self.assertEqual(res['data']['errorCode'], 1006)
        print("这是我的第四个case！！")

    @unittest.expectedFailure
    def test_05(self):
        url = 'http://www.imooc.com/m/web/shizhanapi/loadmorepingjia.html'
        data = {
            'cart': '11'
        }
        res = self.run.run_main(url, 'POST', data)
        self.assertEqual(res['code'], 300)
        print('这是我的第五个case')


if __name__ == '__main__':
    test_dir = './'
    discover = unittest.defaultTestLoader.discover(
        test_dir,
        pattern='*_test.py'
    )
    now_time = time.strftime('%Y-%m-%d %H_%M_%S')
    report_file = '../report/'+ now_time + '_report.html'
    with open(report_file, 'wb') as fp:
        runner = HTMLTestRunner(
            stream=fp,
            title='TestMethod Report',
            description='This is a test report哈哈'
        )
        runner.run(discover)




