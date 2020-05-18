#coding:utf-8

'''
作者：李子浩
内容：顾问云主页元素集合定义
'''

from UI.base_element import BaseElement, ElementCollection, AsyncElement

class HomePageElementCollection(ElementCollection):
    '''
    主页元素集合定义类
    '''
    def __init__(self):
        self.login_title = AsyncElement('.logoTitle.fl')