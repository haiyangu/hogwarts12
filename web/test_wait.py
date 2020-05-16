from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.get('https://home.testing-studio.com')
        self.driver.implicitly_wait(1) #建议都设一个小的隐式等待
    def teardown(self):
        self.driver.quit()
    def test_wait(self):
        # sleep(1)
        self.driver.find_element(By.XPATH, '//*[@title="归入各种类别的所有主题"]').click()
        # sleep(1)

        # 显示等待
        # 这里的wait函数不要再写self函数，这个x是什么意思？？？要不然会传一个参数，咋传的？
        # 知道了，后面这个wait被调用的时候会给它一个默认的driver参数，所以这里必须设一个参数接受
        def wait(x):
            return len(self.driver.find_elements(By.XPATH, '//*[@class="table-heading"]')) >= 1 #这里是elements才有长度len，element没有
        WebDriverWait(self.driver, 10).until(wait) #注意这里的wait传参数的时候一定不要写（）

        # 还可以用expected_conditions。设置各种期待条件
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@class="table-heading"]')))
        self.driver.find_element(By.XPATH, '//*[@title="在最近的一年，一月，一周或一天最活跃的主题"]').click()
