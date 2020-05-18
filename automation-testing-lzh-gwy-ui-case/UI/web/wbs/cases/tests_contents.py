from UI.base_case import BaseUITestCase
from ..pages.content_page import InformationPage


class InformationTest(BaseUITestCase):

    def setUp(self):
        self.information_page = InformationPage(self.browser)

    def tests_information(self):
        self.information_page.new_information()