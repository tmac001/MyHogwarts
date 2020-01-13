from selenium.webdriver.common.by import By

from selenium_test.page.base_page import BasePage


class RegisterPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/register_wx?from=myhome"

    def input_corp_name(self, name):
        """输入企业名称"""
        self._driver.find_element(By.ID, 'corp_name').send_keys(name)
        return self

    def select_corp_industry(self):
        """选择行业类型"""
        self._driver.find_element(By.CSS_SELECTOR, '.js_corp_industry_btn').click()
        self._driver.find_element(By.CSS_SELECTOR, '.register_industry_maintype_item_link').click()
        self._driver.find_element(By.CSS_SELECTOR, '.js_register_industry_subtype_item').click()
        return self

    def select_dropdown(self):
        """选择人员规模"""
        self._driver.find_elements(By.CSS_SELECTOR, '.ww_btn_Dropdown_label')[1].click()
        self._driver.find_element(By.XPATH, '//li[2]/a/span[2]').click()
        return self

    def input_manager_name(self, name):
        self._driver.find_element(By.CSS_SELECTOR, "[id='manager_name']").send_keys(name)
        return self

    def input_register_tel(self, tel):
        self._driver.find_element(By.CSS_SELECTOR, "[id='register_tel']").send_keys(tel)
        return self

    # 点击获取验证码，需要正确手机号后才能输入
    def input_code(self):
        self._driver.find_element(By.CSS_SELECTOR, "[id='get_vcode']").click()
        return self

    # 验证码需要输入正确手机号，后才能输入
    def input_code(self, code):
        self._driver.find_element(By.CSS_SELECTOR, "[id='vcode']").send_keys(code)
        return self

    def select_agree(self):
        self._driver.find_element(By.CSS_SELECTOR, "[id='iagree']").click()
        return self

    def register_submit(self):
        """click register button
            return The current page object
        """
        self._driver.find_element(By.ID, 'submit_btn').click()
        return self

    def get_error_messages(self):
        """"""
        error_list = []
        element_list = self._driver.find_elements(By.CSS_SELECTOR, ".js_error_msg")
        [error_list.append(i.text) for i in element_list]
        print(error_list)
        return error_list
