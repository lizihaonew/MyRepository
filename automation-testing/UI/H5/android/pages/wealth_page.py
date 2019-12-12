from UI.base_page import BasePage
from ..elements.wealth_elements import WealthElementCollection


class WealthPage(BasePage):

    view_url = '/wealth.html'

    def __init__(self, browser):
        self.wealth_elements = WealthElementCollection()
        self.set_browser(browser)
        self.get_url()

    # FIXME: scroll to view and swip both do not work for H5 elements
    def get_my_wealth(self):
        self.wealth_elements.my_wealth.scroll_into_view()
        self.wealth_elements.my_wealth.click()