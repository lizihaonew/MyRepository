import os
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from browser import BrowserMixin, DriverSingleton
import config


class BaseElement(BrowserMixin):
    """
    Base element class
    """
    driver_type, test_type = DriverSingleton.get_category(os.getenv('type', None) or 'web:Chrome')
    locate_way = ''
    locator = ''

    def __init__(self, locator, locate_way=By.CSS_SELECTOR):
        self.locator = locator
        self.locate_way = locate_way

    # def __call__(self, value=None, visible_filter=True, index=0):
    #     """
    #     A method that can cover both get and set
    #     :param value: the value you wanna set for element
    #     :param visible_filter: True if you only wanna handle visible elements
    #     :return: elements or element with setting value
    #     """
    #     elements = self.browser.find_elements(self.locate_way, self.locator)
    #     if value is not None:
    #         elements[index].clear()
    #         elements[index].send_keys(value)
    #     return [e for e in elements if e.is_displayed()] if visible_filter else elements

    def __call__(self, value=None, visible_filter=True, index=0, file_type=False):
        """
        A method that can cover both get and set
        :param value: the value you wanna set for element
        :param visible_filter: True if you only wanna handle visible elements
        :return: elements or element with setting value
        If you wanna set value a file name, please set file_type being True
        """
        elements = self.browser.find_elements(self.locate_way, self.locator)
        if value is not None:
            if not file_type:
                elements[index].clear()
                elements[index].send_keys(value)
            else:
                file_path = os.path.abspath(value)
                elements[index].send_keys(file_path)
        return [e for e in elements if e.is_displayed()] if visible_filter else elements

    def move_to_element(self, index=0, visible_filter=True):
        actions = ActionChains(self.browser)
        elements = self(visible_filter=visible_filter)
        actions.move_to_element(elements[index])
        actions.perform()

    def scroll_into_view(self, index=0, visible_filter=True):
        """
        This is a method to scroll to the element. Due to selenium upgrade, selenium does not go to the elements which
        are not in the view point. 
        """
        self.browser.execute_script('arguments[0].scrollIntoView(false)', self(visible_filter=visible_filter)[index])

    def swipe(self, direction="UP", duration=1000):
        x, y = self._get_size()
        start_x = 0
        start_y = 0
        end_x = 0
        end_y = 0
        if direction == 'UP':
            start_x = x * 0.5
            start_y = y * 0.75
            end_x = start_x
            end_y = y * 0.25
        elif direction == 'Down':
            start_x = x * 0.5
            start_y = y * 0.25
            end_x = start_x
            end_y = y * 0.75
        elif direction == 'Left':
            start_x = x * 0.75
            start_y = y * 0.5
            end_x = x * 0.05
            end_y = start_y
        elif direction == 'Right':
            start_x = x * 0.05
            start_y = y * 0.5
            end_x = x * 0.75
            end_y = start_y
        time.sleep(2)
        self.browser.swipe(start_x, start_y, end_x, end_y, duration)

    def _get_size(self):
        x = self.browser.get_window_size()['width']
        y = self.browser.get_window_size()['height']
        return x, y

    def get_text(self, index=0, visible_filter=True):
        text = self(visible_filter=visible_filter)[index].text.strip()
        if "\n" in text:
            text = text[:text.find("\n")] + text[text.find("\n")+1:]
        return text

    def click(self, index=0, visible_filter=True):
        self(visible_filter=visible_filter)[index].click()

    def wait_until_element_visible(self, timeout=config.ELEMENT_WAIT_TIMEOUT):
        WebDriverWait(self.browser, timeout).until(
            expected_conditions.visibility_of_any_elements_located((By.CSS_SELECTOR, self.locator)),
        )

    def wait_until_element_invisible(self, timeout=config.ELEMENT_WAIT_TIMEOUT):
        WebDriverWait(self.browser, timeout).until(
            expected_conditions.invisibility_of_element_located((By.CSS_SELECTOR, self.locator))
        )


class AsyncElement(BaseElement):
    """
    Base element for those which need to be waited. Like Ajax elements or something invoked by click event.
    """
    def __call__(self, value=None, visible_filter=True, index=0):
        WebDriverWait(self.browser, config.ELEMENT_WAIT_TIMEOUT).until(
            lambda driver: len([e for e in driver.find_elements(self.locate_way, self.locator) if e.is_displayed()]
                               if visible_filter else driver.find_elements_by_css_selector(self.locator)),
            "Waiting for {0} in URL {1}, but it didn't show up in time, please check".format(
                self.locator, self.browser.current_url
            )
        )
        return super(AsyncElement, self).__call__(value, visible_filter, index)


class ElementCollection(BrowserMixin):
    """
    element collection that will be used in specific page instance
    """
    smoke_locators = []

    def set_browser(self, browser):
        super(ElementCollection, self).set_browser(browser)
        for attribute in self.__dict__.itervalues():
            if isinstance(attribute, BaseElement) or isinstance(attribute, ElementCollection):
                attribute.set_browser(browser)