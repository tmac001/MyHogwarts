from selenium_test.page.base_page import BasePage
from selenium.webdriver.common.by import By

from selenium_test.page.register_page import RegisterPage


class HomePage(BasePage):
    _base_url = "https://work.weixin.qq.com/"

    def goto_register(self):
        self._driver.find_element(By.LINK_TEXT, '立即注册').click()
        return RegisterPage(self._driver)

    def goto_login(self):
        self._driver.find_element(By.LINK_TEXT, '企业登录').click()

    def goto_dowload(self):
        self._driver.find_element(By.LINK_TEXT, '下载').click()
