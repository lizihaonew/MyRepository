#coding:utf-8

'''
作者：李子浩
内容：顾问云系统登录页面元素定义
'''

from UI.base_element import BaseElement, ElementCollection

class SignInElementCollection(ElementCollection):
    '''
    顾问云登录页面元素集合
    '''
    def __init__(self):
        self.username = BaseElement('div:nth-child(1) > input')
        self.password = BaseElement('div:nth-child(2) > input')
        self.login_button = BaseElement('.btn.btn-primary.block.full-width.m-b')

