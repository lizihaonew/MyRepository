import random
from UI.base_case import BaseUITestCase
from ..pages.news_page import NewsPage


class NewsTest(BaseUITestCase):

    def setUp(self):
        self.news_page = NewsPage(self.browser)

    def tests_add_news(self):
        new_news_title = self.news_page.add_news(scope=random.randint(0, 1))
        self.assertIn(new_news_title, self.news_page.get_news_list()['news_title'])

    def tests_delete_news(self):
        self.news_page.delete_news(index=-1)