from appium.webdriver.common.mobileby import MobileBy
from app.page_object.base_page import BasePage

class EditmemberPage(BasePage):

    def edit_memberinfo(self,name,phone):
        #编辑成员信息，保存
        from app.page_object.addmember_page import AddmemberPage
        self.find_and_input(MobileBy.XPATH,"//*[contains(@text,'姓名')]/..//android.widget.EditText",name)
        self.find_and_input(MobileBy.XPATH,"// *[contains(@text,'手机')]/..//android.widget.EditText",phone)
        self.find_and_click(MobileBy.XPATH,"//*[@text='保存']")
        return AddmemberPage(self.driver)