# @Time : 2020-03-01 15:50
from selenium.webdriver.common.by import By
from appium_test.page.base_page import BasePage


class SearchPage(BasePage):
    def search(self, title):
        self.find(By.ID, "search_input_text").send_keys(title)
        self.find(By.ID, "name").click()
        return self

    def search_by_yaml(self, value):
        self._send_key_value = value
        self.load_steps(r"D:\workspace\MyHogwarts\appium_test\page\search_steps.yaml")
        return self

    def get_price(self) -> float:
        price_locate = (By.ID, 'current_price')
        return float(self.find(*price_locate).get_attribute("text"))

    def add_optional(self, name):
        follow_xpath = "// *[ @ text = '%s'] /../../..// *[contains(@resource-id,'follow_btn')]" % name
        print(follow_xpath)
        follow_locate = (By.XPATH, follow_xpath)
        self.find(*follow_locate).click()
        return self

    def cancel_optional(self, name):
        followed_xpath = "// *[ @ text = '%s'] /../../..// *[contains(@resource-id,'followed_btn')]" % name
        print(followed_xpath)
        followed_locate = (By.XPATH, followed_xpath)
        self.find(*followed_locate).click()
        return self

    def search_close(self):
        self.find(By.ID, "action_close").click()
