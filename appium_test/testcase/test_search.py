# @Time : 2020-03-01 16:06
import pytest
import yaml

from appium_test.page.app import App


class TestSearch:
    def setup(self):
        self.main = App().start().main()

    @pytest.mark.parametrize("title,price", [
        ("Alibaba", 100),
        ("tsla", 200)
    ])
    def test_search_tesla(self, title, price):
        assert self.main.goto_search().search(title).get_price() > price

    #  数据驱动
    @pytest.mark.parametrize("title,price", yaml.safe_load(open("search.yaml")))
    def test_search_tesla1(self, title, price):
        assert self.main.goto_search().search(title).get_price() > price

    def test_goto_search_by_yaml(self):
        self.main.goto_search_by_yaml()

    def test_search_by_yaml(self):
        self.main.goto_search_by_yaml().search_by_yaml("tsla")
