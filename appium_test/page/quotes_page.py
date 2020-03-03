# @Time : 2020-03-02 23:55
from time import sleep

from selenium.webdriver.common.by import By

from appium_test.page.base_page import BasePage
from appium_test.page.search_page import SearchPage


class QuotesPage(BasePage):
    def goto_search(self):
        sleep(10)
        self.find(By.ID, "action_search").click()
        return SearchPage(self._driver)

    def get_follow_stockname(self):
        stock_elements = self._driver.find_elements(By.ID, "portfolio_stockName")
        return [stocks.get_attribute("text") for stocks in stock_elements]

