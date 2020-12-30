from UI.base_element import BaseElement, AsyncElement, ElementCollection


class InformationListElements(ElementCollection):

    def __init__(self):
        self.add_information = AsyncElement('#add_information')


class InformationAddElements(ElementCollection):

    def __init__(self):
        self.title = AsyncElement('#title')
        self.author = AsyncElement('#author')
        self.summary = AsyncElement('#summary')
        self.content = AsyncElement('.note-editable')
        self.pic_attach = AsyncElement('#file_img')
        self.text_attach = AsyncElement('input[name="pdfs"]')
        self.confirm = AsyncElement('#_submit')
        self.back = AsyncElement('#go_back')
        self.js_tip = AsyncElement('.js-tip')


class VisibilityScopeElements(ElementCollection):

    def __init__(self):
        self.customer_scope = AsyncElement('#scope_1')
        self.inter_consultant_scope = AsyncElement('#scope_2')
        self.outer_consultant_scope = AsyncElement('#scope_4')