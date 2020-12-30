from contextlib import contextmanager
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.support.wait import WebDriverWait
from UI.browser import DriverSingleton

import config
from browser import BrowserMixin
from base_element import ElementCollection


class BasePage(BrowserMixin):
    """
    Base page class
    """
    view_url = ''
    slug = None
    app_package = 'cn.newbanker'
    app_activity = ''
    driver_type, test_type = DriverSingleton.get_category(os.getenv('type', None) or 'web:Firefox')
    project_name = os.getenv("project", None) or 'wbs'

    def set_browser(self, browser):
        super(BasePage, self).set_browser(browser)
        for attribute in self.__dict__.itervalues():
            if isinstance(attribute, ElementCollection):
                attribute.set_browser(browser)

    def get_url(self):
        """
        open a page
        """
        self._get_url()

    def start_activity(self):
        """
        This is specific for android
        :return: 
        """
        self.browser.start_activity(self.app_package, self.app_activity)

    def _get_url(self):
        url = config.TEST_SERVER_ADDRESS[self.driver_type][self.project_name] + self.view_url
        self.browser.get(url)

    def get_current_url(self):
        """
        get current url of opening page
        """
        return self.browser.current_url

    @contextmanager
    def wait_for_page_load(self, element=None):
        """
        Wait until page loaded, if element assigned, wait specific element loaded and otherwise wait full page
        :param element: 
        :return: 
        """
        old_page = self.browser.find_element_by_tag_name('html') if not element else element
        yield
        WebDriverWait(self.browser, config.ELEMENT_WAIT_TIMEOUT).until(
            staleness_of(old_page),
            'The page {0} is not refreshed'.format(self.get_current_url())
        )

    def get_all_window_handles(self):
        return self.browser.window_handles

    def switch_to_window(self, window_name):
        self.browser.switch_to_window(window_name)

    def switch_to_div_alert(self):
        """
        This is made to handle those div kind of alert dialog
        """
        self.browser.switch_to.default_content()

    def refresh_page(self):
        self.browser.refresh()

    def wait_success_tip_visible(self):
        '''
        wait until success tip visible
        :return: None
        '''
        WebDriverWait(self.browser, 20, 0.5).until(
            EC.visibility_of_any_elements_located((By.CSS_SELECTOR, ".layui-layer-content")))

    def wait_success_tip_invisible(self):
        '''
        wait until success tip invisible
        :return: None
        '''
        WebDriverWait(self.browser, 20, 0.5).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, ".layui-layer-content")))




