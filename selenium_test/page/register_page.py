from selenium.webdriver.common.by import By

from selenium_test.page.base_page import BasePage


class RegisterPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/register_wx?from=myhome"

    def input_corp_name(self, name):
        self._driver.find_element(By.ID, 'corp_name').send_keys(name)
        return self

    def get_error_messages(self):
        """"""
        error_list = []
        element_list = self._driver.find_elements(By.CSS_SELECTOR, ".js_error_msg")
        for i in element_list:
            error_list.append(i.text)
        print(error_list)
        return error_list

    def register_failed(self):
        """click register button
            return The current page object
        """
        self._driver.find_element(By.ID, 'submit_btn').click()
        return self

