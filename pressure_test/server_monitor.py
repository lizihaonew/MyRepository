# -*- coding: utf-8 -*-
# @Author  : Li Zihao
# @Time    : 2020/8/27 14:57
# @File    : server_monitor.py

"""
该脚本用于获取指定服务器zabbix和grafana监控截图文件，并生成Excel报告文件；
用法：
1.需安装selenium、openpyxl、Pillow
2.需要指定iamge_base_path和excel_base_path
3.需指定浏览器驱动文件位置，本脚本默认使用Chrome浏览器
4.需要给定指定的参数，包括zabbix和grafana监控地址，zabbix监控的开始和结束时间，服务器名称
"""

from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from openpyxl import load_workbook, Workbook
from openpyxl.drawing.image import Image
import time
import re
import os


class ServerMonitor(object):
    iamge_base_path = "E:\\images\\"
    excel_base_path = "E:\\excels\\"
    executable_path = r"D:\Program Files\Python\python37\Scripts\chromedriver.exe"
    grafana_username = 'reader'
    grafana_password = 'reader'

    def __init__(self, name):
        options = webdriver.ChromeOptions()
        self.server_name = name
        options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
        options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
        # options.add_argument('window-size=1920x3000')  # 指定浏览器分辨率
        options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
        options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面

        self.driver = webdriver.Chrome(options=options, executable_path=self.executable_path)
        self.wait = WebDriverWait(self.driver, 10)
        self.folder_path = os.path.join(self.iamge_base_path, (self.server_name + time.strftime('%Y%m%d%H%M%S')))
        if not os.path.exists(self.folder_path):
            os.mkdir(self.folder_path)

    def get_zabbix_image(self, url, start_time, end_time):
        driver = self.driver
        driver.get(url)
        driver.maximize_window()

        begintime = driver.find_element_by_id('begintime')
        begintime.clear()
        begintime.send_keys(start_time)

        endtime = driver.find_element_by_id('endtime')
        endtime.clear()
        endtime.send_keys(end_time)

        driver.find_element_by_xpath('/html/body/div[2]/button[3]').click()
        time.sleep(3)

        check_name = re.findall(r'item_name=([\w.\[\]]+)', url)[0]
        image_name = check_name + '.png'
        image_path = os.path.join(self.folder_path, image_name)
        driver.get_screenshot_as_file(image_path)

    def get_zabbix_all_image(self, url, start_time, end_time):
        items = ['established', 'cpu', 'memfree', 'load', 'timewait', 'net.if.in[eth0]', 'net.if.out[eth0]']
        for item_name in items:
            zabbix_url = re.sub(r'item_name=[\w.\[\]]+', 'item_name=%s' % item_name, url)
            self.get_zabbix_image(zabbix_url, start_time, end_time)

    def get_grafana_image(self, url):
        driver = self.driver
        login_url = 'http://grafana.idc5calicok8s.dangdang.cn/login'
        driver.get(login_url)
        driver.maximize_window()
        driver.find_element_by_name('username').send_keys(self.grafana_username)
        driver.find_element_by_name('password').send_keys(self.grafana_password)
        driver.find_element_by_xpath('//*[@id="login-view"]/form/div[3]/button').click()
        time.sleep(2)
        driver.get(url)

        driver.set_window_size(1000, 2650)
        target = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#panel-69 > div > a")))
        target.location_once_scrolled_into_view
        time.sleep(2)

        image_name = 'grafana.png'
        image_path = os.path.join(self.folder_path, image_name)
        driver.save_screenshot(image_path)

    def get_all_images(self, zabbix_url, start_time, end_time, grafana_url):
        self.get_zabbix_all_image(zabbix_url, start_time, end_time)
        self.get_grafana_image(grafana_url)
        self.driver.close()

    def get_excel_file(self):
        image_folder_path = self.folder_path
        excel_file_name = self.server_name + time.strftime('%Y%m%d%H%M%S') + '.xlsx'
        excel_file_path = os.path.join(self.excel_base_path, excel_file_name)

        book = Workbook()
        sheet = book.active
        sheet.title = "服务器监控报告"

        start = 0

        image_names = os.listdir(image_folder_path)
        if not image_names:
            raise Exception('没有截图文件')

        image_names = [image for image in image_names if '.png' in image]
        image_names.remove('grafana.png')
        image_names.append('grafana.png')

        for i in range(len(image_names)):
            image_path = os.path.join(image_folder_path, image_names[i])
            img = Image(image_path)
            location = 'B%d' % (start + i*32 + 2)
            sheet.add_image(img, location)

        book.save(excel_file_path)
        book.close()
        # os.system('rm -rf %s' % image_folder_path)
        return excel_file_path


if __name__ == '__main__':
    zabbix_url1 = 'http://zabbixserver.dapp.com/tea/hcgraph/graph_spline.php?period=3600&hosts=10.7.9.212,10.7.9.213,10.7.9.214,10.7.9.215,10.7.9.216,10.7.9.217,10.7.9.218,10.7.9.130,10.7.9.131,10.7.9.132,10.7.9.133,10.7.9.134,10.7.9.164,10.7.9.166,10.7.9.168,10.5.20.1,10.5.20.2,10.5.20.3,10.5.20.4,10.5.16.160,10.5.17.160,10.5.16.132,10.5.17.132,10.5.42.23,10.5.19.21,10.5.24.103,10.5.25.103,10.5.25.196&item_name=established'
    grafana_url1 = 'http://grafana.idc5calicok8s.dangdang.cn/d/k8sAppMetrics/k8s-app?orgId=1&var-App=1172&from=1598457600000&to=1598463000000'

    start_time1 = '2020-08-27 00:00:00'
    end_time1 = '2020-08-27 01:30:00'
    server_name = 'mapi'

    sm = ServerMonitor(server_name)
    sm.get_all_images(zabbix_url1, start_time1, end_time1, grafana_url1)
    sm.get_excel_file()


