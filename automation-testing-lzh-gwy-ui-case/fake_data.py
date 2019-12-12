# -*- coding: utf-8 -*-
from faker import Factory
import random
import time


class FakeData(object):

    def __init__(self, locale='zh_cn'):
        self.fake = Factory.create(locale=locale)

    def text(self, max_length=20):
        return self.fake.text(max_nb_chars=max_length)[:-1]

    def user_name(self):
        return self.fake.name()

    @staticmethod
    def position_name():
        return '"自动化测试职位{0}"'.format(random.randint(1111, 9999))

    @staticmethod
    def department_name():
        return '"接口自动化名称{0}"'.format(random.randint(1111, 9999))

    @staticmethod
    def department_update_name():
        return '"接口自动化修改名称{0}"'.format(random.randint(1111, 9999))

    def phone_number(self):
        return self.fake.phone_number()

    def email(self):
        return self.fake.email()

    def address(self):
        return self.fake.address()

    @staticmethod
    def bank_name():
        return random.choice(['建设银行', '招商银行', '中国银行', '北京银行'])

    @staticmethod
    def product_category():
        return random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9'])

    @staticmethod
    def product_state():
        return random.choice(['1', '2', '0'])

    @staticmethod
    def product_release():
        return random.choice(['1', '2', '3', '99'])

    @staticmethod
    def product_deadline():
        return random.choice(['1年', '12个月', '2年+1年', '最长18个月'])

    @staticmethod
    def product_annual_yield():
        return random.choice(['15%', '15%-18%', '浮动收益'])

    @staticmethod
    def product_attachment_type():
        return random.choice(['1'])

    @staticmethod
    def id_number():
        return random.choice(['310104198002054660', '42120219930612561X', '231124197907050754'])

    @staticmethod
    def pii():
        """随机生成身份证号"""
        arr = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
        #remove X as last
        last = ('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2')
        #last = ('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2')

        t = time.localtime()[0]
        x = '%02d%02d%02d%04d%02d%02d%03d' % (random.randint(10, 99),
                                              random.randint(01, 99),
                                              random.randint(01, 99),
                                              random.randint(t - 80, t - 18),
                                              random.randint(1, 12),
                                              random.randint(1, 28),
                                              random.randint(1, 999))
        y = 0
        for i in range(17):
            y += int(x[i]) * arr[i]

        return '%s%s' % (x, last[y % 11])
