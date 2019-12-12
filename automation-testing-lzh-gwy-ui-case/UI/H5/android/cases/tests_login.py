from UI.base_case import BaseUITestCase
from ..pages.login_page import LoginPage
from ..pages.personal_information_page import PersonalInformationPage
import time


class LoginInCase(BaseUITestCase):

    def test_login_in(self):
        login_page = LoginPage(self.browser)
        mobile, password = login_page.login_in()
        time.sleep(2)
        my_info_page = PersonalInformationPage(self.browser)
        self.assertEqual(mobile, my_info_page.get_my_info()['phone'])

