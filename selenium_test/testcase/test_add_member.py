# @Time : 2020-02-14 16:57
from selenium_test.page.add_member_page import AddMemberPage
from selenium_test.page.home_page import HomePage


class TestAddMember:
    def setup_method(self):
        self.home_page = HomePage(reuse=True)

    def test_add_member(self):
        self.home_page.go_add_member().add_member()
