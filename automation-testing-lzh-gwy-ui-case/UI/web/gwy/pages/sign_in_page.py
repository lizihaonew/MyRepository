#coding:utf-8

'''
作者：李子浩
内容：定义顾问云系统登录页面page类
'''

from UI.base_page import BasePage
from ..elements.sign_in_elements import SignInElementCollection
from ..elements.home_page_elements import HomePageElementCollection

class SignInPage(BasePage):
    '''
    顾问云登录页面page类
    '''
    def __init__(self, browser):
        self.sign_in_elements = SignInElementCollection()
        self.home_page_element = HomePageElementCollection()
        self.set_browser(browser)

    def sign_in_to_gwy(self):
        self.sign_in_elements.username('18800080008')
        self.sign_in_elements.password('111111')
        self.sign_in_elements.login_button.click()
        return self.home_page_element.login_title()
