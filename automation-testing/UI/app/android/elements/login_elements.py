from selenium.webdriver.common.by import By

from UI.base_element import BaseElement, ElementCollection


class LoginElementCollection(ElementCollection):

    def __init__(self):
        self.server_config = BaseElement('cn.newbanker:id/txtDescription', By.ID)
        self.custom_config = BaseElement('cn.newbanker:id/net_demo', By.ID)
        self.confirm = BaseElement('android.widget.Button', By.CLASS_NAME)
        self.phone = BaseElement('cn.newbanker:id/et_phone', By.ID)
        self.password = BaseElement('cn.newbanker:id/et_pwd', By.ID)
        self.login = BaseElement('cn.newbanker:id/btn_login', By.ID)
