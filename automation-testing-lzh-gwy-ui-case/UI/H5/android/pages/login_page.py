from UI.base_page import BasePage
from ..elements.login_elements import LoginElementCollection


class LoginPage(BasePage):
    view_url = '/#!/wealth'

    def __init__(self, browser):
        self.login_elements = LoginElementCollection()
        self.set_browser(browser)
        self.get_url()

    def login_in(self):
        self.login_elements.confirm_buton.click()
        self.login_elements.login_link.click()
        mobile = '18900000001'
        self.login_elements.mobile(mobile)
        self.login_elements.next_button.click()
        password = '111111q'
        self.login_elements.password(password)
        self.login_elements.login_button.click()
        return mobile, password

