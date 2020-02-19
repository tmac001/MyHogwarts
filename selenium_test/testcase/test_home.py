# @Time : 2020-02-14 0:25
from selenium_test.page.home_page import HomePage


class TestHome:
    def setup_method(self):
        self.homePage = HomePage(reuse=True)

    def test_goto_add_member(self):
        self.homePage.go_add_member()
