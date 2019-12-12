from UI.base_element import ElementCollection, AsyncElement


class ServiceCongigurarion(ElementCollection):

    def __init__(self):
        self.add_configurarion = AsyncElement('.btn.btn-w-m.btn-default')
        self.add_configurarion_rank = AsyncElement('input[name="rank"]')
        self.add_configurarion_sort = AsyncElement('input[name="sort"]')
        self.add_configurarion_remark = AsyncElement('textarea[name="remark"]')
        self.add_configurarion_cancel = AsyncElement('.btn.highlight.js-btn.js-cancel')
        self.add_configurarion_confirm = AsyncElement('.btn.highlight.js-btn.js-ok')
        self.update = AsyncElement('._update')
        self.delete = AsyncElement('._delete')
        self.delete_confirm = AsyncElement('.btn.highlight.js-btn.js-ok')
        self.succeed_tip = AsyncElement('.content.js-tip')
