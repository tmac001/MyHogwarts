# @Time : 2020-03-01 18:17
import yaml
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    #  异常弹框列表
    _black_list = [
        (By.ID, "tv_agree"),
        (By.ID, "image_cancel"),
        (By.ID, "ib_close"),
        (By.ID, "tv_left")
    ]
    #  find异常处理重试次数
    _error_max = 3
    _error_count = 0
    #  通过yaml数据驱动时，send_key(value)的值
    _send_key_value = ""

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, by, locate=None):
        """
        封装find_element方法，添加各种因弹出框，元素定位异常处理
        :param by: 支持两种传参方式，1、(定位方式，定位器)元组传入 2、定位方式，定位器分别传入
        :param locate:
        :return:
        """
        try:
            element = self._driver.find_element(*by) if isinstance(by, tuple) else self._driver.find_element(by, locate)
            self._error_count = 0
            return element
        except Exception as e:
            if self._error_count >= self._error_max:
                raise e
            self._error_count += 1
            for element in self._black_list:
                if len(self._driver.find_elements(*element)) > 0:
                    self._driver.find_element(*element).click()
                    return self.find(by, locate)

    def load_steps(self, path):
        """
        加载yaml数据，驱动元素查找、点击、输入等事件
        :param path: 文件路径
        """
        element: WebElement = None
        with open(path) as f:
            steps: list[dict] = yaml.safe_load(f)
        for step in steps:
            if "by" in step.keys():
                element = self.find(step["by"], step["locate"])
            if "action" in step.keys():
                action = step["action"]
                if action == "click":
                    element.click()
                if action == "send_key":
                    #  修改send_key的值
                    step["value"] = self._send_key_value
                    element.send_keys(step["value"])


if __name__ == '__main__':
    BasePage().load_steps(1)
