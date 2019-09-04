#coding:utf-8

from time import sleep
import unittest, random, sys
from model import myunit, function
from page_object.login_page import LoginPage
from page_object.mail_page import MailPage

sys.path.append('./model')
sys.path.append('./page_obj')

class LoginTest(myunit.MyTest):

    def test_login_user_pwd_null(self):
        '''
        用户名、密码为空
        :return: None
        '''
        po = LoginPage(self.driver)
        po.open()
        po.login_action('', '')
        sleep(2)
        self.assertEqual(po.login_error_hint(), u'请输入账号')
        function.insert_img(self.driver, 'user_pwd_null.png')

    def test_login_pwd_null(self):
        '''
        密码为空登录
        :return: None
        '''
        po = LoginPage(self.driver)
        po.open()
        po.login_action('123', '')
        sleep(2)
        self.assertEqual(self.driver, u'请输入密码')
        function.insert_img(self.driver, 'pwd_null.png')

    def test_login_user_pwd_error(self):
        '''
        用户名或密码错误
        :return: None
        '''
        po = LoginPage(self.driver)
        po.open()
        username = 'test' + random.choice('zyxwvutsrqponmlkjihgfedcba')
        po.login_action(username, '123456')
        sleep(2)
        self.assertEqual(self.driver, u'账号或密码错误')
        function.insert_img(self.driver, 'user_pwd_error.png')

    def test_login_successful(self):
        '''
        用户名、密码都正确，登录成功
        :return: None
        '''
        po = LoginPage(self.driver)
        po.open()
        user = 'ldq791918813'
        po.login_action(user, 'xiuxiu060801zhu')
        sleep(2)
        po2 = MailPage(self.driver)
        self.assertEqual(po2.login_success_user(), user + '@163.com')
        function.insert_img(self.driver, 'success.png')





