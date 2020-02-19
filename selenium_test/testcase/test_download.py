from selenium_test.page.base_page import BasePage
from selenium_test.page.index_page import HomePage


class TestDownload:
    def setup_method(self):
        self.home_page = HomePage()

    def test_download_jump(self):
        self.home_page.goto_download()

    def teardown_method(self):
        self.home_page.close()
