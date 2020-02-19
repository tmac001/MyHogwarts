# @Time : 2020-02-15 17:45
from time import sleep

from selenium.webdriver.common.by import By

from selenium_test.page.base_page import BasePage


class CreateMessagePage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#createMessage"

    def send_message(self):
        locator_select_apps = (By.CSS_SELECTOR, ".js_select_apps_btn")
        locator_app_title = (By.CSS_SELECTOR, '[data-name="TESTHOME"]')
        locator_submit = (By.CSS_SELECTOR, '[d_ck="submit"]')
        locator_select_range = (By.LINK_TEXT, "选择发送范围")
        locaator_memberSearch = (By.ID, "memberSearchInput")
        locator_peopleName = (By.CSS_SELECTOR, ".ww_searchResult_title_peopleName")
        locator_msg_text = (By.CSS_SELECTOR, ".js_send_msg_text")
        self.find(locator_select_apps).click()
        self.find(locator_app_title).click()
        sleep(5)
        self.find(locator_submit).click()
        self.find(locator_select_range).click()
        self.find(locaator_memberSearch).send_keys("李庆国")
        self.find(locator_peopleName).click()
        self.find(locator_submit).click()
        self.find(locator_msg_text).send_keys("dfsdf")
        return self
