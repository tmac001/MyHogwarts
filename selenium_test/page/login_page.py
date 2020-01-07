from selenium.webdriver.common.by import By

from selenium_test.page.base_page import BasePage


class LoginPage(BasePage):
    def goto_register(self):
        self._driver.find_element(By.LINK_TEXT, "企业注测").click()
        from selenium_test.page.register_page import RegisterPage
        return RegisterPage(self._driver)
