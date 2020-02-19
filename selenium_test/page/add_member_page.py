# @Time : 2020-02-14 16:17
from selenium.webdriver.common.by import By

from selenium_test.page.base_page import BasePage


class AddMemberPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#contacts"

    def add_member(self):
        name_locator = (By.NAME, "username")
        acctid_locator = (By.NAME, "acctid")
        gender = (By.CSS_SELECTOR, '.ww_radio[value="2"]')
        mobile = (By.NAME, "mobile")
        save = (By.CSS_SELECTOR, ".js_btn_save")
        self.find(name_locator).send_keys("tmac")
        self.find(acctid_locator).send_keys("522929875")
        self.find(gender).click()
        self.find(mobile).send_keys("15399714423")
        self.find(save).click()
        return self
