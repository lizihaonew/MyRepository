from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from UI import config

from UI.base_element import AsyncElement


class Select2Element(AsyncElement):
    """
    Base element for select2 controls
    """

    def __call__(self, value=None, index=0):
        self.element = self._find_select2_elements(self.locator)[index]
        if value is not None:
            method = value[:value.find("=")]
            value = value[value.find("=")+1:]
            if method == 'search_input':
                self.input_from_search_box(value, index)
            elif method == "select_index":
                self.select_by_index(int(value), index)
            elif method == "select_text":
                self.select_by_visible_text(value)
            else:
                raise InvalidLocatorString(value)
        else:
            return self.get_chosen_option()

    def _find_select2_elements(self, locator):
        WebDriverWait(self.browser, config.ELEMENT_WAIT_TIMEOUT).until(
            lambda driver: expected_conditions.visibility_of_any_elements_located((By.CSS_SELECTOR, locator)),
            "Waiting for {0} in URL {1}, but didn't show up in time".format(
                locator, self.browser.current_url
            )
        )
        return self.browser.find_elements_by_css_selector(locator)

    def _click_select_arrow(self, index=0):
        locator = '{0} .select2-selection__arrow'.format(self.locator)
        self._find_select2_elements(locator)[index].click()

    def _open(self, index=0):
        if not self._is_open:
            self._click_select_arrow(index)

    def _close(self):
        if not self._is_open:
            self._click_select_arrow()

    @staticmethod
    def _element_has_class(element, param):
        class_name = element.get_attribute('class')
        return param in class_name

    @property
    def _is_open(self):
        return self._element_has_class(self.element, 'select2-container--open')

    @property
    def _input_search(self):
        return self._find_select2_elements('.select2-search__field')

    def options(self):
        return self._find_select2_elements('.select2-results__option')

    @property
    def _chosen_option(self):
        locator = '{0} .select2-selection__rendered'.format(self.locator)
        return self._find_select2_elements(locator)[0]

    def select_by_index(self, value, index):
        self._open(index)
        self.options()[value].click()

    def select_by_visible_text(self, text):
        pass

    def input_from_search_box(self, text, index):
        self._open(index)
        self._input_search.send_keys(text)
        self._input_search.send_keys(Keys.ENTER)

    def get_chosen_option(self):
        return self._chosen_option.text.strip()


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
