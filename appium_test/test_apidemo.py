# @Time : 2020-02-24 0:24
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By


class TestApi:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "io.appium.android.apis"
        caps["appActivity"] = ".ApiDemos"
        caps["skipServerInstallation"] = True
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def test_api(self):
        scroll_to_element = (
            MobileBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable('
            'new UiSelector().scrollable(true).instance(0))'
            '.scrollIntoView('
            'new UiSelector().text("Views").instance(0));')
        self.driver.find_element(*scroll_to_element).click()

        scroll_to_element = (
            MobileBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable('
            'new UiSelector().scrollable(true).instance(0))'
            '.scrollIntoView('
            'new UiSelector().text("Popup Menu").instance(0));')
        self.driver.find_element(*scroll_to_element).click()

        self.driver.find_element(MobileBy.XPATH, "//*[@text='MAKE A POPUP!']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='Search' and contains(@resource-id,'title')]").click()
        toast = self.driver.find_element(By.XPATH, "//*[@class='android.widget.Toast']").text
        assert "Search" in toast

    def teardown(self):
        sleep(5)
        self.driver.quit()
