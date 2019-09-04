#coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import unittest

# 基本层
class Base(object):
    def __init__(self, driver, base_url = 'http://mail.163.com'):
        self.driver = driver
        self.base_url = base_url
        self.timeout = 30

    def _open(self, url):
        url_ = self.base_url +url
        # print url_
        self.driver.maximize_window()
        self.driver.get(url_)
        sleep(2)
        assert self.driver.current_url == url_, 'Did ont land on %s' % url_

    def open(self):
        self._open(self.url)

    # *参数个数不是固定的(By.ID, 'kw')
    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def iframe(self, iframeid):
        return self.driver.switch_to.frame(iframeid)

    def iframe_out(self):
        return self.driver.switch_to.default_content()
