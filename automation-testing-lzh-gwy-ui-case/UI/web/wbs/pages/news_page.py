# -*- coding: utf-8 -*-
from UI.base_page import BasePage
from ..elements import news_elements
from fake_data import FakeData
import time


class NewsPage(BasePage):

    view_url = '/html/newsManagement.html'

    def __init__(self, browser):
        self.add_news_elements = news_elements.NewsAddElements()
        self.news_list_elements = news_elements.NewsListElements()
        self.js_information_elements = news_elements.JsInformationElements()
        self.fake = FakeData()
        self.set_browser(browser)
        self.get_url()

    def add_news(self, scope=0):
        self.news_list_elements.add_news.click()
        news_title = u'自动化测试消息标题--{0}'.format(self.fake.text(max_length=5))
        self.add_news_elements.news_title(news_title)
        self.add_news_elements.news_summary(u'自动化测试消息简介--{0}'.format(self.fake.text(max_length=30)))
        self.add_news_elements.news_content(u'自动化测试消息内容--{0}'.format(self.fake.text(max_length=100)))
        self.add_news_elements.sent_button.scroll_into_view()
        # FIXME Have no idea why clicking time control has no response after scrolling, so have to click other space first
        self.add_news_elements.news_sent_scope.outer_consultant_scope.click()
        self.add_news_elements.news_sent_time.time_control.click()
        self.add_news_elements.news_sent_time.now.click()
        current_time = self.get_current_time()
        self.add_news_elements.news_sent_time.hour(int(current_time[current_time.find(" ")+1:current_time.find(':')])+1)
        self.add_news_elements.news_sent_time.confirm.click()
        if scope == 0:
            self.add_news_elements.news_sent_scope.customer_scope.click()
        elif scope == 1:
            self.add_news_elements.news_sent_scope.inter_consultant_scope.click()
        elif scope == 2:
            self.add_news_elements.news_sent_scope.outer_consultant_scope.click()
        self.add_news_elements.sent_button.click()
        self.js_information_elements.confirm.click()
        return news_title

    def get_news_list(self):
        news = self.news_list_elements.news()
        return {
            'news_title': [news[::4][index].text for index in range(0, len(news[::4]))]
        }

    def delete_news(self, index=0):
        self.news_list_elements.delete.click(index)
        self.js_information_elements.confirm.click()

    @staticmethod
    def get_current_time():
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
