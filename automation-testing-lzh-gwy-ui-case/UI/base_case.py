import unittest
import sys
import os
import requests
import time
import json

import config
from browser import DriverSingleton
from base_element import BaseElement, ElementCollection


class BaseUITestCase(unittest.TestCase):
    """
    Base test case for newbanker UI testing
    """

    SCREENSHOTS_DIR = 'screenshots'
    driver_type, test_type = DriverSingleton.get_category(os.getenv('type', None) or 'web:Firefox')
    project_name = os.getenv("project", None) or 'wbs'

    @classmethod
    def setUpClass(cls):
        super(BaseUITestCase, cls).setUpClass()
        cls.browser = DriverSingleton().browser
        cls.browser.get(config.TEST_SERVER_ADDRESS[cls.driver_type][cls.project_name])
        if cls.driver_type == 'web':
            cls._dummy_login()
            # maximize_window does not work well for chrome
            if cls.test_type == 'Chrome':
                cls.browser.set_window_size(1440, 900)
            cls.browser.maximize_window()

    @classmethod
    def tearDownClass(cls):
        super(BaseUITestCase, cls).tearDownClass()
        cls.browser.quit()

    @staticmethod
    def _is_failed():
        """
        Check if there's error when running specific case
        """
        return sys.exc_info()[0]

    def _save_screenshots(self):
        snapshot_name = '{0}/{1}_{2}.png'.format(self.SCREENSHOTS_DIR, self.id(), time.asctime().replace(' ', '_'))
        self.browser.save_screenshot(snapshot_name)

    def tearDown(self):
        if self._is_failed():
            self._save_screenshots()

    @classmethod
    def _get_user_data_from_login_api(cls):
        response = requests.post('{0}{1}'.format(config.TEST_SERVER_ADDRESS[cls.driver_type][cls.project_name], config.dict_data[cls.project_name]['LOGIN_API_ENDPOINT']),
                                 data=config.dict_data[cls.project_name]['DATA'], headers=config.dict_data[cls.project_name]['HEADER'])
        return json.dumps(response.json()['data'])

    # @classmethod
    # def _get_user_data_from_login_api(cls):
    #     response = requests.post('{0}{1}'.format(config.TEST_SERVER_ADDRESS[cls.driver_type][cls.project_name], config.LOGIN_API_ENDPOINT[cls.project_name]),
    #                              data=config.DATA[cls.project_name], headers=config.HEADER[cls.project_name])
    #     return json.dumps(response.json()['data'])

    @classmethod
    def _dummy_login(cls):
        """
        Dummy login by setting userData key to H5 local Storage
        """
        storage = config.dict_data[cls.project_name]['Storage']
        if cls.project_name == 'wbs':
            cls.browser.execute_script('localStorage.setItem("%s", arguments[0]);'% storage,
                                        cls._get_user_data_from_login_api()
                                        )
        elif cls.project_name == 'gwy':
            tokens = json.dumps(json.loads(cls._get_user_data_from_login_api())['token'])
            cls.browser.execute_script('localStorage.setItem("%s", %s);'% (storage, tokens))


class SmokeTestMixin(object):

    page_class = None
    page_instance = None

    def _get_page(self):
        if self.page_instance is None:
            self.page_instance = self.page_class(self.browser)
        self.page_instance.get_url()

    def _check_element(self, element_collection, slug=None):
        locators = element_collection.smoke_locators
        if slug is not None:
            locators = locators[slug]
            for locator in locators:
                each_element = getattr(element_collection, locator)
                if isinstance(each_element, BaseElement):
                    each_element = each_element()
                    self.assertGreater(
                        len(each_element), 0,
                        "Locator {0} is not found on page: {1}".format(
                            locator, self.page_instance.get_current_url()
                        )
                    )

    def test_response_content_contains_selectors(self):
        self._get_page()
        for element_collection in self.page_instance.__dict__.itervalues():
            if isinstance(element_collection, ElementCollection):
                self._check_element(element_collection, self.page_instance.slug)

