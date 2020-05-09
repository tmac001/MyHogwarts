# @Time : 2020-05-04 15:38
from wework_test.api.department import Department
from wework_test.api.wework import WeWork


class TestDepartment:

    def setup(self):
        self.department = Department()

    def test_department_list(self):
        res = self.department.department_list()
        print(res)
        assert len(res["department"]) != 0

    def test_create_department(self):
        res = self.department.create_department("1768", 1)
        print(res)
        assert res["errmsg"] == "created"

    def test_update_department(self):
        res = self.department.update_department(4, name="1768")
        print(res)
        assert res["errmsg"] == "updated"

    def test_delete_department(self):
        res = self.department.delete_department(4)
        print(res)
        assert res["errmsg"] == "deleted"

