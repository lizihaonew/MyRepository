from UI.base_element import ElementCollection, BaseElement, AsyncElement


class HomeElementCollection(ElementCollection):

    def __init__(self):
        self.welcome = AsyncElement('.m-r-sm.text-muted.welcome-message')