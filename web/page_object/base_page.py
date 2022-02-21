import time

import yaml
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:

    _url=''
    def __init__(self,base_driver:WebDriver = None):
        if base_driver == None:
            self.driver = webdriver.Chrome()
            self.driver.get(self._url)

            cookie = yaml.safe_load(open('../conf/cookie.yaml'))
            self.driver.implicitly_wait(10)
            for c in cookie:
                self.driver.add_cookie(c)
            time.sleep(3)
            self.driver.get(self._url)
        else:
            self.driver = base_driver

    def find(self,by,value):
        ele = self.driver.find_element(by=by,value=value)
        print(f'查找到到元素是{ele}')
        return ele
