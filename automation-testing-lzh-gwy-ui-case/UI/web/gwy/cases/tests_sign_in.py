#coding:utf-8

'''
作者：李子浩
内容：顾问云登录case类
'''

from UI.base_case import BaseUITestCase
from ..pages.sign_in_page import SignInPage

class TestSignIn(BaseUITestCase):
    '''
    顾问云登录case类
    '''
    def test_sign_in_gwy_success(self):
        sign_in_page = SignInPage(self.browser)
        self.assertIsNotNone(sign_in_page.sign_in_to_gwy(), 'you do not login in to wbs, please recheck')
