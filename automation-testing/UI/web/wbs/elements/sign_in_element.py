from UI.base_element import ElementCollection, BaseElement, AsyncElement


class SignInElementCollection(ElementCollection):

    def __init__(self):
        self.username = BaseElement('#_account')
        self.password = BaseElement('#_password')
        self.login_button = BaseElement('#_login')
