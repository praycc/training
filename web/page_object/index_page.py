from selenium import webdriver
from selenium.webdriver.common.by import By

from web.page_object.base_page import BasePage
from web.page_object.contact_page import ContactPage
from web.page_object.add_member_page import AddMemberPage
class IndexPage(BasePage):

    _url = "https://work.weixin.qq.com/wework_admin/frame#index"
    def goto_contace(self):
        # 跳转通讯录
        return ContactPage()

    def goto_add_member(self):
        # 跳转添加成员页面
        self.driver.find_element(By.CSS_SELECTOR, ".ww_indexImg_AddMember").click()
        return AddMemberPage(self.driver)
