from UI.base_element import ElementCollection, AsyncElement
from UI.special_elements.select_element import SelectElement


class ServiceManagent(ElementCollection):

    def __init__(self):
        self.add_classify = AsyncElement('#add_classify')
        self.add_managent_name = AsyncElement('input[name="category_name"]')
        self.add_managent_attribute = SelectElement('select[name="category_type"]')
        self.add_managent_template = AsyncElement('.view_template')
        self.add_managent_cancel = AsyncElement('.btn.highlight.js-btn.js-cancel')
        self.add_managent_confirm = AsyncElement('.btn.highlight.js-btn.js-ok')
        self.sort = AsyncElement('#set_sort')
        self.sort_input = AsyncElement('.sort_input')
        self.sort_save = AsyncElement('.btn.btn-w-m.btn-default')
        self.update = AsyncElement('.update')
        self.delete = AsyncElement('.delete')
        self.check_product = AsyncElement('.view_item')
        self.delete_cancel = AsyncElement('.btn.highlight.js-btn.js-cancel')
        self.delete_confirm = AsyncElement('.btn.highlight.js-btn.js-ok')
        self.succeed_tip = AsyncElement('.content.js-tip')
