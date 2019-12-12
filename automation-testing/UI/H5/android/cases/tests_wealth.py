from UI.base_case import BaseUITestCase
from ..pages.wealth_page import WealthPage
from ..pages.login_page import LoginPage
import time


class WealthTest(BaseUITestCase):

    def setUp(self):
        LoginPage(self.browser).login_in()
        time.sleep(1)
        self.wealth_page = WealthPage(self.browser)

    def tests_my_wealth(self):
        self.wealth_page.get_my_wealth()