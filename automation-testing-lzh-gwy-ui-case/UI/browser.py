import selenium
#import appium
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import config
import os


class DriverSingleton(object):

    desired_caps = {
        'web': {
            'Chrome': {
                "browserName": "chrome",
                "version": "",
                "platform": "ANY",
                'chromeOptions': {
                    'args': ['start-maximized']
                }
            },
            'Firefox': {
                "browserName": "firefox",
                "version": "",
                "platform": "ANY",
                "javascriptEnabled": True,
            }
        },
        'app': {
            'Android': {
                'platformName': 'Android',
                'platformVersion': '5.1',
                'deviceName': '45EMGY49DMBM4LZS',
                'appPackage': 'cn.newbanker',
                'appActivity': '.ui.main.WelcomeActivity'
            },
            'IOS': {
            },
            'H5': {
                'platformName': 'Android',
                'platformVersion': '5.1',
                'deviceName': '45EMGY49DMBM4LZS',
                'browserName': 'Chrome'
            }
        }

    }

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DriverSingleton, cls).__new__(cls)
        return cls.instance

    def __init__(self, category=os.getenv('type', None) or 'web:Firefox'):
        driver_type, test_type = self.get_category(category)
        if driver_type == 'web':
            driver = selenium.webdriver
        """else:
            driver = appium.webdriver"""
        # FIXME make all entry point to hub port 4444 later
        port = '4723' if (test_type == 'Android' or test_type == 'IOS') else '4444'
        self.browser = driver.Remote(command_executor='http://192.168.0.82:{0}/wd/hub'.format(port),
                                     desired_capabilities=self.desired_caps[driver_type][test_type])
        #self.browser = driver.Remote(command_executor='http://192.168.0.55:4444/wd/hub',
                                     #desired_capabilities=self.desired_caps[driver_type][test_type])

    @staticmethod
    def get_category(category):
        driver_type = category[:category.find(":")]
        test_type = category[category.find(":")+1:]
        return driver_type, test_type


class BrowserMixin(object):
    browser = None

    def set_browser(self, browser):
        self.browser = browser
