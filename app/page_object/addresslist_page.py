from selenium.common.exceptions import NoSuchElementException

from app.page_object.addmember_page import AddmemberPage
from appium.webdriver.common.mobileby import MobileBy
from app.page_object.base_page import BasePage
from app.page_object.personInfo_page import PersonInfoPage


class AddresslistPage(BasePage):

    def click_addmember(self):
        #点击添加成员按钮
        ele_name = "添加成员"
        self.swipe_find(ele_name)
        self.find_and_click(MobileBy.XPATH,f"//*[@text='{ele_name}']")
        return AddmemberPage(self.driver)

    def click_personlist(self,name):
        #点击成员列表，打开成员详细信息
        eles = self.find(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/kvu']/android.widget.TextView",isList=True)
        for ele in eles:
            str = ele.get_attribute('text')
            if str == name:
                ele.click()
                print("找到成员了")
                return PersonInfoPage(self.driver)
            else:
                print(f"{name}未找到")

    def check_member(self,name):
        eles = self.find(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/kvu']/android.widget.TextView",isList=True)
        namelist=[]
        for ele in eles:
            text = ele.get_attribute('text')
            namelist.append(text)
        if name in namelist:
            return False
        else:
            return True