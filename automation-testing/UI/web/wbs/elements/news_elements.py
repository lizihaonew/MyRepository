from UI.base_element import BaseElement, AsyncElement, ElementCollection


class NewsListElements(ElementCollection):

    def __init__(self):
        self.add_news = AsyncElement('#add_position')
        self.news = AsyncElement('.gradeX td')
        self.delete = AsyncElement('.delete_news')


class NewsAddElements(ElementCollection):

    def __init__(self):
        self.news_title = AsyncElement('#title')
        self.news_summary = AsyncElement('#summary')
        self.news_content = AsyncElement('.note-editable')
        self.news_sent_time = CalendarElements()
        self.news_sent_scope = SentScopeElements()
        self.sent_button = AsyncElement('#_add')
        self.back_button = AsyncElement('#go_back')


class CalendarElements(ElementCollection):

    def __init__(self):
        self.time_control = AsyncElement('#time')
        self.date_prev_button = AsyncElement('.cxcalendar_hd .prev')
        self.date_next_button = AsyncElement('.cxcalendar_hd .next')
        self.days = AsyncElement('.cxcalendar_bd .days li')
        self.now = AsyncElement('.cxcalendar_bd .days .now')
        self.hour = AsyncElement('.intime .hour')
        self.min = AsyncElement('.intime .mint')
        self.sec = AsyncElement('.intime .secs')
        self.confirm = AsyncElement('.confirm')


class SentScopeElements(ElementCollection):

    def __init__(self):
        self.customer_scope = AsyncElement('#scope_1')
        self.inter_consultant_scope = AsyncElement('#scope_2')
        self.outer_consultant_scope = AsyncElement('#scope_4')


class JsInformationElements(ElementCollection):

    def __init__(self):
        self.confirm = AsyncElement('.js-ok')
        self.cancel = AsyncElement('.js-cancel')