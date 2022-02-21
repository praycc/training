
from app.page_object.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy

class EditmemberInfoPage(BasePage):
    #编辑成员页面
    def del_member(self):
        #点击删除成员按钮
        from app.page_object.addresslist_page import AddresslistPage
        str = '删除成员'
        self.swipe_find(str)
        self.find_and_click(MobileBy.XPATH,f"//*[@text='{str}']")
        self.find_and_click(MobileBy.ID,"com.tencent.wework:id/ceq")
        return AddresslistPage(self.driver)