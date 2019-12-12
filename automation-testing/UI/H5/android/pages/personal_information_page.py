from UI.base_page import BasePage
from ..elements.personal_information_elements import PersonalInformationElementCollection


class PersonalInformationPage(BasePage):

    view_url = '/views/personalInformation.html'

    def __init__(self, browser):
        self.personal_information = PersonalInformationElementCollection()
        self.set_browser(browser)
        self.get_url()

    def get_my_info(self):
        return {
            'name': self.personal_information.my_name.get_text(),
            'identity': self.personal_information.identity.get_text(),
            'phone': self.personal_information.my_phone.get_text()
        }
