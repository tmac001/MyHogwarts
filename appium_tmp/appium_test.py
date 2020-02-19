# @Time : 2020-02-16 13:51
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction


class TestAppium:
    def setup(self):
        caps = {}
        caps["appPackage"] = "com.xueqiu.android"
        caps["platformName"] = "Android"
        caps["deviceName"] = "test"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["noReset"] = True
        # caps["dontStopAppOnReset"] = True
        # caps["unicodeKeyboard"] = True
        # caps["resetKeyboard"] = True

        self.driver = webdriver.Remote("http://localho:4723/wd/hub", caps)
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

    def teardown(self):
        # pass
        self.driver.quit()
