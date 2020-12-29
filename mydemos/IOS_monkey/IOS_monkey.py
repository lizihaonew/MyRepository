# -*- coding: utf-8 -*-
# @Author  : Li Zihao
# @Time    : 2020/11/30 15:08
# @File    : IOS_monkey.py


from datetime import datetime
from appium import webdriver
from random import randint
import os
import configparser

config = configparser.ConfigParser()
config.read('config.conf', encoding='utf-8-sig')
section = 'DEFAULT'
device_name = config.get(section, 'device_name')
app = config.get(section, 'app')
usenew_wda = config.get(section, 'usenew_wda')
is_realdevice = config.get(section, 'is_realdevice')
udid = config.get(section, 'udid')
appium_host = config.get(section, 'appium_host')
appium_port = config.get(section, 'appium_port')
screenshot = config.get(section, 'screenshot')
image_path = config.get(section, 'image_path')
percentage_tap = config.get(section, 'percentage_tap')
percentage_swipe = config.get(section, 'percentage_swipe')
percentage_swipe_down = config.get(section, 'percentage_swipe_down')
run_time = config.get(section, 'run_time')


class IOSMonkey:
    def __init__(self, devicename, app_path, usenewwda=False, realdevice=False, device_udid=""):
        self.device_name = devicename
        self.app = app_path
        self.is_usenew = usenewwda
        self.udid = device_udid
        self.is_realdevice = realdevice

        desired_caps = dict()
        desired_caps['platformName'] = 'IOS'
        desired_caps['deviceName'] = self.device_name
        desired_caps['app'] = self.app
        desired_caps['automationName'] = 'XCUITest'
        desired_caps['useNewWDA'] = self.is_usenew
        if self.is_realdevice:
            desired_caps["xcodeOrgId"] = "ZTW9XPA927"
            desired_caps["xcodeSigningId"] = "iPhone Developer"
            desired_caps["udid"] = self.udid
        try:
            print(desired_caps)
            host = 'http://%s:%s/wd/hub' % (appium_host, appium_port)
            driver = webdriver.Remote(host, desired_caps)
            self.driver = driver
        except Exception as e:
            print(e)
            exit("get driver failed")

    @staticmethod
    def mkdir():
        dir_name = "imgs" + datetime.now().strftime('%y%m%d%H%M%S')
        if image_path:
            base_path = image_path
        else:
            base_path = os.getcwd()
        dir_path = os.path.join(base_path, dir_name)

        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        dirs = os.listdir(dir_path)
        for d in dirs:
            child_f = os.path.join(dir_path, d)
            os.remove(child_f)

        return dir_path

    def random_tap(self):
        if self.driver is not None:
            win_size = self.driver.get_window_size()
            x = randint(1, win_size["width"])
            y = randint(5, win_size["height"] - 5)
            self.driver.tap([(x, y)])

    def swipe_y(self):
        if self.driver is not None:
            win_size = self.driver.get_window_size()
            x = win_size["width"] / 2
            start_y = randint(30, win_size["height"])
            end_y = randint(30, win_size["height"])

            self.driver.swipe(
                start_x=x,
                start_y=start_y,
                end_x=x,
                end_y=end_y,
                duration=1000)

    def swipe_x(self):
        if self.driver is not None:
            win_size = self.driver.get_window_size()
            y = win_size["height"] / 2
            start_x = randint(30, win_size["width"])
            end_x = randint(30, win_size["width"])

            self.driver.swipe(
                start_x=start_x,
                start_y=y,
                end_x=end_x,
                end_y=y,
                duration=1000)

    def save_screenshot(self, ss_path):

        if self.driver is not None:
            try:
                pic_name = self.device_name+datetime.now().strftime('%y%m%d%H%M%S') + \
                    str(randint(1, 60)) + ".png"
                pic_path = os.path.join(ss_path, pic_name)
                self.driver.save_screenshot(pic_path)
            except IOError:
                print("save screenshot failed.")


def main():
    config_message = '''
            Config Message:
            device_name = {0}
            app = {1}
            usenew_wda = {2}
            is_realdevice = {3}
            udid = {4}
            appium_host = {5}
            appium_port = {6}
            screenshot = {7}
            image_path = {8}
            run_time = {12}
            percentage_tap = {9}
            percentage_swipe = {10}
            percentage_swipe_down = {11}
            '''.format(device_name, app, usenew_wda, is_realdevice, udid, appium_host, appium_port, screenshot,
                       image_path, percentage_tap, percentage_swipe, percentage_swipe_down, run_time)
    print(config_message)

    ios_monkey = IOSMonkey(device_name, app)
    dp = ios_monkey.mkdir()

    start_time = datetime.now()
    print("begin.")
    while True:
        random_num = randint(1, 100)
        if random_num < percentage_tap:
            ios_monkey.random_tap()
            if screenshot:
                ios_monkey.save_screenshot(dp)
        elif random_num <= (percentage_tap + percentage_swipe):
            ios_monkey.swipe_y()
            if screenshot:
                ios_monkey.save_screenshot(dp)
        else:
            ios_monkey.swipe_x()
            if screenshot:
                ios_monkey.save_screenshot(dp)
        end_time = datetime.now()
        if (end_time - start_time).seconds >= run_time:
            print("end.")
            break


if __name__ == '__main__':
    main()

