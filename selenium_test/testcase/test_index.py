from selenium_test.page.index_page import HomePage


class TestRegister:
    def setup_method(self):
        self.home_page = HomePage(reuse=True)

    def test_download_jump(self):
        title_list = self.home_page.goto_download().get_download_item_title()
        assert 'Windows桌面端' in title_list

    def teardown_method(self):
        self.home_page.close()
