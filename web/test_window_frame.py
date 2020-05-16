from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains


class TestSwitchWindow():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_switch_window(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_xpath("//*[@id='u1']/a[2]").click() # 点击登录按钮 frame，弹出来的登录页面是div
        print(self.driver.current_window_handle) # 打印当前窗口的句柄
        print(self.driver.window_handles) # 打印所有窗口的句柄

        self.driver.find_element_by_link_text("立即注册").click()
        # 此时已经开始出现第二个页面，即注册页面
        print(self.driver.current_window_handle)  # 打印当前窗口的句柄
        print(self.driver.window_handles)  # 打印所有窗口的句柄

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1]) # 切换到最后打开的那个窗口，也就是注册窗口

        self.driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_4__userName']").send_keys("user")
        self.driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_4__phone']").send_keys("111111111")
        sleep(2)

        self.driver.switch_to.window(windows[0]) # 再切回刚才的登陆页面
        sleep(2)

    def test_switch_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        # 首先切换到右边的frame，并寻找里面的元素
        self.driver.switch_to.frame("iframeResult")
        drag_element = self.driver.find_element_by_xpath("//*[@id='draggable']")
        drop_element = self.driver.find_element_by_xpath("//*[@id='droppable']")

        # 然后执行拖拽操作
        actions = ActionChains(self.driver)
        actions.drag_and_drop(drag_element, drop_element).perform()
        sleep(2)

        # 此时屏幕上方会出现一个小弹框，下面的操作将切换到弹窗并且点击确定操作
        self.driver.switch_to.alert.accept()
        sleep(2)

        # 最后切换回原来的frame，恢复原来的样子
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath("//*[@id='submitBTN']").click()
        # self.driver.switch_to.parent_frame()
        sleep(2)