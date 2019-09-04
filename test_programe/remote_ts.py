#coding:utf-8

from selenium.webdriver import Remote
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = Remote(
    command_executor='http://127.0.0.1:5555/wd/hub',
    desired_capabilities={
        'platform': 'ANY',
        'browserName':'chrome',
        'version': '',
        'javascriptEnabled': True
    }
)

driver.get('http://www.baidu.com')
driver.find_element_by_id('kw').send_keys('python')
driver.find_element_by_id('kw').click()
driver.quit()