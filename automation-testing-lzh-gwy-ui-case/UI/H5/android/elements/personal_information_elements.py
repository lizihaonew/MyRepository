from UI.base_element import AsyncElement, ElementCollection


class PersonalInformationElementCollection(ElementCollection):

    def __init__(self):
        self.my_name = AsyncElement('.name_mark .personName')
        self.identity = AsyncElement('.name_mark .identify_mark')
        self.my_phone = AsyncElement('.weui-cell__ft.myPhone')
        self.exit = AsyncElement('.exitBtn')
