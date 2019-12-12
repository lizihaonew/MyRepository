from UI.base_page import BasePage
from ..elements.sign_in_element import SignInElementCollection
from ..elements.home_element import HomeElementCollection


class SignInPage(BasePage):

    def __init__(self, browser):
        self.sign_in_elements = SignInElementCollection()
        self.home_elements = HomeElementCollection()
        self.set_browser(browser)

    def sign_in_to_wbs(self):
        self.get_url()
        self.sign_in_elements.username('18877777771')
        self.sign_in_elements.password('a111111')
        self.sign_in_elements.login_button.click()
        return self.home_elements.welcome()

