from UI.base_case import BaseUITestCase
from UI.web.wbs.pages.sign_in_page import SignInPage


class SignInTest(BaseUITestCase):

    def test_sign_in_to_wbs(self):
        sign_in_page = SignInPage(self.browser)
        self.assertIsNotNone(sign_in_page.sign_in_to_wbs(), 'you do not login in to wbs, please recheck')

