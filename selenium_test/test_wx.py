import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWx:
    def setup_method(self):
        options = webdriver.ChromeOptions()
        # 设置启动debug模式浏览器
        # options.debugger_address = "127.0.0.1:9222"

        # 设置无界面模式的启动方式，使用headless模式
        # options.add_argument("--headless")
        # options.add_argument("--disable-gpu")
        # options.add_argument("--window-size=1280,1696")

        # 通过设置变量值，处理多浏览器的方式，
        # browser = os.getenv("browser", "").lower()
        # print(browser)
        # if browser == "headless":
        #     self.driver = webdriver.PhantomJS(options=options)
        # elif browser == "firefox":
        #     self.driver = webdriver.Firefox(options=options)
        # else:
        #     self.driver = webdriver.Chrome(options=options)
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(r"https://work.weixin.qq.com/wework_admin/frame")
        self.driver.implicitly_wait(3)
        self.member = {
            "username": "le",
            "english_name": "tmac",
            "acctid": "1111",
            "phone": "15399714424",
            "telphone": "15399714423",
            "mail": "522929875@qq.com",
            "address": "hunan",
            "title": "ll"
        }

    def wait(self, times, method):
        WebDriverWait(self.driver, times).until(method)
        WebDriverWait(self.driver, timeout=10).until(method)

    def test_add(self):
        self.driver.find_element(By.LINK_TEXT, "通讯录").click()
        self.wait(10, self.find_add_member)
        element_form = (By.CSS_SELECTOR, '[id="username"]')
        self.wait(10, expected_conditions.element_to_be_clickable(element_form))
        self.driver.find_element(By.CSS_SELECTOR, '[id="username"]').send_keys(self.member["username"])
        self.driver.find_element(By.CSS_SELECTOR, '[id="memberAdd_english_name"]').send_keys(
            self.member["english_name"])
        self.driver.find_element(By.CSS_SELECTOR, '[id="memberAdd_acctid"]').send_keys(self.member["acctid"])
        self.driver.find_element(By.CSS_SELECTOR, '[id="memberAdd_phone"]').send_keys(self.member["phone"])
        self.driver.find_element(By.CSS_SELECTOR, '[id="memberAdd_telephone"]').send_keys(self.member["telphone"])
        self.driver.find_element(By.CSS_SELECTOR, '[id="memberAdd_mail"]').send_keys(self.member["mail"])
        self.driver.find_element(By.CSS_SELECTOR, '[id="memberEdit_address"]').send_keys(self.member["address"])
        self.driver.find_element(By.CSS_SELECTOR, '[id="memberAdd_title"]').send_keys(self.member["title"])
        self.driver.find_element(By.LINK_TEXT, "保存").click()

    def find_add_member(self, X):
        # self.driver.find_element(By.LINK_TEXT, "添加成员").click()
        element_exit = len(self.driver.find_elements(By.ID, 'username'))
        if element_exit < 1:
            self.driver.find_element(By.CSS_SELECTOR, '.js_has_member > div:nth-child(1) > .js_add_member').click()
        return element_exit >= 1

    def teardowm_method(self):
        time.sleep(3)
        self.driver.quit()
