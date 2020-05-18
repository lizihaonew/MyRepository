from UI.base_element import ElementCollection, AsyncElement


class ServiceSupport(ElementCollection):
    def __init__(self):
        self.service_support_add = AsyncElement('#add_serviceSupport')
        self.service_support_add_department = AsyncElement('input[name="_department"]')
        self.service_support_add_phone = AsyncElement('input[name="_phone"]')
        self.service_support_add_clientele = AsyncElement('input[name="_clientele"]')
        self.service_support_add_interior = AsyncElement('input[name="_interior"]')
        self.service_support_add_independent = AsyncElement('input[name="_independent"]')
        self.service_support_add_cancel = AsyncElement('.btn.highlight.js-btn.js-cancel')
        self.service_support_add_confirm = AsyncElement('.btn.highlight.js-btn.js-ok')
        self.service_support_add_delete = AsyncElement('.center.delete_serviceSupport')
        self.service_support_add_delete_ok = AsyncElement('.btn.highlight.js-btn.js-ok')
        self.succeed_tip = AsyncElement('.content.js-tip')
