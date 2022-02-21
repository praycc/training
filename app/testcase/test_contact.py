from faker import Faker

from app.page_object.app import App
from app.untils.untils import Untils


class TestContact:
    def setup_class(self):
        self.app = App()

    def setup(self):
        #启动app
        self.app.start()

    def teardown(self):
        self.app.back()

    def teardown_class(self):
        self.app.stop()

    def test_add_member(self):
        #测试添加成员功能
        name = Untils.get_name()
        phone= Untils.get_phonenumber()
        result = self.app.got_to_main().go_to_dresslist().click_addmember().addmember_by_manual().edit_memberinfo(name,phone).add_suucess()
        assert result=="添加成功"

    def test_del_member(self):
        #测试删除成员功能
        del_name = 'haoyu7'
        result = self.app.got_to_main().go_to_dresslist().click_personlist(del_name).go_to_personSettings().click_edit_member().del_member().check_member(del_name)
        assert result == True
