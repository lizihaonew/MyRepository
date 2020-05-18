from UI.base_element import BaseElement, AsyncElement, ElementCollection


class LoginElementCollection(ElementCollection):

    def __init__(self):
        self.confirm_buton = BaseElement('.confirmBtn')
        self.login_link = AsyncElement('.wealth a')
        self.mobile = AsyncElement('input[type="tel"]')
        self.next_button = BaseElement('.next_btn')
        self.password = AsyncElement('input[type="password"]')
        self.login_button = BaseElement('.login_btn')
