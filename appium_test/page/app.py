# @Time : 2020-03-01 15:13
from time import sleep

from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from appium_test.page.base_page import BasePage
from appium_test.page.main import Main


class App(BasePage):
    _package = "com.xueqiu.android"
    _activity = ".view.WelcomeActivityAlias"
    _main_page_source = ["我的", "同意", "升级", "image_cancel"]

    def start(self, driver: WebDriver = None):
        if driver is None:
            caps = {"appPackage": self._package,
                    "platformName": "Android",
                    "deviceName": "test",
                    "appActivity": self._activity,
                    # "noReset": True,
                    "chromedriverExecutable": r"D:\data\appium\chromedriver\44\chromedriver.exe"}
            # self._driver = webdriver.Remote("http://localhost:4444/wd/hub", caps)
            # grid 模式
            self._driver = webdriver.Remote("http://192.168.1.6:5555/wd/hub", caps)

            self._driver.implicitly_wait(5)
        else:
            self._driver.start_activity(self._package, self._activity)
        return self

    def restart(self):
        self._driver.start_activity("com.xueqiu.android", ".view.WelcomeActivityAlias")

    def main(self):

        def wait_load_main(driver):
            source = self._driver.page_source
            if "我的" in source or "同意" in source or "image_cancel" in source:
                return True
            return False

        WebDriverWait(self._driver, 30).until(wait_load_main)
        return Main(self._driver)

    def quit(self):
        self._driver.quit()
