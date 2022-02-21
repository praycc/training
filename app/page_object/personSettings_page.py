from appium.webdriver.common.mobileby import MobileBy

from app.page_object.base_page import BasePage
from app.page_object.editmemberInfo_page import EditmemberInfoPage


class PersonSettingsPage(BasePage):

    def click_edit_member(self):
        #点击编辑成员按钮
        self.find_and_click(MobileBy.XPATH,"//*[@text='编辑成员']")
        return EditmemberInfoPage(self.driver)