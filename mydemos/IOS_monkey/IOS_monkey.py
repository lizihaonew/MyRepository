# -*- coding: utf-8 -*-
# @Author  : Li Zihao
# @Time    : 2020/11/30 15:08
# @File    : IOS_monkey.py


from datetime import datetime
from appium import webdriver
from random import randint, choice
import configparser
import os
from get_ios_log import get_log_file, analyse_log_file, get_device_info, get_app_name
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from send_email import send_email


config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8-sig')
section = 'DEFAULT'
app = config.get(section, 'app')
bundle_id = config.get(section, 'bundleId')
appium_host = config.get(section, 'appium_host')
appium_port = config.get(section, 'appium_port')
percentage_tap = int(config.get(section, 'percentage_tap'))
percentage_swipe = int(config.get(section, 'percentage_swipe'))
percentage_swipe_down = int(config.get(section, 'percentage_swipe_down'))
run_time = int(config.get(section, 'run_time'))
email_recivers = config.get(section, 'email_recivers')
device_udid, device_name, device_version = get_device_info()
app_name = get_app_name(device_udid, bundle_id)


class IOSMonkey:
    def __init__(self):
        desired_caps = dict()
        desired_caps['platformName'] = 'IOS'
        desired_caps['deviceName'] = device_name
        desired_caps['app'] = app
        desired_caps['automationName'] = 'XCUITest'
        desired_caps['bundleId'] = bundle_id
        desired_caps['platformVersion'] = device_version
        desired_caps["udid"] = device_udid
        desired_caps["xcodeOrgId"] = "7KM2N7UNX3"
        desired_caps["xcodeSigningId"] = "iPhone Developer"

        try:
            print(desired_caps)
            host = 'http://%s:%s/wd/hub' % (appium_host, appium_port)
            self.driver = webdriver.Remote(host, desired_caps)
            self.win_size = self.driver.get_window_size()
            # print(self.win_size)
            self.half_y = self.win_size["height"] / 2
            self.half_x = self.win_size["width"] / 2
        except Exception as e:
            print(e)
            exit("get driver failed")

    def random_tap(self):
        if self.driver:
            # win_size = self.driver.get_window_size()
            x = randint(1, self.win_size["width"])
            y = randint(5, self.win_size["height"] - 5)
            print('tap at (%s, %s)' % (x, y))
            self.driver.tap([(x, y)])

    # def swipe_y(self):
    #     if self.driver:
    #         # win_size = self.driver.get_window_size()
    #         x = self.win_size["width"] / 2
    #         start_y = randint(30, self.win_size["height"])
    #         end_y = randint(30, self.win_size["height"])
    #
    #         print('Longitudinal swipe from (%s, %s) to (%s, %s)' % (x, start_y, x, end_y))
    #         self.driver.swipe(
    #             start_x=x,
    #             start_y=start_y,
    #             end_x=x,
    #             end_y=end_y,
    #             duration=1000)

    def swipe_y(self):
        tag_x = choice([1, 2])
        x = self.half_x
        if tag_x == 1:
            # start_y = randint(30, self.win_size["height"]-250)
            start_y = 200
            end_y = start_y + 300
        else:
            # start_y = randint(250, self.win_size["height"]-30)
            start_y = self.win_size["height"]-200
            end_y = start_y - 300

        print('Zongxiang swipe from (%s, %s) to (%s, %s)' % (x, start_y, x, end_y))
        self.driver.swipe(
            start_x=x,
            start_y=start_y,
            end_x=x,
            end_y=end_y,
            duration=500)

    # def swipe_x(self):
    #     if self.driver:
    #         # win_size = self.driver.get_window_size()
    #         y = self.half_y
    #         start_x = randint(30, self.win_size["width"])
    #         end_x = randint(30, self.win_size["width"])
    #
    #         print('Lateral swipe from (%s, %s) to (%s, %s)' % (start_x, y, end_x, y))
    #         self.driver.swipe(
    #             start_x=start_x,
    #             start_y=y,
    #             end_x=end_x,
    #             end_y=y,
    #             duration=1000)

    def swipe_x(self):
        tag_y = choice([1, 2])
        y = self.half_y
        if tag_y == 1:
            # start_x = randint(20, self.win_size["width"] - 220)
            start_x = 30
            end_x = start_x + 300
        else:
            # start_x = randint(180, self.win_size["width"] - 30)
            start_x = self.win_size["width"]-30
            end_x = start_x - 300

        print('Hengxiang swipe from (%s, %s) to (%s, %s)' % (start_x, y, end_x, y))
        self.driver.swipe(
            start_x=start_x,
            start_y=y,
            end_x=end_x,
            end_y=y,
            duration=500)

    def close_driver(self):
        self.driver.quit()

    def wait_element(self, time, element_by, element, msg):
        res = WebDriverWait(self.driver, time). until(
            expected_conditions.presence_of_element_located((element_by, element)), msg)
        return res

    def is_element_exist(self, key, value):
        try:
            res = self.driver.find_element_by_ios_predicate("%s == '%s'" % (key, value))
            return res
        except Exception as e:
            # print(e)
            return False

    def find_element(self, key, value):
        res = self.driver.find_element_by_ios_predicate("%s == '%s'" % (key, value))
        return res

    def find_elements(self, key, value):
        res = self.driver.find_elements_by_ios_predicate("%s == '%s'" % (key, value))
        return res

    def special_cases(self):
        login_name = self.is_element_exist("name", "账号密码登录")    # 登录页面特殊处理
        if login_name:
            print('进入到登录页面')
            # self.find_element("name", "username arrow down").click()
            self.find_element("type", "XCUIElementTypeTextField").click()
            self.find_element("name", "清除文本").click()
            self.find_element("type", "XCUIElementTypeTextField").send_keys('11111')
            passwd_input = self.find_element("value", "请输入密码").send_keys('22222222')
            types = self.find_elements("type", "XCUIElementTypeStaticText")
            print(types)
            self.find_element("name", "登录").click()


def run_loop(times, start_time):
    try:
        ios_monkey = IOSMonkey()
        print('Connect succed and start running...')
        while True:
            pack_name = ios_monkey.is_element_exist("name", app_name)
            if not pack_name:
                ios_monkey.close_driver()
                print("未获取到name=当当测试包的元素")
                run_loop(times, start_time)

            random_num = randint(1, 100)
            if random_num < percentage_tap:
                ios_monkey.random_tap()
            elif random_num <= (percentage_tap + percentage_swipe):
                ios_monkey.swipe_y()
            else:
                ios_monkey.swipe_x()
            end_time = datetime.now()
            if (end_time - start_time).seconds >= run_time:
                print('end at %s' % end_time)
                break
    except Exception as e:
        print(e)
        print('reloading...')
        run_loop(times, start_time)


def main():
    start_time = datetime.now()
    print("Begin at %s" % start_time)
    log_path = get_log_file(device_udid, start_time)
    times = 0
    run_loop(times, start_time)
    res_dict = analyse_log_file(device_udid, log_path)
    print(res_dict)

    content = '本次运行日志，统计结果如下：<br>' + str(res_dict) + '<br><br>具体情况请见附件日志;'
    nums = list(res_dict.values())
    if sum(nums) == 0:
        title = 'IOS自动化结果：无异常'
    else:
        title = 'IOS自动化结果：有异常'
    if ',' in email_recivers:
        recipients = email_recivers.split(',')
    else:
        recipients = [email_recivers]

    file_size = os.path.getsize(log_path)
    if file_size > 20971520:
        content = '本次运行日志，统计结果如下：<br>' + str(res_dict) + \
                  '<br><br>日志文件较大，无法附邮件发送，请查看日志文件：<br>' + log_path
        log_path = None

    send_email(title, content, recipients, log_path)


if __name__ == '__main__':
    main()
