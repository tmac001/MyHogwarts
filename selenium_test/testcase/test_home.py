from selenium_test.page.home_page import HomePage


class TestRegister:
    def setup_method(self):
        self.home_page = HomePage()

    def test_download_jump(self):
        title_list = self.home_page.goto_download().get_download_item_title()
        assert 'Windows桌面端' in title_list

    def teardown_method(self):
        self.home_page.close()
