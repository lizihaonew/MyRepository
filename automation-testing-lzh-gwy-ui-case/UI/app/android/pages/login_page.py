from UI.base_page import BasePage
from ..elements.login_elements import LoginElementCollection


class LoginPage(BasePage):

    app_activity = '.ui.loginandregist.LoginActivity'

    def __init__(self, browser):
        self.login_elements = LoginElementCollection()
        self.set_browser(browser)
        self.start_activity()

    def login_in(self):
        self.login_elements.server_config.click()
        self.login_elements.custom_config.click()
        self.login_elements.confirm.click()
        self.login_elements.server_config.click(index=1)
        self.login_elements.custom_config.click()
        self.login_elements.confirm.click()
        self.login_elements.phone('18910345678')
        self.login_elements.password('a111111')
        self.login_elements.login.click()
