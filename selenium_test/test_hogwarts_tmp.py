import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestDefaultSuite:
    def setup_method(self):
        options = webdriver.ChromeOptions()
        # 设置无界面模式的启动方式，使用headless模式
        # options.add_argument("--headless")
        # options.add_argument("--disable-gpu")
        # options.add_argument("--window-size=1280,1696")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://testerhome.com/")

    def teardown_method(self):
        time.sleep(3)
        self.driver.quit()

    def wait(self, times, method):
        WebDriverWait(self.driver, times).until(method)

    def test_hogwarts(self):
        """进入testerhome，访问社团，访问霍格沃兹测试学院，访问最顶部的第一个帖子"""
        element_teams = (By.LINK_TEXT, "社团")
        self.wait(10, expected_conditions.element_to_be_clickable(element_teams))
        self.driver.find_element(*element_teams).click()
        element_team_name = (By.CSS_SELECTOR, '[data-name="霍格沃兹测试学院"]')
        self.wait(10, expected_conditions.presence_of_element_located(element_team_name))
        self.driver.find_element(*element_team_name).click()
        element_fister_post = (By.CSS_SELECTOR,
                               "div.panel-body > div:nth-child(1) > div.infos.media-body "
                               "> div.title.media-heading > a")
        self.wait(10, expected_conditions.element_to_be_clickable(element_fister_post))
        self.driver.find_element(*element_fister_post).click()

    def test_mtsc2020(self):
        """进入testerhome，访问MTSC2020置顶帖，点击目录，点击议题征集范围"""
        element_mtsc_post = (By.CSS_SELECTOR, '[title="MTSC2020 中国互联网测试开发大会议题征集"]')
        self.wait(10, expected_conditions.element_to_be_clickable(element_mtsc_post))
        self.driver.find_element(*element_mtsc_post).click()
        element_menu = (By.CSS_SELECTOR, '.btn-default:nth-child(1)')
        self.wait(10, expected_conditions.element_to_be_clickable(element_menu))
        self.driver.find_element(*element_menu).click()
        element_child_menu = (By.LINK_TEXT, '征集议题范围')
        self.wait(10,expected_conditions.element_to_be_clickable(element_child_menu))
        self.driver.find_element(*element_child_menu).click()

    # def test_wx(self):
    #     option = webdriver.ChromeOptions()
