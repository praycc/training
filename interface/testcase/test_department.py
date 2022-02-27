import uuid
import allure
import pytest
from jsonpath import jsonpath

from interface.apis.department import Department

@allure.feature("部门管理")
class TestDepartment:

    def setup(self):
        self.depart = Department()

    def teardown(self):
        pass


    def get_uid(self):
        return str(uuid.uuid1()).split('-')[0]

    @allure.story("新增部门")
    def test_creat_department(self):
        #创建部门
        with allure.step('创建部门'):
            uid = self.get_uid()
            data = {
                       "name": f"广州研发中心_{uid}",
                       "name_en": f"RDGZ_{uid}",
                       "parentid": 1,
                    }
            r = self.depart.creat(data)
        
            #断言返回errcode是否为0
            assert r.json().get('errcode') == 0
            dpt_id = r.json().get('id')
            dpt_list = self.depart.get_list().json()
            expr = f"$.department[?(@.id=={dpt_id})].name"
            name_list = jsonpath(dpt_list,expr)
            #断言创建部门是否存在在部门列表中
            if name_list:
                assert f"广州研发中心_{uid}" == name_list[0]
            else:
                assert 1==2

    @pytest.mark.skip()
    def test_update_department(self):
        #更新部门
        data = {
                   "id": 2,
                   "name": "广州研发中心",
                   "name_en": "RDGZ",
                   "parentid": 1,
                   "order": 1
                }
        r = self.depart.update(data)
        print(r.json())

    @pytest.mark.skip()
    def test_del_department(self):
        #删除部门
        department_id = 2
        r = self.depart.delete_department(department_id)
        print(r.json())

    def test_get_department_list(self):
        #获取部门列表
        r = self.depart.get_list()
        # r.json().get('access_token')
        assert r.json().get('errcode') ==0


