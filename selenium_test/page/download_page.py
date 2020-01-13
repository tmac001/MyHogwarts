from selenium.webdriver.common.by import By

from selenium_test.page.base_page import BasePage


class DownloadPage(BasePage):
    _base_url = "https://work.weixin.qq.com/#indexDownload"

    def get_download_item_title(self):
        download_items = []
        for i in self._driver.find_elements(By.CSS_SELECTOR, '.index_download_item_title'):
            download_items.append(i.text)
        return download_items

