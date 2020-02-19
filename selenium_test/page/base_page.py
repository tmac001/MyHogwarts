from time import sleep

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _base_url = ""

    def __init__(self, driver: WebDriver = None, reuse=False):
        if driver is None:
            if reuse:
                options = webdriver.ChromeOptions()
                options.debugger_address = "127.0.0.1:9222"

                # index页面会使用这个
                self._driver = webdriver.Chrome(options=options)
            else:
                self._driver = webdriver.Chrome()
            self._driver.implicitly_wait(2)
        else:
            # Login与Register等页面需要用这个方法
            self._driver = driver
        self._driver.get(self._base_url)

    def find(self, locator):
        return self._driver.find_element(*locator)

    def close(self):
        sleep(10)
        self._driver.quit()
