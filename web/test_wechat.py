import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class TestWechatLogin():
    '''
    A class to test login wechat by debug address.
    '''
    def setup(self):
        option = Options()
        # 我的总是连不上！！！
        # 是要把后台的所有与chrome相关的程序都要关掉啊！！！那些Google程序
        option.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_info_access(self):
        self.driver.find_element_by_xpath("//*[@id='menu_contacts']/span").click()
        sleep(3)

    # 在这里复用当前的浏览器获得登录的cookie，并将这个cookie存储到shelve中
    def test_get_current_cookies(self):
        print(self.driver.get_cookies())
        db = shelve.open("cookies")
        db['cookie'] = self.driver.get_cookies()

class TestCookieLogin():
    '''
    A class to test login wechat by cookies.
    '''
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    # 这里不再复用当前的浏览器，而是新打开一个登录界面，为其注入cookie之后再访问登录
    def test_login_with_cookie(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

        # 注入cookies
        db = shelve.open("cookies")
        login_cookies = db['cookie']
        for cookie in login_cookies:
            print(cookie)
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element_by_xpath("//*[@id='menu_contacts']/span").click()
        db.close()
        sleep(3)
