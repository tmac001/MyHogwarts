# @Time : 2020-03-02 14:44
from appium_test.page.app import App


class TestCenter:
    def setup(self):
        self.center = App().start().main().goto_center()

    def test_login_by_password(self):
        self.center.login_by_password("15399714420", "123123321")
        assert "错误" in self.center.get_error_msg()





