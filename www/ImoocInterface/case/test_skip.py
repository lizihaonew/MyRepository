#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : Lizihao
# @Time     : 2019/9/5 21:07
# @File     : test_skip.py

"""
unittest提供了一些跳过指定用例的方法
@unittest.skip(reason)：强制跳转。reason是跳转原因，且reason只能是英文，不支持中文
@unittest.skipIf(condition, reason)：condition为True的时候跳转
@unittest.skipUnless(condition, reason)：condition为False的时候跳转
@unittest.expectedFailure：如果test失败了，这个test不计入失败的case数目
"""

import unittest
from ..base.demo import RunMain
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


class TestSkiping(unittest.TestCase):
    def setUp(self):
        self.run = RunMain()
        error_code2 = 200

    def test_01(self):
        url = 'http://www.imooc.com/m/web/shizhanapi/loadmorepingjia.html'
        data = {
            'cart': '11'
        }
        res = self.run.run_main(url, 'POST', data)
        self.assertEqual(res['code'], 200)
        print '这是我的第一个case'

    @unittest.skip("跳过")
    def test_02(self):
        url = 'http://www.imooc.com/m/web/shizhanapi/loadmorepingjia.html'
        data = {
            'cart': ''
        }
        res = self.run.run_main(url, 'POST', data)
        self.assertEqual(res['code'], 200)
        print '这是我的第二个case'

    def test_03(self):
        url = 'http://www.imooc.com/m/web/shizhanapi/loadmorepingjia.html'
        data = {
            'cart': '11'
        }
        res = self.run.run_main(url, 'POST', data)
        print '这是我的第三个case'
        self.assertEqual(res['code'], 200)
        # globals()['error_code2'] = res['code']
    '''
    @unittest.skipIf(error_code2 == 200, 'error_code2是200的时候不执行')
    def test_04(self):
        url = 'http://www.imooc.com/m/web/shizhanapi/loadmorepingjia.html'
        data = {
            'cart': '11'
        }
        res = self.run.run_main(url, 'POST', data)
        self.assertEqual(res['code'], 200)
        print '这是我的第四个case'

    @unittest.skipUnless(error_code2 == 200, '只有error_code2是200的时候执行')
    def test_05(self):
        url = 'http://www.imooc.com/m/web/shizhanapi/loadmorepingjia.html'
        data = {
            'cart': ''
        }
        res = self.run.run_main(url, 'POST', data)
        self.assertEqual(res['code'], 200)
        print '这是我的第五个case'

    @unittest.expectedFailure
    def test_06(self):
        url = 'http://www.imooc.com/m/web/shizhanapi/loadmorepingjia.html'
        data = {
            'cart': '11'
        }
        res = self.run.run_main(url, 'POST', data)
        self.assertEqual(res['code'], 300)
        print '这是我的第六个case'
'''


if __name__ == '__main__':
    unittest.main()