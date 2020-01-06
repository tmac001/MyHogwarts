from selenium.webdriver.common.by import By

from selenium_test.page.base_page import BasePage


class RegisterPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/register_wx?from=myhome"

    def input_corp_name(self, name):
        self._driver.find_element(By.ID, 'corp_name').send_keys(name)
        return self

    def register_submit(self):
        self._driver.find_element(By.ID, 'submit_btn').click()
