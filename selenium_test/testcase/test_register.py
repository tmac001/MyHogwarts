from selenium_test.page.home_page import HomePage


class TestRegister:
    def setup_method(self):
        self.home_page = HomePage()

    def test_register_post_error(self):
        page = self.home_page.goto_register().input_corp_name("dfd").select_corp_industry().select_dropdown()
        assert '请填写正确的验证码' in page.register_submit().get_error_messages()

    def test_tmp(self):
        self.home_page.goto_register().select_agree()

    def teardown_method(self):
        self.home_page.close()
