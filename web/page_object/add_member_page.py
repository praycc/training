import time

from selenium.webdriver.common.by import By

from web.page_object.base_page import BasePage
from web.page_object.contact_page import ContactPage


class AddMemberPage(BasePage):
    # 跳转通讯录
    def goto_contact(self):
        return ContactPage

    def add_member(self,name,accid,phone):
        # 添加成员信息
        self.find(By.ID,'username').send_keys(name)
        self.find(By.ID,'memberAdd_acctid').send_keys(accid)
        self.find(By.ID,'memberAdd_phone').send_keys(phone)


    def add_member_sucess(self,name,accid,phone):
        #添加信息成功跳转通讯录
        self.add_member(name,accid,phone)
        self.find(By.CSS_SELECTOR,'.js_btn_save').click()
        return ContactPage(self.driver)


    def add_member_fail(self,name,accid,phone):
        #添加信息失败提示错误信息
        self.add_member(name,accid,phone)
        time.sleep(2)
        eles = self.driver.find_elements(By.CSS_SELECTOR,'.ww_inputWithTips_WithErr>.ww_inputWithTips_tips')
        err_msg = []
        for ele in eles:
            err_msg.append(ele.text)
        return err_msg
