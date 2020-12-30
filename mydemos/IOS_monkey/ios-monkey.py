# coding:utf-8
# author:wangsuqiang
# create time:2020/6/15

from datetime import datetime
from appium import webdriver
from random import randint
import os


class IOSMonkey:

    def __init__(self, device_name, app=None,
                 usenew_wda=False,
                 is_realdevice=False,
                 udid=""
                 ):

        self.device_name = device_name
        self.app = app
        self.is_usenew =usenew_wda
        self.udid = udid
        self.is_realdevice = is_realdevice

        desired_caps = {}
        desired_caps['platformName'] = 'iOS'
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
            driver = webdriver.Remote(
                'http://localhost:4723/wd/hub', desired_caps)
            self.driver = driver

        except Exception as e:
            print(e)
            exit("get driver failed")

    def mkdir(self, dir_name="imgs"):

        dir_path = os.path.join(os.getcwd(), dir_name)

        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        dirs = os.listdir(dir_path)
        for dir in dirs:
            child_f = os.path.join(dir_path, dir)
            os.remove(child_f)

        return dir_path

    def random_tap(self):
        if self.driver is not None:
            win_size = self.driver.get_window_size()
            # print(win_size)
            x = randint(1, win_size["width"])
            y = randint(5, win_size["height"] - 5)
            self.driver.tap([(x, y)])

    def random_swipe(self):
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

    def swipe_y(self):

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


if __name__ == '__main__':
    device_name = "iPhone SE (2nd generation)"
    # app = ""
    iosmonkey = IOSMonkey(device_name)
    dp = iosmonkey.mkdir()

    # monkey run time: seconds,default 5 min
    run_time = 300
    start_time = datetime.now()
    print("begin.")
    while True:
        random_num = randint(1, 100)
        if random_num < 60:
            iosmonkey.random_tap()
            iosmonkey.save_screenshot(dp)
        elif random_num <= 80:
            iosmonkey.random_swipe()
            iosmonkey.save_screenshot(dp)

        else:
            iosmonkey.swipe_y()
            iosmonkey.save_screenshot(dp)
        end_time = datetime.now()

        if (end_time - start_time).seconds >= run_time:
            print("end")
            break

