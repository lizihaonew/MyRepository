# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from .. import config
from selenium.webdriver.support.ui import Select, WebDriverWait

from ..base_element import ElementCollection, AsyncElement


class SelectElement(AsyncElement):
    """
    Base element for select controls
    """
    def __call__(self, value=None, index=0):
        WebDriverWait(self.browser, config.ELEMENT_WAIT_TIMEOUT).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, self.locator)),
            "URL: {0} | Waiting for {1}, but didn't show up in time".format(
                self.browser.current_url, self.locator
            )
        )
        elements = self.browser.find_elements_by_css_selector(self.locator)
        s = Select(elements[index])
        if value is not None:
            method = value[:value.find("=")]
            value = value[value.find("=") + 1:]
            if method == "value":
                s.select_by_value(value)
            elif method == "index":
                s.select_by_index(value)
            elif method == "text":
                s.select_by_visible_text(value)
            else:
                raise InvalidLocatorString(value)
        else:
            e = s.first_selected_option
            return str(e.text)

    def all_options(self):
        return Select(self.browser.find_element_by_css_selector(self.locator)).all_selected_options

    def options(self, index=0):
        return Select(self.browser.find_elements_by_css_selector(self.locator)[index]).options


class SelectElementCollection(ElementCollection):
    """
    Base element collection for select controls
    """
    def set_browser(self, browser):
        """
        pass webdriver
        """
        self.browser = browser
        for elements in self.__dict__.itervalues():
            if isinstance(elements, SelectElement):
                elements.set_browser(browser)


class InvalidLocatorString(Exception):
    """
    Exception that if we specified an invalid locator string.
    """
    def _get_message(self):
        """
        get method
        """
        return self._message

    def _set_message(self, message):
        """
        set method
        """
        self._message = message

    message = property(_get_message, _set_message)