# @Time : 2020-02-14 0:19
from selenium.webdriver.common.by import By

from selenium_test.page.add_member_page import AddMemberPage
from selenium_test.page.base_page import BasePage
from selenium_test.page.create_message_page import CreateMessagePage
from selenium_test.page.import_contacts_page import ImportContactsPage


class HomePage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame"

    def go_add_member(self):
        locator = (By.LINK_TEXT, '添加成员')
        # self.find(locator).click()
        self._driver.execute_script("arguments[0].click();", self.find(locator))
        return AddMemberPage(self._driver, reuse=True)

    def go_group_message(self):
        locator = (By.CSS_SELECTOR, ".ww_indexImg_GroupMessage")
        self.find(locator).click()
        return CreateMessagePage(self._driver, reuse=True)

    def go_import_contacts(self):
        locator = (By.CSS_SELECTOR, ".ww_indexImg_Import")
        self.find(locator).click()
        return ImportContactsPage(self._driver, reuse=True)
