from selenium_test.page.home_page import HomePage


class TestRegister:
    def setup_method(self):
        self.home_page = HomePage()

    def test_register_post_error(self):
        assert '请选择所属行业' in self.home_page.goto_register().input_corp_name("dfd").register_submit().get_error_messages()

    def teardown_method(self):
        self.home_page.close()
