from appium.webdriver.common.mobileby import MobileBy

from app.page_object.base_page import BasePage
from app.page_object.personSettings_page import PersonSettingsPage


class PersonInfoPage(BasePage):

    def go_to_personSettings(self):
        #点击右上角三个点，打开个人信息设置界面
        self.find_and_click(MobileBy.ID,"com.tencent.wework:id/kc8")
        return PersonSettingsPage(self.driver)

