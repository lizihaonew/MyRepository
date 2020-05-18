from UI.base_case import BaseUITestCase
from ..pages.login_page import LoginPage


class LoginInCaseTest(BaseUITestCase):

    def setUp(self):
        self.login_page = LoginPage(self.browser)

    def test_login_in(self):
        self.login_page.login_in()
