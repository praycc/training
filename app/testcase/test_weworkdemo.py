from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait


class TestWorkbench:
    def setup(self):
        #读取app配置信息
        caps = {
            "platformName": "Android",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.LaunchSplashActivity",
            "noReset": "true",
            "dontStopAppOnReset":"true",
            "setttings[waitForIdleTimeout]":0,
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        # 关闭应用
        self.driver.quit()

    def swipe_find(self,str):
        num = 3
        for i in range(num):
            try:
                ele = self.driver.find_element(MobileBy.XPATH,"//*[@text='打卡']")
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
                duration = 100
                self.driver.swipe(start_x, start_y, end_x, end_y, duration)
            if i == num-1:
                raise NoSuchElementException('未找到该元素')


    def test_daka(self):
        #打卡用例
        self.driver.find_element(MobileBy.XPATH, "//*[@text='工作台']").click()
        # 滑动查找"打卡"文字
        self.swipe_find("打卡").click()
        #只适用于android
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector().scrollable(true).\
        #                          instance(0)).scrollIntoView(new UiSelector().\
        #                          text("打卡").instance(0));').click()
        #点击外出打卡页签
        self.driver.find_element(MobileBy.XPATH,"//*[@text='外出打卡']").click()
        #查找打卡按钮，包含文字"第N次外出打卡"
        self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'次外出')]").click()
        # self.driver.find_element(MobileBy.XPATH,"//*[@text='外出打卡成功']")
        WebDriverWait(self.driver,10).until(lambda x:"外出打卡成功" in x.page_source)

