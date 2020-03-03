# @Time : 2020-03-01 15:43
from selenium.webdriver.common.by import By
from appium_test.page.base_page import BasePage
from appium_test.page.center_page import CenterPage
from appium_test.page.quotes_page import QuotesPage
from appium_test.page.search_page import SearchPage


class Main(BasePage):
    def goto_search(self):
        self.find(By.ID, "tv_search").click()
        return SearchPage(self._driver)

    def goto_search_by_yaml(self):
        self.load_steps(r"D:\workspace\MyHogwarts\appium_test\page\goto_search_steps.yaml")
        return SearchPage(self._driver)

    def goto_quotes(self):
        locate_quotes = (By.XPATH, "//*[@text='行情' and contains(@resource-id,'tab_name')]")
        self.find(*locate_quotes).click()
        return QuotesPage(self._driver)

    def goto_trade(self):
        pass
        # TODO

    def goto_center(self):
        locate_center = (By.XPATH, "//*[@text='我的' and contains(@resource-id,'tab_name')]")
        self.find(locate_center).click()
        return CenterPage(self._driver)
