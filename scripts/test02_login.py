import unittest

from parameterized import parameterized

import api
from api.api_employee import ApiEmployee
from tools.read_json import read_json
from tools.assert_common import assert_common


class Testadk(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.api =ApiEmployee()



    @parameterized.expand(read_json("login.json"))
    def test01_post(self,username,mobile,workNumber):
        r = self.api.api_post(username,mobile,workNumber)
        print("新增员工后结果:",r.json())
        api.user_id=r.json().get("data").get("id")
        print("新增员工id",api.user_id)
        assert_common(self,r)

    def test02_put(self,username="真帅"):
        r=self.api.api_put(username)
        print("更新员工的姓名为:",r.json())
        assert_common(self,r)

    def test03_get(self):
        r =self.api.api_get()
        print("查询结果为",r.json())
        assert_common(self,r)


    def test04_delete(self):
        r = self.api.api_delete(api.user_id)
        print("删除员工成功",r.json())
        assert_common(self,r)
