# @Time : 2020-02-15 0:33
from selenium.webdriver.common.by import By

from selenium_test.page.base_page import BasePage


class ImportContactsPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#contacts/import_auto/1688850567609420"

    def import_contacts(self, path):
        # locator_import = (By.CSS_SELECTOR, ".import_settingStage_upload_inputWrap")
        locator_path = (By.ID, "js_upload_file_input")
        locator_submit = (By.ID, "submit_csv")
        # self.find(locator_import).click()
        self.find(locator_path).send_keys(path)
        self.find(locator_submit).click()
        return self
