from selenium_test.page.home_page import HomePage


class TestRegister:
    def setup_method(self):
        self.home_page = HomePage()

    def test_register(self):
        self.home_page.goto_register().input_corp_name("dfd").register_submit()

    def teardown_method(self):
        self.home_page.close()
