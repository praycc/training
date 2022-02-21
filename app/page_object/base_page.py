import logging

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException


class BasePage:

    def __init__(self,driver:WebDriver = None):
        self.driver = driver

    def back(self):
        for i in range(3):
            self.driver.back()

    def find(self,by,value,isList = False):
        #查找元素
        self.log_info('find：')
        self.log_info(by)
        self.log_info(value)
        if isList:
            return self.driver.find_elements(by=by,value=value)
        else:
            return self.driver.find_element(by=by,value=value)

    def find_and_click(self,by,value):
        #查找到元素后点击元素
        self.log_info('find and click')
        return self.find(by,value).click()

    def find_and_input(self,by,value,str):
        #查找到元素后输入文字
        self.log_info('find and input')
        return self.find(by,value).send_keys(str)

    def swipe_find(self,str):
        num = 3
        for i in range(num):
            try:
                ele = self.find(MobileBy.XPATH,f"//*[@text='{str}']")
                return ele
            except:
                print(f"第{i}次查找，没有找到{str}")
                size = self.driver.get_window_size()
                width = size.get('width')
                height = size.get('height')
                start_x = width / 2
                start_y = height * 0.75
                end_x = start_x
                end_y = height * 0.4
                duration = 2000
                self.driver.swipe(start_x, start_y, end_x, end_y, duration)
            if i == num-1:
                raise NoSuchElementException('未找到该元素')

    def log_info(self,msg):
        #打印日志
        logging.info(msg)