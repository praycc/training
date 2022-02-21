from appium import webdriver

from app.page_object.base_page import BasePage
from app.page_object.main_page import MainPage


class App(BasePage):
    def start(self):
        if self.driver == None:
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
        else:
            self.driver.launch_app()
        return self

    def stop(self):
        self.driver.quit()

    def restart(self):
        pass

    def got_to_main(self):
        return MainPage(self.driver)