from appium.webdriver.common.mobileby import MobileBy
from app.page_object.base_page import BasePage

class AddmemberPage(BasePage):
    def addmember_by_manual(self):
        #点击手动添加成员，跳转添加成员界面
        from app.page_object.editmember_page import EditmemberPage
        self.find_and_click(MobileBy.XPATH, "//*[@text='手动输入添加']")
        return EditmemberPage(self.driver)


    def add_suucess(self):
        #获取toast信息"添加成功"
        self.driver.implicitly_wait(10)
        result = self.find(MobileBy.XPATH,"//*[@class='android.widget.Toast']").get_attribute('text')
        return result