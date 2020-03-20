# @Time : 2020-02-16 13:51
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import os
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestAppium:
    def setup(self):
        caps = {}
        caps["appPackage"] = "com.xueqiu.android"
        caps["platformName"] = "Android"
        caps["deviceName"] = "test"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["noReset"] = True
        caps["udid"] = os.getenv("udid")
        # caps["dontStopAppOnReset"] = True
        # caps["unicodeKeyboard"] = True
        # caps["resetKeyboard"] = True
        caps["chromedriverExecutable"] = r"D:\data\appium\chromedriver\44\chromedriver.exe"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(20)

    def test_search(self):
        self.driver.find_element(MobileBy.ID, "tv_search").click()
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("特斯拉")

    def test_scroll(self):
        size = self.driver.get_window_rect()
        for i in range(10):
            TouchAction(self.driver).long_press(x=size["width"] * 0.5, y=size["height"] * 0.8) \
                .move_to(x=size["width"] * 0.5, y=size["height"] * 0.2) \
                .release() \
                .perform()

    def test_get_price(self):
        self.driver.find_element(MobileBy.ID, "tv_search").click()
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(MobileBy.ID, "search_input_text").click()
        self.driver.find_element(MobileBy.ID, "name").click()
        resource_id = self.driver.find_element(MobileBy.XPATH,
                                               "//*[@text=09988]/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").get_attribute(
            "text")
        # print(self.driver.find_element(MobileBy.ID, "resource_id").get_attribute("resourceId"))
        print(resource_id)
        assert float(resource_id) > 200

    def test_my_follow(self):
        follow_bn = (MobileBy.XPATH, "// *[ @ text = 'TSLA'] /../../..// *[contains(@resource-id,'follow_btn')]")
        followed_bn = (MobileBy.XPATH, "// *[ @ text = 'TSLA'] /../../..// *[contains(@resource-id,'followed_btn')]")
        self.driver.find_element(MobileBy.ID, "tv_search").click()
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("特斯拉")
        self.driver.find_element(MobileBy.ID, "search_input_text").click()
        self.driver.find_element(MobileBy.ID, "name").click()
        self.driver.find_element(*follow_bn).click()
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("特斯拉")
        self.driver.find_element(MobileBy.ID, "search_input_text").click()
        self.driver.find_element(MobileBy.ID, "name").click()
        assert self.driver.find_element(*followed_bn).get_attribute("text") == "已添加"
        self.driver.find_element(*followed_bn).click()

    def test_get_source(self):
        with open("page_source.xml", "w") as f:
            f.write(self.driver.page_source)

    def test_webview(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='交易' and contains(@resource-id,'tab_name')]").click()
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "A股开户").click()
        phone_number = (MobileBy.XPATH, " //android.widget.EditText")
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(phone_number))
        self.driver.find_element(*phone_number).send_keys("15399714423")
        self.driver.find_element(MobileBy.ID, "code").send_keys("12345")

    def test_webview_dubug(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='交易' and contains(@resource-id,'tab_name')]").click()
        WebDriverWait(self.driver, 30).until(lambda x: len(self.driver.contexts) > 1)
        # sleep(10)
        print(self.driver.contexts)
        self.driver.switch_to.context(self.driver.contexts[-1])
        self.driver.find_element(By.CSS_SELECTOR, ".trade_home_info_3aI").click()
        WebDriverWait(self.driver, 30).until(lambda x: len(self.driver.window_handles) > 3)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        phone = (By.ID, 'phone-number')
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(phone))
        self.driver.find_element(*phone).send_keys("15399714423")

    def test_webdriver_hk(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='交易' and contains(@resource-id,'tab_name')]").click()
        WebDriverWait(self.driver, 30).until(lambda x: len(self.driver.contexts) > 1)
        print(self.driver.contexts)
        self.driver.switch_to.context(self.driver.contexts[-1])
        self.driver.find_elements(By.CSS_SELECTOR, ".trade_home_info_3aI")[2].click()
        WebDriverWait(self.driver, 30).until(lambda x: len(self.driver.window_handles) > 3)
        print(self.driver.window_handles)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        phone = (By.CSS_SELECTOR, '[placeholder="请输入手机号"]')
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(phone))
        self.driver.find_element(*phone).send_keys('15399714423')
        self.driver.switch_to.context(self.driver.contexts[0])
        self.driver.find_element(MobileBy.ID, 'action_bar_back').click()

    def teardown(self):
        sleep(5)
        self.driver.quit()
