#coding:utf-8

from selenium import webdriver
import time
import requests

def get_token():
    api_url = 'http://192.168.0.212:808/api/gwy/user/login.json'
    request_data = 'data={"param":{"mobile":"18800080008","password":"96e79218965eb72c92a549dd5a330112"},"sign":"2b78538442997ea1b47eda413c91bf95"}'
    HEADER = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }

    res = requests.post(api_url, data=request_data, headers=HEADER).json()
    return res

driver = webdriver.Chrome()
driver.get('http://192.168.0.212:808/html/marketTypeManagement.html')

time.sleep(3)
# driver.add_cookie({'name': 'token', 'value': 'f53fe0f1-504b-4cac-adde-eb17e42fde72'})
driver.execute_script('localStorage.setItem("token", arguments["token"]);', get_token()['data'])

time.sleep(5)
driver.quit()
