from UI.base_element import AsyncElement, ElementCollection


class WealthElementCollection(ElementCollection):

    def __init__(self):
        self.my_wealth = AsyncElement('.wealth_top')