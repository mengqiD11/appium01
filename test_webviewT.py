
# 该模块用于测试混合应用场景
import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



class TestWebViewT:
    def setup(self):
        desird_cap = {}
        desird_cap['platformName'] = "Android"
        desird_cap['platformVersion'] = "6.0"  # 网易mumu是6.0
        #desird_cap['browserName'] = 'Browser'
        desird_cap['appPackage'] = "com.xueqiu.android"
        desird_cap['appActivity'] = ".view.WelcomeActivityAlias"
        desird_cap['deviceName'] = "192.168.49.103:5555"
        desird_cap['noReset'] = True
        #desird_cap['chromdriverExecutable'] = 'I:/appium/hromdriver/2.23'
        # 指定多个driver的存储目录
        desird_cap['chromedriverExecutableDir'] = 'I:/appium/chromdriver/all'
        # 指定了上面的目录还不行，还需要配置下面的mapping文件，这样即使不是对应的版本，但是可以起到向上兼容的作用，如2.20默认
        # 对应的是43版本，但是指定了mapping文件后就可以向上兼容44
        desird_cap['chromedriverChromeMappingFile'] = 'I:/PycharmProjects/lagou/appium01/mapping.json'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desird_cap)
        self.driver.implicitly_wait(15)
    def test_webviewt(self):
        #点击交易
        self.driver.find_element(MobileBy.XPATH,'//*[@text="交易"]').click()
        #定位A股开户
        a_locator = (MobileBy.XPATH,'//*[@id="Layout_app_3V4"]/div/div/ul/li[1]/div[2]')
        print(self.driver.contexts)
        #切换上下文,从原生切换到webview
        self.driver.switch_to.context(self.driver.contexts[-1])
        print(self.driver.contexts)
        #点击A股开户，点击前加显示等待
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(a_locator))
        #点击A股开户
        self.driver.find_element(*a_locator).click()
        #点击A股开户后，其实打开了一个新的页面，需要先进入新窗口
        kaihu_window = self.driver.window_handles[-1]
        self.driver.switch_to.window(kaihu_window)

        pythonnumber_locator = (MobileBy.ID,'phone-number')
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(pythonnumber_locator))
        #输入用户名密码，点击立即开户
        self.driver.find_element(*pythonnumber_locator).send_keys("13466657656")
        self.driver.find_element(MobileBy.ID,'code').send_keys("1234")
        self.driver.find_element(MobileBy.CSS_SELECTOR,"body > div.container > div > div.form-wrap > div > div.btn-submit > h1").click()


    def teardown(self):
        pass