#coding:utf-8

from selenium import webdriver
import time
import requests
import json
from selenium.webdriver.support.select import Select
import os, random
from faker import Factory
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_token():
    api_url = 'http://192.168.0.212:808/api/gwy/user/login.json'
    request_data = 'data={"param":{"mobile":"18800080008","password":"96e79218965eb72c92a549dd5a330112"},"sign":"2b78538442997ea1b47eda413c91bf95"}'
    HEADER = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    response = requests.post(api_url, data=request_data, headers=HEADER)
    return json.dumps(response.json()['data']['token'])

fake = Factory.create()
driver = webdriver.Chrome()
driver.get('http://192.168.0.212:808')
driver.execute_script('localStorage.setItem("token", %s);'% get_token())
driver.get('http://192.168.0.212:808/html/marketCourseManagement.html') # 目标页面地址
driver.maximize_window()
driver.implicitly_wait(20)
try:
    driver.find_element_by_css_selector('div:nth-child(2) > form > div:nth-child(4) > div > a').click()
    Select(driver.find_element_by_css_selector('#newsForm > div.form-group.form-group-20 > div > select')).select_by_index(2)
    driver.find_element_by_css_selector(
        '#newsForm > div:nth-child(3) > div > label:nth-child(1) > input[type="radio"]').click()
    add_name = 'AutoTestAdd' + str(random.randint(0, 99)).zfill(3)
    driver.find_element_by_css_selector('#newsForm > div:nth-child(5) > div > input').send_keys(add_name)
    img_path = os.path.abspath(r'..\timg.jpeg')
    driver.find_element_by_css_selector(
        '#newsForm > div:nth-child(7) > div > div > span.btn.btn-default.btn-file > input[type="file"]').send_keys(img_path)
    driver.find_element_by_css_selector('#newsForm > div:nth-child(9) > div > input').send_keys('AutoTestUser')
    driver.find_element_by_css_selector('#newsForm > div:nth-child(11) > div > textarea').send_keys(u'这是简介！')
    text = 'abcdefghijklmnopqrstuvwxyz123456789'
    driver.find_element_by_css_selector(
        '#newsForm > div.form-group.form-group-80 > div > div.note-editor.note-frame.panel.panel-default > div.note-editing-area > div.note-editable.panel-body').send_keys(text)
    file_path = os.path.abspath(r'..\timg.jpeg')
    driver.find_element_by_css_selector('#contactAttachments').send_keys(file_path)
    driver.find_element_by_css_selector('#newsForm > div:nth-child(17) > div > input').send_keys(20000)
    driver.find_element_by_css_selector(
        '#newsForm > div:nth-child(19) > div > div > label:nth-child(1) > input[type="checkbox"]').click()
    driver.find_element_by_css_selector('.btn.btn-Save').click()
    WebDriverWait(driver, 10, 0.5).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '.layui-layer-content')))
    title = driver.find_element_by_css_selector(
        'div:nth-child(3) > div > table > tbody > tr:nth-child(1) > td:nth-child(1) > a').text
    print title
    second_type = driver.find_element_by_css_selector(
        'div:nth-child(3) > div > table > tbody > tr:nth-child(1) > td:nth-child(2) > span').text
    print second_type

    driver.find_element_by_css_selector(
        'div:nth-child(3) > div > table > tbody > tr:nth-child(1) > td:nth-child(1) > a').click()
    text_detail = driver.find_element_by_css_selector(
        '#form > div > fieldset > div > div > div:nth-child(5) > div > span').text
    print text_detail
    driver.find_element_by_css_selector('#page-wrapper > div > div > div > div > div.ibox-title > div > a').click()

    driver.find_element_by_css_selector(
        'div:nth-child(3) > div > table > tbody > tr:nth-child(1) > td:nth-child(7) > a:nth-child(1)').click()
    driver.find_element_by_css_selector('#newsForm > div:nth-child(5) > div > input').clear()
    driver.find_element_by_css_selector('#newsForm > div:nth-child(5) > div > input').send_keys('AutoTestUpdateTitle')
    driver.find_element_by_css_selector('.btn.btn-Save').click()
    WebDriverWait(driver, 10, 0.5).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '.layui-layer-content')))
    title = driver.find_element_by_css_selector(
        'div:nth-child(3) > div > table > tbody > tr:nth-child(1) > td:nth-child(1) > a').text
    print title

    driver.find_element_by_css_selector('#cp_name').send_keys('AutoTestUpdateTitle')
    driver.find_element_by_css_selector('#_query').click()
    title = driver.find_element_by_css_selector(
        'div:nth-child(3) > div > table > tbody > tr:nth-child(1) > td:nth-child(1) > a').text
    print title

    driver.find_element_by_css_selector(
        'div:nth-child(3) > div > table > tbody > tr:nth-child(1) > td:nth-child(7) > a:nth-child(2)').click()
    driver.find_element_by_css_selector(
        'body > div.alertBox3 > div > div.content-wrapper > label > b.confirm-btn').click()
    success_tip = driver.find_element_by_css_selector('.layui-layer-content').text
    print success_tip

except Exception as e:
    print e

time.sleep(3)
driver.quit()
