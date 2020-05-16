from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains, TouchActions
from selenium.webdriver.common.keys import Keys


class TestActionChains():
    '''
    A class to test ActionChains.
    '''
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_clicks(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        element_click = self.driver.find_element_by_xpath("/html/body/form/input[3]")
        element_right_click = self.driver.find_element_by_xpath("/html/body/form/input[4]")
        element_double_click= self.driver.find_element_by_xpath("/html/body/form/input[2]")
        actions = ActionChains(self.driver)
        actions.click(element_click)
        actions.context_click(element_right_click)
        actions.double_click(element_double_click)
        actions.perform()
        sleep(3)

    def test_dragdrop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        element_from = self.driver.find_element_by_xpath("//*[@id='dragger']")
        element_to = self.driver.find_element_by_xpath("/html/body/div[3]")
        actions = ActionChains(self.driver)
        # 这里给出了三种拖拽的方法
        actions.drag_and_drop(element_from, element_to).perform()
        # actions.click_and_hold(element_from).release(element_to).perform()
        # actions.click_and_hold(element_from).move_to_element(element_to).release().perform()
        sleep(3)

    def test_move(self):
        self.driver.get("https://www.baidu.com/")
        element = self.driver.find_element_by_xpath('//*[@id="s-usersetting-top"]')
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.perform()
        sleep(3)

    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        input_box = self.driver.find_element_by_xpath("/html/body/label[1]/input")
        input_box.click()
        actions = ActionChains(self.driver)
        actions.send_keys("username").send_keys(Keys.SPACE).send_keys("Tom").perform()
        sleep(3)

class TestTouchActions():
    '''
    A class to test TouchActions.
    '''
    def setup(self):
        # 这里是这样解决下面的报错的
        # selenium.common.exceptions.WebDriverException: Message: unknown command: Cannot call non W3C standard command while in W3C mode
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_scroll_to_bottom(self):
        self.driver.get("https://www.baidu.com/")
        input_box = self.driver.find_element_by_id("kw")
        search_button = self.driver.find_element_by_id("su")
        input_box.send_keys("selenium测试")
        action = TouchActions(self.driver)
        action.tap(search_button) # 点击操作
        action.scroll_from_element(input_box, 0, 10000).perform() # 滑动到最底端一般给一个很大的偏移量
        sleep(3)