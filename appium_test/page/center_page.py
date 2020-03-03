# @Time : 2020-03-02 14:31
from selenium.webdriver.common.by import By

from appium_test.page.base_page import BasePage


class CenterPage(BasePage):
    def login_by_password(self, name, pwd):
        self.find(By.XPATH, "//*[@text='帐号密码登录']").click()
        self.find(By.ID, "login_account").send_keys(name)
        self.find(By.ID, "login_password").send_keys(pwd)
        self.find(By.ID, "button_next").click()
        return self

    def get_error_msg(self) -> str:
        msg = self.find(By.ID, "md_content").get_attribute("text")
        return msg
