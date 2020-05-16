import selenium
from selenium import webdriver
# pip install selenium -i https://mirrors.aliyun.com/pypi/simple

from time import sleep

# def test_selenium():
#     driver = webdriver.Chrome() # 调用记得加括号
#     driver.get("https://www.baidu.com")
from selenium.webdriver.common.by import By


class TestHogwarts():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3) #我的不行！！！

    def teardown(self):
        self.driver.quit()

    def test_hogwarts(self):
        self.driver.get("http://www.testerhome.com")
        self.driver.find_element_by_link_text("社团").click()
        #self.driver.find_element_by_link_text("霍格沃兹测试学院").click()
        self.driver.find_element_by_xpath("//*[@id='hot_teams']/div[2]/div/div[1]/div/div[2]/div[1]/a").click()
        self.driver.find_element_by_css_selector(".topic-22621 .title > a").click() # 不推荐用css，因为这个topic可能变化

    def test_elements(self):
        self.driver.get("https://www.baidu.com")
        # 可以用很多方式实现同一个功能，底层基本都是CSS实现
        # self.driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys("霍格沃兹测试学院")
        # self.driver.find_element(By.ID, 'kw').send_keys("霍格沃兹测试学院")
        self.driver.find_element(By.CSS_SELECTOR, '#kw').send_keys("霍格沃兹测试学院")


