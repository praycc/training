from web.page_object.index_page import IndexPage
class TestAddMember:


    data = ['haoyu3','113','13133333333']
    def test_add_member(self):
        #成功添加成员信息
        index = IndexPage()
        phonelist = index.goto_add_member().add_member_sucess(*self.data).get_members()
        assert self.data[2] in phonelist

    def test_add_member_fail(self):
        #添加重复信息，导致失败
        index = IndexPage()
        err_msg = index.goto_add_member().add_member_fail(*self.data)
        for i in range(len(err_msg)):
            for j in range(len(self.data)):
                if self.data[j] in err_msg[i]:
                    print(err_msg[i])
                    assert True
                    return
        assert False

