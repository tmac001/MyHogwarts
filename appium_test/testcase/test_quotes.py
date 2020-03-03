# @Time : 2020-03-02 23:59
from appium_test.page.app import App


class TestQuotes:
    def setup(self):
        self.quotes = App().start().main().goto_quotes()

    def test_search_in_quotes(self):
        self.quotes.goto_search().search("jd").add_optional("JD").search_close()
        assert "京东" in self.quotes.get_follow_stockname()
