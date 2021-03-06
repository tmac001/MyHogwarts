from selenium_test.page.base_page import BasePage
from selenium.webdriver.common.by import By

from selenium_test.page.download_page import DownloadPage
from selenium_test.page.login_page import LoginPage
from selenium_test.page.register_page import RegisterPage


class IndexPage(BasePage):
    _base_url = "https://work.weixin.qq.com/"

    def goto_register(self):
        self._driver.find_element(By.LINK_TEXT, '立即注册').click()
        return RegisterPage(self._driver)

    def goto_login(self):
        self._driver.find_element(By.LINK_TEXT, '企业登录').click()
        return LoginPage(self._driver)

    def goto_download(self):
        self._driver.find_element(By.LINK_TEXT, '下载').click()
        return DownloadPage(self._driver)
