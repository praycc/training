from app.page_object.addresslist_page import AddresslistPage
from appium.webdriver.common.mobileby import MobileBy

from app.page_object.base_page import BasePage


class MainPage(BasePage):

    def go_to_dresslist(self):
        #点击通讯录按钮
        self.find_and_click(MobileBy.XPATH,"//*[@text='通讯录']")
        return AddresslistPage(self.driver)
