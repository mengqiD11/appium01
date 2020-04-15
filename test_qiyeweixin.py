from time import sleep

import pytest
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException


class TestQiYeWeiXin:
    def setup(self):
        desird_cap = {}
        desird_cap['platformName'] = "Android"
        desird_cap['platformVersion'] = "6.0"  # 网易mumu是6.0
        desird_cap['deviceName'] = "127.0.0.1:7555"
        desird_cap['appPackage'] = "com.tencent.wework"
        desird_cap['appActivity'] = ".launch.LaunchSplashActivity"
        desird_cap['noReset'] = True
        # desird_cap['dontStopAppOnReset'] = 'true' 感觉这个参数不好用
        desird_cap['skipDeviceInitialization'] = True  # 每次启动，跳过安装、权限设置等操作
        desird_cap['unicodeKeyBoard'] = 'true'  # 输入中文需要设置这个
        desird_cap['resetKeyBoard'] = 'true'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desird_cap)
        self.driver.implicitly_wait(15)

    def test_searc(self):

        '''
        打开企业微信（提前登录）
        进入通讯录
        点击搜索按钮
        输入 已存在的联系人姓名, 例如“aa”，
        点击联系人，进入聊天页面
        输入“测试code”
        点击发送
        退出应用
        '''

        # 点击通讯录
        self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/dnj' and @text='通讯录']").click()
        # 点击搜索按钮
        self.driver.find_element_by_id("com.tencent.wework:id/gq_").click()
        # 输入搜索内容
        self.driver.find_element_by_id("com.tencent.wework:id/ffq").send_keys("采儿")

        # 点击搜索结果
        try:
            self.driver.find_element_by_id("com.tencent.wework:id/de1").click()
        except NoSuchElementException:
            print("无此联系人！")
            return

        # 点击发送消息按钮
        self.driver.find_element_by_id("com.tencent.wework:id/aaj").click()
        # 输入消息
        self.driver.find_element_by_id("com.tencent.wework:id/dtv").send_keys("测试code")
        # 点击发送
        self.driver.find_element_by_id("com.tencent.wework:id/dtr").click()

    def teardown(self):
        self.driver.quit()

    if __name__ == '__main__':
        pytest.main()
